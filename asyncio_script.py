##The Asyncio Module
# Now we will cover another concurrent programming model: the asyncio module.

# The asyncio module uses async/await syntax. async and await are two keywords that allow you to build and execute asynchronous code in your programs.

# The async keyword declares a function as a coroutine. Coroutines are functions that may return normally with a value or may suspend themselves internally and return a continuation. This is a fancy way of saying they allow tasks to be paused and resumed to mimic multitasking. This is conceptually very similar to what we saw with threads! Coroutines are at the heart of asynchronous programs in Python.

# The await keyword suspends execution of the current task until whatever is being “await”ed on is completed. For example, if we have an “await function task2” within a coroutine “task1” this tells Python “Suspend task1 until task2 is completed.”

import time
import asyncio

async def greeting_with_sleep_async(string):
  print(string)
  await asyncio.sleep(2)
  print(string + " says hello!")


async def main_async():
  s = time.perf_counter()
  greetings = [greeting_with_sleep_async('Codecademy'), greeting_with_sleep_async('Chelsea'), greeting_with_sleep_async('Hisham'), greeting_with_sleep_async('Ashley')]
  # your code goes here
  await asyncio.gather(*greetings)


  elapsed = time.perf_counter() - s
  print("Asyncio Elapsed Time: " + str(elapsed) + " seconds")

loop = asyncio.get_event_loop()
loop.run_until_complete(main_async())

# OR
# asyncio.run(main_async())


