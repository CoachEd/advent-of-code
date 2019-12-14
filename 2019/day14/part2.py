import sys
import time
import math
from copy import copy, deepcopy

import cProfile, pstats
from io import StringIO
pr = cProfile.Profile()  # create a profile object
pr.enable()  # start profiling
start_secs = time.time()







pr.disable()  # end profiling

# print out some stats.
s = StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
