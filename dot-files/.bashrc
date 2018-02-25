#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export TERM=xterm-256color        # for common 256 color terminals (e.g. gnome-terminal)
export TERM=screen-256color       # for a tmux -2 session (also for screen)
export TERM=rxvt-unicode-256color # for a colorful rxvt unicode session
eval `dircolors /home/andre/source/src/dircolors-solarized/dircolors.256dark`
alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

source /usr/share/doc/pkgfile/command-not-found.bash

PATH=$PATH:~/source/scripts

PATH=$PATH:/home/andre/.cask/bin

PATH=$PATH:$HOME/.cargo/bin

PATH=$PATH:$HOME/go/bin

PATH=$PATH:$HOME/source/Fuchsia/topaz/.jiri_root/bin
PATH=$PATH:$HOME/.gem/ruby/2.5.0/bin
# Add RVM to PATH for scripting. Make sure this is the last PATH variable change.
export PATH="$PATH:$HOME/.rvm/bin"
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"

# alias msfconsole="msfconsole --quiet -x \"db_connect ${USER}@msf\""
alias msfconsole="msfconsole -x \"db_connect ${USER}@msf\""

powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /usr/lib/python3.6/site-packages/powerline/bindings/bash/powerline.sh

