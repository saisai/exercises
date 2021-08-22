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
    with open("youtube_sample.txt", "w", encoding='utf-8') as outfile:
        while not q.empty():
            t = q.get()
            t.update({'num': '{:04d}'.format(num)})            
            outfile.write('wget -c -O {:04d}.mp4 {}'.format(num,t.get('link')))
            outfile.write('\n')
            num += 1    
            
def get_download_data(num):
    q = queue.Queue()
    data = open('txt.txt', encoding='utf-8').read()
    soup = BeautifulSoup(data, 'html.parser')
    fblink = '\nsource from: http://www.dhammadownload.com/DhammaByuharDawKhinHlaTin-Video-others.htm'
    
    desc = """
            ဓမ္မဗျူဟာ <br />
            ဒေါ်ခင်လှတင် <br />
            မဟာ သဒ္ဓမ္ဓဇောတိကဓဇ <br />
            ဓမ္မဗျူဟာ သာသနမာမကအဖွဲ့ <br />
            လူပုဂ္ဂိုလ်များဆိုင်ရာ ဓမ္မစာပေသင်တန်းကျောင်း  <br />
            အမှတ်(၆)၊ ကြားတောရလမ်း၊ ဗဟန်းမြို့နယ်၊ ရန်ကုန် <br />
            ဖုန်း။ (၉၅) ၀၁-၃၈၀၈၈၀ <br />
            သင်ကြားပို့ချသော တရားတော်များ
           """
    
    for d in soup.find_all('a'):
        
        a_link = d.get('href')
        title = d.get_text()
        q.put({'link': a_link, 'title': title, 'desc': title + desc + fblink})

    t = []
    with open("sample.txt", "w", encoding='utf-8') as outfile:
        while not q.empty():
            t = q.get()
            t.update({'num': '{:04d}'.format(num)})
            outfile.write(str(t))
            outfile.write('\n')            
            num += 1 

def get_html_page(num):
    q = queue.Queue()
    data = open('txt.txt', encoding='utf-8').read()
    soup = BeautifulSoup(data, 'html.parser')
    fblink = '<br />source from: http://www.dhammadownload.com/DhammaByuharDawKhinHlaTin-Video-others.htm'
    
    desc = """
            <br />
            ဓမ္မဗျူဟာ <br />
            ဒေါ်ခင်လှတင် <br />
            မဟာ သဒ္ဓမ္ဓဇောတိကဓဇ <br />
            ဓမ္မဗျူဟာ သာသနမာမကအဖွဲ့ <br />
            လူပုဂ္ဂိုလ်များဆိုင်ရာ ဓမ္မစာပေသင်တန်းကျောင်း  <br />
            အမှတ်(၆)၊ ကြားတောရလမ်း၊ ဗဟန်းမြို့နယ်၊ ရန်ကုန်။ <br />
            ဖုန်း၊ (၉၅) ၀၁-၃၈၀၈၈၀ <br />
            သင်ကြားပို့ချသော တရားတော်များ။
           """
    for d in soup.find_all('a'):        
        a_link = d.get('href')
        title = d.get_text()
        link = '<br />link: ' + a_link
        q.put({'link': a_link, 'title': title, 'desc': title + desc + link + fblink})
              
    
    t = []    
    with open('test.html', 'w', encoding='utf-8') as outfile:

        while not q.empty():
            t = q.get()
            tbl_html = ''
            tbl_html += '<tr><td>{num:03d}.</td><td>{num:03d} - {title}</td><td>{desc}</td><td><button onClick="$(this).closest(\'tr\').remove();" id=\"id_{num}\" type=\"button\" class="btn btn-danger">Delete</button></td></tr>'.format(
                        num=num, title=t.get('title'), desc=t.get('desc'))
            outfile.write(tbl_html)
            outfile.write('\n')
            num += 1            

get_download_wget(1)
get_download_data(1)
get_html_page(1)
