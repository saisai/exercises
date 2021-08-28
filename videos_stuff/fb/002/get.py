import json
import queue
from bs4 import BeautifulSoup

def get_download_youtube(num):
    q = queue.LifoQueue()
    data = open('txt.txt', encoding='utf-8').read()
    soup = BeautifulSoup(data, 'html.parser')
    fblink = '\nsource from: https://www.facebook.com/watch/0.SayarMoe/'
    for d in soup.find_all('div', attrs={'class': 'rq0escxv rj1gh0hx buofh1pr ni8dbmo4 stjgntxs l9j0dhe7'}):
        link = 'https://www.facebook.com'
        a_link = d.find('div', attrs={'class': 'bi6gxh9e'}).find('a').get('href')
        title = d.find('div', attrs={'class': 'i1fnvgqd btwxx1t3 j83agx80 bp9cbjyn'}).find('a').get_text().strip()
        q.put({'link': link + a_link, 'title': title, 'desc': title + fblink})
    
    t = []
    with open("youtube_sample.sh", "w", encoding='utf-8') as outfile:
        while not q.empty():
            t = q.get()
            t.update({'num': '{:04d}'.format(num)})            
            outfile.write('youtube-dl -v --output {:04d}.mp4 {}'.format(num,t.get('link')))
            outfile.write('\n')
            num += 1


def get_html_page(num):
    q = queue.LifoQueue()
    data = open('txt.txt', encoding='utf-8').read()
    soup = BeautifulSoup(data, 'html.parser')
    fblink = '\nsource from: https://www.facebook.com/ရွှေသုန်ရဲ့-ရွှေစာဝါ-103582395352744/'
    for d in soup.find_all('div', attrs={'class': 'rq0escxv rj1gh0hx buofh1pr ni8dbmo4 stjgntxs l9j0dhe7'}):
        link = 'https://www.facebook.com'
        a_link = d.find('div', attrs={'class': 'bi6gxh9e'}).find('a').get('href')
        fb_link = link + a_link
        fb_link_2 = '\nfb link: {fblink}'.format(fblink=fb_link)
        title = d.find('div', attrs={'class': 'i1fnvgqd btwxx1t3 j83agx80 bp9cbjyn'}).find('a').get_text().strip()
        if title.count('\n') > 1:
            title = title.replace('\n', '')
            q.put({'link': fb_link, 'title': title, 'desc': "\n".join(title.split("\n")) + fb_link_2 + fblink })
        else:
            q.put({'link': fb_link, 'title': title, 'desc': "\n".join(title.split("\n")) + fb_link_2 + fblink })        
    
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
            
if __name__ == '__main__':
    get_download_youtube(1)
    get_html_page(1)
