
import requests
from requests.exceptions import ConnectionError
import os

def download_ol_dump_editions_latest(dump_url,dump_path):
    print(dump_path)
    max_download_resumes_count = 0
    with requests.Session() as s:
        try:
            with s.get(dump_url,stream=True,allow_redirects=True,timeout=300) as r:
                r.raise_for_status()
                with open(dump_path, 'w+b') as f:
                    last_file_size = None
                    for chunk in r.iter_content(chunk_size=1024*1024):
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
        except ConnectionError as to:
            print("Here is Suppose to Timeout")
            resume_download_ol_dump_editions_latest(dump_url=dump_url,dump_path=dump_path,max_d_r_c=max_download_resumes_count)

def resume_download_ol_dump_editions_latest(dump_url,dump_path,max_d_r_c):
    print("Im Resuming the Download")
    max_download_resumes = 30
    if max_d_r_c < max_download_resumes:
        max_d_r_c += 1
        print(f"Number of times i resumed: {max_d_r_c}" )
        with open(dump_path, 'ab') as f:
            position = f.tell()
            pos_header = {"Range": f"bytes={position}-"}
        
        with requests.Session() as s:
            try:
                with s.get(dump_url,headers=pos_header,stream=True,allow_redirects=True,timeout=300) as r:
                    r.raise_for_status()
                    with open(dump_path, 'ab') as f:
                        for chunk in r.iter_content(chunk_size=1024*1024):
                            f.write(chunk)
                            f.flush()
                            os.fsync(f.fileno())
            except ConnectionError as to:
                print("Here is Suppose to Timeout")
                resume_download_ol_dump_editions_latest(dump_url=dump_url,dump_path=dump_path,max_d_r_c=max_d_r_c)

dump_url = "https://openlibrary.org/data/ol_dump_editions_latest.txt.gz"
#dump_path =  "temp_file/ol_dump_editions_latest.txt.gz"
dump_path ="ol_dump_editions_latest.txt.gz"
download_ol_dump_editions_latest(dump_url=dump_url, dump_path=dump_path)
