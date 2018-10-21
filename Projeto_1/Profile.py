'''
Created on 21 de out de 2018

@author: danilo
'''
import cProfile, pstats, io
from memory_profiler import memory_usage

def profile(func):
    '''
    Decorador do profile
    '''

    def inner(*args, **kwargs):
        from pstats import SortKey
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = SortKey.CUMULATIVE
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

def memProfile(func):

    def inner(*args, **kwargs):
        mem_usage = memory_usage(retval = func(*args, **kwargs), interval=.1, timeout=None)
        print(mem_usage)

    return inner

