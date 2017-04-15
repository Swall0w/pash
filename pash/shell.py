# -*- coding:utf-8 -*-
import sys

shell_status_run = True
shell_status_stop = False
def loop():
    status = shell_status_run
    while status == shell_status_run:
        sys.stdout.write('> ')
        sys.stdout.flush()

        cmd = sys.stdin.readline()
def main():
    loop() 

if __name__ == '__main__':
    main()
