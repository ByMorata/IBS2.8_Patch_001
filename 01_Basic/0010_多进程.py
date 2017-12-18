from multiprocessing import Process
import os


def run_proc(name):
    print("Run child process %s(%s)..." % (name, os.getpid()))


if __name__ == '__main__':
    print("Parent process %s." % os.getpid())
    pid_00 = Process(target=run_proc,args=('test',))
    pid_00.start()
    pid_00.join()
    print("Child process end.")
