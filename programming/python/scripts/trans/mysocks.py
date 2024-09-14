
import re

from bs4 import BeautifulSoup


class MySocks:

    RE_INT = re.compile(r'^[0-9]')
    
    def __init__(self, filename):
        self.read_file = self.readfile(filename)
        self.results = set()
        self.get_result()
    
    
    
    def readfile(self, filename):
        
        read_file = open(filename, 'r', encoding='utf-8').read()
        return read_file
        
        
    def get_result(self):
        soup = BeautifulSoup(self.read_file, 'html.parser')

        for data in soup.find_all('tr'):
            for td in data.find_all('td'):
                if td.find('font', attrs={'class': 'spy14'}) != None:
                    td_text = td.find('font', attrs={'class': 'spy14'}).get_text()
                    
                    if MySocks.RE_INT.match(td_text) != None:
                        if '100%' in td_text or '-' in td_text:
                            continue
                        self.results.add(td_text)        
        

    def __iter__(self):
        self.n = 0
        return self
        
    
    def __next__(self):        
        #n = 0
        lst_results = list(self.results)
        max_count = len(lst_results)
        try:        
            if self.n <= max_count:
                result = lst_results[self.n]
                self.n += 1
                return result
        except IndexError as e:
            raise StopIteration

        


if __name__ == '__main__':

    sock = Socks('socks.txt')
    print(list(sock))


