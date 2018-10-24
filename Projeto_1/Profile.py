'''
Created on 21 de out de 2018

@author: danilo
'''
import cProfile, pstats, io

def time_Profile(func):
    '''
    Decorador do profile de tempo do CProfile
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

