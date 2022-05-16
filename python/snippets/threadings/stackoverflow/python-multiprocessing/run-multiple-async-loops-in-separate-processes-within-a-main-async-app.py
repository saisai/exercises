import asyncio
import time
# from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

# Refactored MyClass to break out MyTask

class MyTask:
    def __init__(self):
        self.multiplier = 2

    async def subtask(self, letter: str):
        await asyncio.sleep(1)
        return letter * self.multiplier
    
    async def task_gatherer(self, subtasks: list):
        return await asyncio.gather(*subtasks)
    
    def blocking_task(self, word: str):
        time.sleep(1)
        subtasks = [self.subtask(letter) for letter in word]
        result = asyncio.run(self.task_gatherer(subtasks))
        return result
    
class MyClass:
    def __init__(self):
        self.task = MyTask()
        self.event_loop: asyncio.AbstractEventLoop = None
        self.pool_executor = ProcessPoolExecutor(max_workers=8)
        # self.pool_executor = ThreadPoolExecutor(max_workers=8)
        self.words = ["one", "two", "three", "four", "five"]

    async def master_method(self):
        self.event_loop = asyncio.get_running_loop()
        master_tasks = [
            self.event_loop.run_in_executor(
                self.pool_executor,
                self.task.blocking_task,
                word,
            )
            for word in self.words
        ]
    
        results = await asyncio.gather(*master_tasks)
        print(results)

if __name__ == "__main__":
    my_class = MyClass()
    asyncio.run(my_class.master_method())