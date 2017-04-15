# -*- coding:utf-8 -*-
import sys
import shlex
import os

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
    ''' 
    Fork a child shell process
    If the current process is a child process, its pid is set to 0
    else the current process is a parent process and the value of pid
    is the process id of its child process.
    '''
    pid = os.fork()
    if pid == 0:
    # Child process
        # Replace the child shell process with the program called with exec
        os.execvp(cmd[0],cmd)
    elif pid > 0:
    # Parent process
        while True:
            # Wait response status from its child process (identifed with pid)
            wpid, status = os.waitpid(pid, 0)
            # Finish waiting if its child process exits normally
            # or is terminated by a signal
            if os.WIFEXITED(status) or os.WIFSIGNALED(status):
                break

    # Return status indicating to wait for next command in loop
    return shell_status_run

def main():
    loop() 

if __name__ == '__main__':
    main()
