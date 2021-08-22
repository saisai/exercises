import json
import queue
from bs4 import BeautifulSoup

    
def get_download_wget(num):
    q = queue.Queue()
    data = open('txt.txt', encoding='utf-8').read()
    soup = BeautifulSoup(data, 'html.parser')
    fblink = '\nsource from: http://www.dhammadownload.com/DhammaByuharDawKhinHlaTin-Video-others.htm'
       
    
    for d in soup.find_all('a'):
        
        a_link = d.get('href')
        title = d.get_text()
        q.put({'link': a_link, 'title': title, 'desc': title + fblink})
    
    t = []
    with open("youtube_sample.sh", "w", encoding='utf-8') as outfile:
        while not q.empty():
            t = q.get()
            t.update({'num': '{:04d}'.format(num)})            
            outfile.write('wget -c -O {:04d}.mp4 "{}"'.format(num,t.get('link')))
            outfile.write('\n')
            num += 1    

def get_html_page(num):
    q = queue.Queue()
    data = open('txt.txt', encoding='utf-8').read()
    soup = BeautifulSoup(data, 'html.parser')
    fblink = '\nsource from: http://www.dhammadownload.com/DhammaByuharDawKhinHlaTin-Video-others.htm'
    '''
    desc = ""
    desc += '\nဓမ္မဗျူဟာ \n'
    desc += 'ဒေါ်ခင်လှတင် \n'
    desc += 'မဟာ သဒ္ဓမ္ဓဇောတိကဓဇ \n'
    desc += 'ဓမ္မဗျူဟာ သာသနမာမကအဖွဲ့  \n'
    desc += 'လူပုဂ္ဂိုလ်များဆိုင်ရာ ဓမ္မစာပေသင်တန်းကျောင်း \n'
    desc += 'အမှတ်(၆)၊ ကြားတောရလမ်း၊ ဗဟန်းမြို့နယ်၊ ရန်ကုန်။ \n'
    desc += 'ဖုန်း၊ (၉၅) ၀၁-၃၈၀၈၈၀\n'
    desc += 'သင်ကြားပို့ချသော တရားတော်များ။\n'
    '''
    
    desc = """
ဓမ္မဗျူဟာ
ဒေါ်ခင်လှတင် 
မဟာ သဒ္ဓမ္ဓဇောတိကဓဇ 
ဓမ္မဗျူဟာ သာသနမာမကအဖွဲ့ 
လူပုဂ္ဂိုလ်များဆိုင်ရာ ဓမ္မစာပေသင်တန်းကျောင်း 
အမှတ်(၆)၊ ကြားတောရလမ်း၊ ဗဟန်းမြို့နယ်၊ ရန်ကုန်။ 
ဖုန်း၊ (၉၅) ၀၁-၃၈၀၈၈၀ 
သင်ကြားပို့ချသော တရားတော်များ။\n"""
    
    for d in soup.find_all('a'):        
        a_link = d.get('href')
        title = d.get_text().replace('\t', '')
        link = 'link: ' + a_link
        q.put({'link': a_link, 'title': title, 'desc': title + desc + link + fblink})
              
    
    t = []    
    with open('test.html', 'w', encoding='utf-8') as outfile:

        while not q.empty():
            t = q.get()
            tbl_html = ''
            tbl_html += '<tr><td>{num:03d}.</td><td><a onClick=copyTitle(this) data-clipboard-text="{num:03d} - {title}">{num:03d} - {title}</a></td><td><a onClick=copyDesc(this) data-clipboard-text="{desc}">{desc}</a></td><td><button onClick="$(this).closest(\'tr\').remove();" id=\"id_{num}\" type=\"button\" class="btn btn-danger">Delete</button></td></tr>'.format(
                        num=num, title=t.get('title'), desc=t.get('desc'))
            outfile.write(tbl_html)
            outfile.write('\n')
            num += 1            

get_download_wget(1)
get_html_page(1)
