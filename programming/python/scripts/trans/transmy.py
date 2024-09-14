import queue
from collections import defaultdict

import requests


from mysocks import MySocks
from tran import trans

class str2(str):
    def __repr__(self):
        return ''.join(('"', super().__repr__()[1:-1], '"'))
        

class Transmy:

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) \
               AppleWebKit/537.36 (KHTML, like Gecko) \
               Chrome/83.0.4103.97 Safari/537.36"}

    def __init__(self):
        self.socks = list(MySocks("socks.txt"))
        self.trans = trans


    def is_english(self, s):
        # check if the sentence is english or not
        # https://stackoverflow.com/questions/27084617/detect-strings-with-non-english-characters-in-python
        try:
            s.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True
    
    
    def get_random(self):
        import random
        return random.sample(self.socks, 1)
        
    def translate_json_retry(self):
        import time
        from json import loads
        from requests import get   
        
        
        try:
            import http.client as http_client
        except ImportError:
            # Python 2
            import httplib as http_client
        http_client.HTTPConnection.debuglevel = 1
        
        import logging
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True
        
        
        total_dict = defaultdict(dict)
        
        
        results = [f.strip("\n") for f in open("new_string.txt", "r", encoding="utf-8")]
        with open("translate_dict.txt", "w", encoding="utf-8") as f:
            self.same_ip = ""
            for r in results:                        
                
                while True:
                
                    try:            
                                                
                        if self.same_ip == "":
                            self.ips = self.get_random()[0]
                        else:
                            self.ips =  self.same_ip
                        print("ips", self.ips)
                        print("same_ip", self.same_ip)
                        #if ips == "0.0.0.0":                        
                        #    request_result = get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=en&tl=my&q={}".format(r))
                        #else:
                        
                        proxies = { 
                                'http': 'socks5://{}'.format(self.ips), 
                                'https': 'socks5://{}'.format(self.ips)
                                }


                        request_result = get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=en&tl=my&q={}".format(r),
                                           headers=Transmy.headers, proxies=proxies, timeout=5)
                        
                        total_dict[self.ips] = total_dict.get(self.ips, 0) + 1
                        translated_text = loads(request_result.text)[0][0][0]
                        f.write("{}:{},".format(r, translated_text))
                        f.write("\n")
                        f.flush()
                        self.same_ip = self.ips
                        print(r)
                        #time.sleep(1)
                    except Exception as inst:
                        print(inst)
                        self.same_ip = ""
                        continue
                    break
        
        print("Ips hit :", total_dict)
        
        
    def check_msgstr_eng(self):
    
        results = [f.strip("\n") for f in open("my.po", encoding="utf-8")]

        q = queue.Queue()

        for r in results:
            q.put(r)
            

        results = set()
        
        while not q.empty():
            item = q.get()        
            if "msgstr" in item:
                new_str = item.replace("msgstr", "").replace('"', '').strip()
                t = self.is_english(new_str)
                if t:
                    results.add(item.replace("msgstr", "").strip())
                
            q.task_done()
            
                
        for t in results:
            print(t)
            
    def check_msgstr(self, msgstr):

        for key, val in self.trans.items():
            compare = 'msgstr "{tran}"'.format(tran=key)
            if compare == msgstr:
                print(key, msgstr)
                new_msgstr = 'msgstr "{new_tran}"'.format(new_tran=val)
                return new_msgstr, True
        
        return msgstr, False



    def main(self):
        results = [f.strip("\n") for f in open("my.po", encoding="utf-8")]

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
                
        
        print()
        print("Total matched: ", total)     


    def check_jsstr(self, jsstr):

        for key, val in trans.items():
        
            if 'catalog' in jsstr:
                    try:
                        item = jsstr.split(' = ')[1].replace(';','')
                        compare_key =  '"{}"'.format(key)                    
                        
                        if "'{}'".format(key)  == item or '"{}"'.format(key)  == item  :
                            new_msgstr = "{0} = '{1}';".format(jsstr.split(' = ')[0], val)
                            return new_msgstr, True
                    except IndexError as e:
                        pass
                        
        return jsstr, False    
    
              
    
    def main_js(self):
        results = [f.strip("\n") for f in open("en.js", encoding="utf-8")]

        q = queue.Queue()

        for r in results:
            q.put(r)
            

        total = 0
        with open("test.js", "w", encoding="utf-8") as f:
            while not q.empty():
                item = q.get()
                
                new_item, matched_msgstr = self.check_jsstr(item)
                
                if matched_msgstr:
                    total += 1
                
                f.write(new_item)
                f.write("\n")
                
        
        print()
        print("Total matched: ", total)          
        
        
    def get_raw_string(self):
        from ordered_set import OrderedSet
        
        results = [f.strip("\n") for f in open(r"d:\some\path\my.po", encoding="utf-8")]        
                
        str_unique = OrderedSet()

        for r in results:
            if "msgstr" in r:
                try:
                    
                    new_str = r.replace("msgstr", '')
                    t = self.is_english(new_str)
                    if t:                        
                        str_unique.add(new_str.strip())
                except Exception as e :
                    pass
                    
        
        for t in str_unique:
            print(t)
        
if __name__ == '__main__':
    #t = Transmy(trans)
    t = Transmy()
    t.translate_json_retry()
    #t.check_msgstr_eng()
    #t.main()
    #t.get_raw_string()
    #t.main_js()
    
    """
    https://translate.yandex.com/?lang=es-my&text=Espa%C3%B1ol
    https://burmese.english-dictionary.help/?q=area
    https://translate.google.com/?sl=en&tl=my&text=Espa%C3%B1ol&op=translate
    https://www.pinterest.com/pin/747456869375409360/
    https://lingvanex.com/english-to-burmese/
    """


