#!/usr/bin/python3
import os
import time
import random as rnd
import sys


# author: karakurik

def main():
    arg = int(sys.argv[1])
    print(f'Сhild[{os.getpid()}]: I am started. My PID {os.getpid()}. Parent PID {os.getppid()}.')
    time.sleep(arg)
    print(f'Child[{os.getpid()}]: I am ended. PID {os.getpid()}. Parent PID {os.getppid()}.')

    exit_code = rnd.randint(0, 1)
    os._exit(exit_code)


main()
