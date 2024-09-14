# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker
from jobsdb.models import Jobsdb, db_connect, create_jobsdb_table


class JobsdbPipeline:

    def __init__(self):
        self.links_seen = set()
        engine = db_connect()
        create_jobsdb_table(engine)
        self.Session = sessionmaker(bind=engine)
    
    def process_item(self, item, spider):
        if len(item['title']) <= 0: # check if length of item is 0, pass it (not inserting blank to database) add strip title from spider
            pass
        else:
            if item['link'] in self.links_seen:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.links_seen.add(item['link'])
                session = self.Session()
                jobsdb = Jobsdb(**item)
                session.add(jobsdb)
                session.commit()
                return item

    #def process_item(self, item, spider):
    #    return item
