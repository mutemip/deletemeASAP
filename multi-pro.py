#           Multiprocessing Library
#       -------------------------------
# Allows the user to leverage multiple processors on a given machine simultaneously. This is because instead of threads or asynchronous tasks, multiprocessing is powered by subprocesses.

# to create a process:

''''
import multiprocessing
p = multiprocessing.Process(target=target_function, args=(arg,))
'''

# to start a process

'''
p.start()
'''

# Example 1
import time
import multiprocessing

def greeting_with_sleep(string):
  s = time.perf_counter()
  print(string)
  time.sleep(2)
  print(string + " says hello!")
  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")

#creating the process - takes in target and a list of args
p = multiprocessing.Process(target=greeting_with_sleep, args=('Mutemi',))

# NB: 
# On Windows the subprocesses will import (i.e. execute) the main module at start. You need to insert an if __name__ == '__main__': guard in the main module to avoid creating subprocesses recursively.

# see docs: https://docs.python.org/2/library/multiprocessing.html

if __name__ == '__main__':
  # starting a process
  p.start()
  