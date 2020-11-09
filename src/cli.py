'''
MIT License

Copyright (c) 2020 Cedric Fauth

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import argparse
import logging
from utils import Symbol as sym

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)

class CLI_Parser:

    def __init__(self):
        # init parser
        self.parser = argparse.ArgumentParser('dolist client')
        self.subparsers = self.parser.add_subparsers(dest="cmd")
        # event args
        self.e_parser = self.subparsers.add_parser('event', help='add an event (event -h)')
        self.e_parser.add_argument('title', type=str, action='store', help='event title')
        self.e_parser.add_argument('-d', type=str, action='store', help='weekday or date')
        self.e_parser.add_argument('-t', type=str, action='store', required=True, help='time period HH:MM-HH:MM')
        self.e_parser.add_argument('-f', type=str, action='store', required=True, help='frequency')
        # task args
        self.t_parser = self.subparsers.add_parser('task', help='add a task (task -h)')
        self.t_parser.add_argument('title', type=str, action='store', help='task title')
        self.t_parser.add_argument('-d', type=str, action='store', help='weekday')
        self.t_parser.add_argument('-t', type=str, action='store', required=True, help='time HH:MM')
        self.t_parser.add_argument('-f', type=str, action='store', required=True, help='frequency')
        # remove
        self.rm_parser = self.subparsers.add_parser('rm', help='remove event or task')
        self.rm_group = self.rm_parser.add_mutually_exclusive_group(required=True)
        self.rm_group.add_argument('-e', action='store_true', help='remove event')
        self.rm_group.add_argument('-t', action='store_true', help='remove task')
        self.rm_parser.add_argument('id', type=int, action='store', help='id of event/task')
        # list
        self.ls_parser = self.subparsers.add_parser('ls', help='list all id\'s')
        # done
        self.done_parser = self.subparsers.add_parser('done', help='mark a task as done\'s')
        self.done_parser.add_argument('task_id', type=int, action='store', help='task ID')
        # parse
        self.args = self.parser.parse_args()
        logger.debug(self.args)

class Output:

    int_to_days = {None: '', 0: "mon", 1: "tue", 2: "wed", 3: "thu",
        4: "fri", 5: "sat", 6: "sun"}
    
    char_to_freq = {'w': 'weekly', 'd': 'daily', 'o': 'once'}

    @staticmethod
    def open():
        # \033[2J\033[H clear screen
        print(f'{sym.default()}', end='', flush=True)
    
    @staticmethod
    def close():
        print(sym.RESET, end='', flush=True)

    @staticmethod
    def info(msg):
        """
        prints an info text
        """
        print(f' {sym.MAGENTA}{sym.DONE}{sym.default()} {msg}')
    
    @staticmethod
    def error(msg):
        """
        prints an error text
        """
        print(f' {sym.RED}{sym.ERR}{sym.default()} {msg}')
    
    # TODO SHOW ALL PARAMETERS
    @staticmethod
    def list_all(events, tasks):
        le = len(events) - 1
        lt = len(tasks) - 1
        event_head = f'{sym.CYAN} event [ID] [TITLE]{"".join(" " for _ in range(25))}' + \
            f'[FREQ] [DAY] [DATE]     [FROM - TO]{sym.default()}'
        task_head = f'\n{sym.MAGENTA} task  [ID] [TITLE]{"".join(" " for _ in range(31))}' + \
            f'[FREQ] [DAY] [DATE]     [DUE]{sym.default()}'
        out = event_head
        for i,e in enumerate(events):
            title = Output.align_text_left(e[1], 31)
            freq = Output.align_text_left(Output.char_to_freq[e[5]], 6)
            day = Output.align_text_left(Output.int_to_days[e[2]], 5)
            date = (e[6] if e[6] != None else '          ')
            if i == le:
                out += f'\n {sym.BOX2}{sym.BOX3*4} '
            else:
                out += f'\n {sym.BOX1}{sym.BOX3*4} ' 
            out += f'{Output.align_text_left(str(e[0]), 4)} {title} {freq} {day} {date} {e[3]}-{e[4]}'
        out += task_head
        for i,t in enumerate(tasks):
            title = Output.align_text_left(t[1], 37)
            freq = Output.align_text_left(Output.char_to_freq[t[4]], 6)
            day = Output.align_text_left(Output.int_to_days[t[2]], 5)
            date = (t[5] if t[5] != None else '          ')
            if i == lt:
                out += f'\n {sym.BOX2}{sym.BOX3*4} '
            else:
                out += f'\n {sym.BOX1}{sym.BOX3*4} ' 
            out += f'{Output.align_text_left(str(t[0]), 4)} {title} {freq} {day} {date} {t[3]}'
        out += sym.default()
        print(out, flush=True)

    @staticmethod
    def align_text_left(title, max_len):
        """
        shortens or extends a title to max_len
        """
        if len(title) > max_len:
            return title[:max_len - 3] + '...'
        else:
            return title + ''.join(' ' for _ in range(max_len-len(title)))

    @staticmethod
    def align_text_right(title, max_len):
        """
        shortens or extends a title to max_len
        """
        if len(title) > max_len:
            return '...' + title[-(max_len-3):]
        else:
            return ''.join(' ' for _ in range(max_len-len(title))) + title

    @staticmethod
    def format_time(days, hours, minutes, now=False):
        if days < 0:
            if now:
                return f'(now)'
            return '(missed)'
        elif days == 0 and hours == 0:
            return f'({minutes}m)'
        elif days == 0:
            return f'({hours}h{minutes:02}m)'
        else:
            return f'({days}d{hours:02}h{minutes:02}m)'

    @staticmethod
    def color_time(days, hours, minutes, time_string):
        """
        colors a time string
        """
        if days < 1: # missed
            return f'{sym.RED}{time_string}'
        elif days == 0 and hours < 3: # less than 2h left
            return f'{sym.BRED}{time_string}'
        elif days < 3: # less than one day daft
            return f'{sym.YELLOW}{time_string}'
        else:
            return f'{sym.default()}{time_string}'

    @staticmethod
    def overview(events, tasks, tasks_done):

        # TODO sym class \u2500...
        # TODO more functions for 'left' + colors
        # TODO less code per line

        out = f'{sym.default()}{sym.CYAN}{sym.HLINE*3}[ \u001b[1mToday\'s Events{sym.default()}{sym.CYAN} ]' \
            + f'{sym.HLINE*59}{sym.default()}'
        
        if len(events) == 0:
            out += "\n   No events found for today. Use 'dl event -h' and add new events :)"
        i = 0
        for e in events:
            if e[7] < 0 and e[10] == False:
                continue
            title = Output.align_text_left(e[1], 50)
            if i == 0 or (e[7] < 0 and e[10] == True):
                out += f'\n{sym.BLUE} {sym.ARROW} {sym.default()}'
                time_left = Output.align_text_right(f'{Output.format_time(*e[7:11])}',9)
                out += f'{title} [{e[5]}] {e[3]}-{e[4]} {sym.CYAN}{time_left}{sym.default()}'
            else:
                out += f'\n{sym.BLUE} {sym.ARROW} {sym.default()}{sym.DIM}'
                time_left = Output.align_text_right(f'{Output.format_time(*e[7:10])}',9)
                out += f'{title} [{e[5]}] {e[3]}-{e[4]} {time_left}{sym.default()}'
            i += 1

        out += f'\n{sym.MAGENTA}{sym.HLINE*3}[ \u001b[1mYour Tasks{sym.default()}{sym.MAGENTA} ]' \
            + "\u2500"*63 + sym.default()

        if len(tasks) == 0 and len(tasks_done) == 0:
            out += "\n   No tasks found. Use 'dl task -h' and add new tasks ;)"

        
        for i,t in enumerate(tasks):
            title = Output.align_text_left(t[1], 48)
            weekday = Output.align_text_left(Output.int_to_days[t[2]], 3).upper()
            time_left = Output.align_text_right(f'{Output.format_time(*t[8:11])}',11)
            time_left = Output.color_time(*t[8:11], time_left)
            mark = (' ', sym.WHITE, )
            if t[8] < 0:
                mark = (sym.MISSED, sym.RED)
            out += f'\n{sym.RED} [{mark[0]}]{mark[1]} {title} [{t[4]}] ' \
                + f'{weekday} {t[3]} {time_left}{sym.default()}'

        for i,t in enumerate(tasks_done):
            title = Output.align_text_left(t[1], 48)
            weekday = Output.align_text_left(Output.int_to_days[t[2]], 3).upper()
            time_left = Output.align_text_right(f'{Output.format_time(*t[8:11])}',11)
            out += f'\n{sym.GREEN} [{sym.DONE}] {title} {sym.default()}[{t[4]}] ' \
                + sym.striken(f'{weekday} {t[3]} {time_left}') + sym.default()
        out += sym.default()
        print(out, flush=True)
