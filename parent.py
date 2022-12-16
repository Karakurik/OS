#!/usr/bin/python3
import os
import random as rnd
import time

# author: karakurik

sleep_time = 10


def is_root(pid: int):
    return pid != 0


def is_child_failed(exit_code: int):
    return exit_code == 0


def fork():
    child_pid = os.fork()
    if is_root(child_pid):
        print(f'Parent[{os.getpid()}]: I ran children process with PID {child_pid}.')
        return child_pid
    else:
        random_number = rnd.randint(5, 10)
        os.execl("child.py", str(random_number))


def main():
    fork_count = int(input())
    children = []
    for i in range(fork_count):
        children.append(fork())
    while children:
        child_pid, exit_code = os.wait()
        if is_root(child_pid):
            print(f'Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit {exit_code}.')
            children.remove(child_pid)
            if is_child_failed(exit_code):
                children.append(fork())
        # else:
        # time.sleep(sleep_time)


main()
