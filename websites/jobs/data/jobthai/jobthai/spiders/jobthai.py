
import scrapy
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker

from jobthai.items import JobthaiItem
from jobthai.models import JobThai, db_connect


class JobThaiSpider(scrapy.Spider):
    name = "jobthai"
    allowed_domain = ["jobthai.com"]
    start_urls = ("https://www.jobthai.com/jobsearch/computer-it/%s" % page for page in range(1, 100))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        engine = db_connect()
        Session = sessionmaker(bind=engine)
        try:
            with Session() as session:
                session.query(JobThai).delete()
                session.commit()
        except Exception as e:
            print("no table created yet")


    def parse(self, response):

        soup = BeautifulSoup(response.body, 'lxml')

        data = soup.find_all('div', attrs={'class': 'ant-row msklqa-8 crLDlD'})

        for obj in data:
            
            link = "https://www.jobthai.com" + obj.find('a').get('href')
            #print(obj.find('h2', attrs={'id': 'job-card-item-'}).get_text())
            tmp = obj.find_all('div', attrs={'class': 'ant-col ant-col-12'})
            tmp2 = tmp[0].find('span').get_text().strip()
            tmp3 = tmp2[:-1]
            
            title = obj.find('h2', attrs={'id': 'job-card-item-{}'.format(tmp3)}).get_text()
            time = tmp[1].find('span').get_text()
            data = JobthaiItem()
            data['title'] = title
            data['link'] = link 
            data['time'] = time
            yield data

            #print(obj)
            #print()
