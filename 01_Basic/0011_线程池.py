
from multiprocessing import pool,Process
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    time.sleep(random.random()*3)
    end = time.time()