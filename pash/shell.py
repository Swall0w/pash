# -*- coding:utf-8 -*-
import sys
import shlex

shell_status_run = True
shell_status_stop = False
def loop():
    status = shell_status_run
    while status == shell_status_run:
# Display a command prompt
        sys.stdout.write('> ')
        sys.stdout.flush()
# Read command input
        cmd = sys.stdin.readline()
# Tokenize the command input
        cmd_tokens = _tokenize(cmd)
        print(cmd_tokens)
# Execute the command and retrieve new status
        status = _execute(cmd_tokens)
def _tokenize(string):
    return shlex.split(string)
def _execute(cmd):
    pass
def main():
    loop() 

if __name__ == '__main__':
    main()
