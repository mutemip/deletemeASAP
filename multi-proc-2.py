import multiprocessing
import time

def greeting_with_sleep(string):
  print(string)
  time.sleep(2)
  print(str(string) + " says hello!")


def main_multiprocessing():
  s = time.perf_counter()
  processes = []
  greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
  # add your code here
  for g in range(len(greetings)):
    # create a process
    p = multiprocessing.Process(target=greeting_with_sleep, args=([g],))
    processes.append(p)
    if __name__ == '__main__':
      p.start()


  if __name__ == '__main__':
    for p in processes:
      p.join()

  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")




main_multiprocessing()