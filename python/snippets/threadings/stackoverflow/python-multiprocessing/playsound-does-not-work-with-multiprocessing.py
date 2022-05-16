from multiprocessing import Process
from playsound import playsound

    
def sound():
    playsound('sqlalchemy-2.0.mp3')

if __name__ == "__main__":
    p = Process(target=sound)
    p.start()
    
    # https://stackoverflow.com/questions/70468929/playsound-does-not-work-with-multiprocessing