#!/bin/sh

GRE="\033[32m"
RES="\033[0m"
MAG="\033[95m"
RED="\033[31m"
YEL="\033[33m"
BRED="\033[31;1m"

name=$SHELL

if [ $name = "/bin/bash" ]; then
	name=".bashrc"
elif [ $name = "/bin/zsh" ]; then
	name=".zshrc"
elif [ $name = "o" ]; then
	printf "$YEL[INSTALL]$RES Current shell is not supported...\n"
	printf "Please name your shell's cnonfig file (has to be located in $HOME)?" 
	read name
else
	echo "$RED[Error]$RESET Unknown argument: $name" 
	exit 1
fi

# make folder
mkdir $HOME/.dolist
# copy files
cp -R src/ $HOME/.dolist/bin
# make alias
echo "alias dl=\"python3 $HOME/.dolist/bin/dolist.py\"" >> $HOME/$name

echo "$GRE[DONE]$RES Installation successful."
echo "$GRE[DONE]$RES Please run '${MAG}source $HOME/$name$RES' to finish the installation or ${BRED}close and reopen your terminal.$RES"

exit 0
