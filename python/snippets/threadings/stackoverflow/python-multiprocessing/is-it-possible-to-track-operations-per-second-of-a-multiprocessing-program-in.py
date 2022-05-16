from multiprocessing import Pool
from time import time
import requests

def download_image(image):
    save_dir = "[PATH TO SAVE IMAGES]"
    image_url = image['url']
    image_name = image['name']

    image_data = requests.get(image_url).content
    with open(os.path.join(save_dir, f"{image_name}.jpg"), 'wb') as f:
        f.write(image_data)

if __name__ == "__main__":
#   Get in the habit of never calling anything that could create a child process
#such as creating a "Pool" or simply calling "multiprocessing.Process" without
#guarding execution by "if __name__ == '__main__':". This is necessary when using
#Windows, it is needed in MacOS with python 3.8 and above, and is highly encouraged
#everywhere else
    pool = Pool(8) #  <- child processes are created here which can't be allowed
                   #     to happen when this file is `import`ed (which is what
                   #     `if __name__ == "__main__":` protects against).
    completed = 0
    t = time()
    for result in pool.imap_unordered(download_image, images):
        #`result` is unused in this case, but could easily be put to some use
        completed += 1
        if time() >= t+60: #once a minute
            rate = completed / (time() - t)
            print(f'{rate} operations per second')
            t = time()
            completed = 0
    print("done")

    pool.close()
    pool.join()