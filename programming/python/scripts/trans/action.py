
import os
import shutil
from shutil import copyfile
import os.path
import queue
import time


from transmy import Transmy
from tran import trans



class Action(Transmy):

    #def __init__(self, trans):
        #super().__init__(trans)
        
        
    def read_po(self):    
    
        my_po = [f.strip() for f in open('my_po.txt', 'r', encoding='utf-8')]
        en_po = [f.strip() for f in open('en_po.txt', 'r', encoding='utf-8')]        
            
        for en, my in zip(en_po, my_po):
            print(en, my)        
                        
            if os.path.isfile(my+'.bak'):
                os.remove(my+'.bak')
            if os.path.isfile(my):
                os.rename(my, my +'.bak')
            copyfile(en, my)
            
            results = [f.strip("\n") for f in open(my, encoding="utf-8")]

            q = queue.Queue()

            for r in results:
                q.put(r)
                
            
            total = 0
            with open("test.po", "w", encoding="utf-8") as f:
                while not q.empty():
                    item = q.get()
                    
                    new_item, matched_msgstr = self.check_msgstr(item)
                    
                    if matched_msgstr:
                        total += 1
                    
                    f.write(new_item)
                    f.write("\n")
                    
            shutil.move("test.po", my)
            
            print()
            print("Total matched: ", total)
            
            
    def read_js(self):
        
        my_path = r'd:\your\path\file\\'
        
        my_en_js = my_path + 'en.js'
        my_my_js = my_path + 'my.js'
        results = [f.strip("\n") for f in open(my_en_js, encoding="utf-8")]

        q = queue.Queue()

        for r in results:
            q.put(r)            

        total = 0
        
        with open("my_test.js", "w", encoding="utf-8") as f:
            while not q.empty():
                item = q.get()
                
                new_item, matched_msgstr = self.check_jsstr(item)
                
                if matched_msgstr:
                    total += 1
                
                f.write(new_item)
                f.write("\n")
                
        shutil.move('my_test.js', my_my_js)
        print()
        print("Total matched: ", total)        
    
    
    
if __name__ == '__main__':
    t = Action()
    #t.read_po()
    t.read_js()

