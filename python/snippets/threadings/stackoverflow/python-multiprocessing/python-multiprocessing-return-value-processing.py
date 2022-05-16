def do_processVal():
   getParamInit()
   do_evaluation()
   currbestVal = bestGlobalVal
   return [currbestVal, os.getpid()]

from multiprocessing import Pool
import concurrent.futures
from os import getpid
import time
import os

start = time.perf_counter()

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(do_processVal) for _ in range(5)]

best_value = -1
values_list = []
for f in concurrent.futures.as_completed(results):
    values = f.result()
    values_list.append(values)
    if best_value == -1 or values[0] < best_value:
        best_value = values[0]

for i in values_list:
    print(f'Current best value: {i[0]} for process {i[1]}')

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
print(f'Final best = {best_value}')

# https://stackoverflow.com/questions/69492620/python-multiprocessing-return-value-processing