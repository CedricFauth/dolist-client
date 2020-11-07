# dolist client

A lecture, event, and assignment manager.

![Screenshot 2020-11-07 at 16 38 14](https://user-images.githubusercontent.com/25117793/98445362-b172fe80-2117-11eb-8a59-952643a5c2f4.png)

## Run the program:

**You need Python 3 or higher in order to run the program.** \
Check out the [Installation Guide](/INSTALL.md).

## Commands:

### Show today's overview
This shows all events of today and all tasks.
```
dl
```
### Add a new event:
```
dl event TITLE -f daily|weekly|once [-d weekday|date] -t HH:MM-HH:MM
```
Examples:
```
dl event 'CS Lecture 1' -f w -d mon -t 13:37-14:42
dl event 'CS Lecture 2' -f o -d 2020-12-24 -t 12:34-13:57
dl event 'CS Lecture 3' -f d -t 00:00-01:05
```
### Add a new task:
```
dl task TITLE -f daily|weekly|once [-d weekday|date] -t HH:MM
```
Examples:
```
dl task 'Assignment 1' -f w -d mon -t 13:37
dl task 'Assignment 2' -f o -d 2020-12-24 -t 12:34
dl task 'Assignment 3' -f d -t 00:00
```
### List all events and tasks
This shows all events, tasks, and their corresponding IDs (You need the IDs in order to delete events/tasks or mark tasks as done).
```
dl ls
```
### Mark a task as done
ID: integer number of a task (see dl ls)
```
dl done ID
```
### Delete an event
```
dl rm -e ID
```
### Delete a task
```
dl rm -t ID
```
