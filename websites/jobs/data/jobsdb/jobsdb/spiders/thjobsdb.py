
import scrapy
from bs4 import BeautifulSoup

from sqlalchemy.orm import sessionmaker

from jobsdb.items import JobsdbItem
from jobsdb.models import Jobsdb, db_connect

class ThjobsdbSpider(scrapy.Spider):
    name = "thjobsdb"
    allowed_domains = ["th.jobsdb.com"]
    start_urls = ("https://th.jobsdb.com/th/search-jobs/django/%s" % page for page in range(1, 3) )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        engine = db_connect()
        Session = sessionmaker(bind=engine)
        try:
            with Session() as session:
                session.query(Jobsdb).delete()
                session.commit()
        except Exception as e:
            print("no table created yet")

    def parse(self, response):        
    
        if 'th.jobsdb.com' in response.url:
            soup = BeautifulSoup(response.body, 'lxml')
            
            data = soup.find('div', attrs={'class': 'z1s6m00', 'data-automation': 'jobListing'})
            for obj in data.find_all('article'):
                link = obj.find('a').get('href')
                #print(obj.find('a').find('span'))
                title = obj.find('a').find('span').get_text()
                time = obj.find('time').find('span').get_text()                
                jobsdb = JobsdbItem()
                jobsdb['title'] = title
                jobsdb['link'] =  "https://th.jobsdb.com" + link 
                jobsdb['time'] = time 
                yield jobsdb

