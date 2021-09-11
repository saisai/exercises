import json
import queue
from bs4 import BeautifulSoup

def get_html_page():

    desc = """
၁၃၈၃-ခုနှစ်၊ ပရိယတ္တိပညာသင်နှစ်၊
နံ့သာမြိုင်ဗိုလ်ကျောင်း၊ သာမဏေကျော်ဒုတိယဆင့်,တတိယဆင့်
ပထမလတ်တန်း,ပထမကြီးတန်းတပည့်များအား 
ညစဉ် ပို့ချအပ်သော နံ့သာမြိုင်သမာသ်စာဝါ အသံဖိုင်(၁-မှ၃၆)
✅ကစ္စည်းကျမ်းရင်း/ရူပသိဒ္ဓိ/နံ့သာမြိုင်သမာသ်,
✅တဒ္ဓိတ်ပို့ချစဉ်စာအုပ်များဖြင့် ပြည့်စုံစွာ ပို့ချထားပါသည်။
source from: https://www.facebook.com/bokyaung/    
    """
    
    with open('test.html', 'w', encoding='utf-8') as outfile:        
        for num in range(1, 37):
            title = 'နံ့သာမြိုင်သမာသ်စာဝါ ({})'.format(num)
            tbl_html = ''
            tbl_html += '<tr><td>{num:03d}.</td><td><a onClick=copyTitle(this) data-clipboard-text="{title}">{title}</a></td><td><a onClick=copyDesc(this) data-clipboard-text="{desc}">{desc}</a></td><td><button onClick="$(this).closest(\'tr\').remove();" id=\"id_{num}\" type=\"button\" class="btn btn-danger">Delete</button></td></tr>'.format(
                        num=num, title=title, desc=desc)
            outfile.write(tbl_html)
            outfile.write('\n')
            num += 1
            
if __name__ == '__main__':
    
    get_html_page()
