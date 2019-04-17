# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from webScrapy.spiders.models import QuoteDB, db_connect, create_table

class ScrapySpiderPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        print("This is the info that we recieve")
        print(item)
        print("That was the info sended")
    
        session = self.Session()
        quotedb = QuoteDB()
        quotedb.year = item["year"]
        quotedb.speaker = item["speaker"]
        quotedb.topic = item["topic"]
        quotedb.url = item["url"]
        quotedb.headline = item["headline"]
        quotedb.words = item["words"]

        try:
            session.add(quotedb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item