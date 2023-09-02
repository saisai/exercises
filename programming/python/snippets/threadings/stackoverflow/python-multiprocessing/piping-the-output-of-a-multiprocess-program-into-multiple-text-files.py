import subprocess
from multiprocessing import Pool
from pathlib import Path

'''
scripts = ('myfirstfile.py',
           'mysecondfile.py',
           'mythirdfile.py',
           'myfourthfile.py')
'''
scripts = ("hello.py", )
def run_process(script):
    log_file = Path(script).stem + '.log'
    with open(log_file, 'w') as log_handle:
        subprocess.run(['python', script], check=True, text=True, stdout=log_handle, stderr=subprocess.STDOUT)

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(run_process, scripts)
    
    # https://stackoverflow.com/questions/69475881/piping-the-output-of-a-multiprocess-program-into-multiple-text-files