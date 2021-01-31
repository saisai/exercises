


import requests



class Transmy:

    def __init__(self):
        pass


    def isEnglish(self, s):
        # https://stackoverflow.com/questions/27084617/detect-strings-with-non-english-characters-in-python
        try:
            s.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True

