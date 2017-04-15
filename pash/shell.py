# -*- coding:utf-8 -*-
import sys

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
# Execute the command and retrieve new status
        status = _execute(cmd_tokens)
def _tokenize(cmd):
    pass
def _execute(cmd):
def main():
    loop() 

if __name__ == '__main__':
    main()
