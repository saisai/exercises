#!/usr/bin/env python
# coding=utf-8
import sys
import os
import time
from threading import Thread
from queue import Queue
import argparse
import binascii
import json
import re 

import glob
from pydub.utils import mediainfo
import subprocess
import datetime
import os
import shutil

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

moved_mp3 = 'moved_mp3'

if not os.path.isdir(moved_mp3):
    os.mkdir(moved_mp3)
    
    
threads = int(sys.argv[1])
print(threads)
images = 3

class Converter(Thread):
    """Downloader class - read queue and downloads each file in succession"""

    def __init__(self, queue):

        Thread.__init__(self, name=binascii.hexlify(os.urandom(16)))
        self.queue = queue
        

    def run(self):
        while True:
            # gets the url from the queue
            mp3file = self.queue.get()
            print(mp3file)
            # download the file
            print("* Thread {} - processing URL".format(self.name))
            self.download_file(mp3file)
            # send a signal to the queue that the job is done
            self.queue.task_done()


    def download_file(self, mp3file):
        """Download file"""
        if os.path.isfile(mp3file):
            
            t_start = time.time()
            t_elapsed = time.time() - t_start
            
            print("* Thread: {} Download {} in {} seconds.".format(self.name, mp3file, str(t_elapsed)))   

            format = mp3file.split('.')[0]
            print('counter' , format)
            info = mediainfo(mp3file)
            seconds = float(info['duration'])       
            result = seconds / images
            plus_one = result
            #command = "ffmpeg|-y|-r|1/{}|-start_number|1|-i|photo-%03d.jpg|-i|{}|-r|18|-pix_fmt|yuv420p|-c:a|aac|-s|320x240|{}.mp4".format(plus_one, mp3file , format)
            command = "ffmpeg|-f|image2|-y|-r|1/{}|-start_number|1|-i|photo-%03d.jpg|-i|{}|-r|18|-pix_fmt|yuv420p|-c:a|aac|-s|320x240|{}.mp4".format(plus_one, mp3file , format)
            print(command)
            completed = subprocess.run(command.split('|'))
            print('returncode:', completed)
            print(completed.returncode)
            if completed.returncode == 0:
                print('Moving file {} .....'.format(mp3file))
                shutil.move(mp3file, moved_mp3)
        else:
            print('No file found', mp3file)
        
            #else:
            #    print("* Thread: {} Bad URL: {}".format(self.name, url))


class ConvertManager():
    """Spawns downoader threads and manages URL downloads queue"""
    def __init__(self, convert_list, thread_count=4):
        self.thread_count = thread_count
        self.convert_list = convert_list
        

    def begin_convert(self):
        """Start the downloader threads, fill the queue with the URLs and

        then feed the threads URLs via the queue
        """

        queue = Queue()
        # create a thred pool and give them a queue
        for i in range(self.thread_count):
            t = Converter(queue)
            t.setDaemon(True)
            t.start()

        # load the queue from the download dict
        for mp3file in self.convert_list:
            queue.put(mp3file)

        # wait for the queue to finish
        queue.join()

        return

parser = argparse.ArgumentParser()
parser.usage = "pydownload.py -o <OutputDirectory> -i <JSONinputfile> -f <url1,url2,url3>"
parser.add_argument('-o', '--output')
parser.add_argument('-i', '--ifile')
parser.add_argument('-f', '--flist')

#def main(argv):
def main():
    
    mp3s = [mp3 for mp3  in sorted(glob.glob("*.mp3"))]
    convert_manager = ConvertManager(mp3s, threads)
    convert_manager.begin_convert()
    
   

if __name__ == "__main__":    
    #args = parser.parse_args()
    #main(args)
    main()
    #  python filedownload.py -o ./tmp -i test.json
