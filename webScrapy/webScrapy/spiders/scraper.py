# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from webScrapy.items import WebscrapyItem
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from webScrapy import settings
from webScrapy.pipelines import ScrapySpiderPipeline
from sqlalchemy.orm import sessionmaker
from webScrapy.spiders.models import QuoteDB, db_connect, create_table

class ScraperSpider(CrawlSpider):
    name = 'scraper'
    allowed_domains = ['lds.org']
    search_url = 'https://www.lds.org/general-conference/conferences?lang=eng'
    start_urls = ['https://www.lds.org/general-conference/conferences?lang=eng']

    def parse(self, response):
        
        url = "https://www.lds.org/general-conference/conferences?lang=eng"
        item = []
        browser = webdriver.Firefox()
        browser.get(url)
        time.sleep(5)
        rests = browser.find_elements_by_xpath("//div[contains(@class, 'year-line')]")
        
        i=0
        #while i<len(rests):
        while i<2:
            browser.find_elements_by_xpath("//div[contains(@class, 'year-line')]/a")[i].click()
            time.sleep(5)
            j=0
            arts = browser.find_elements_by_xpath("//div[contains(@class, 'lumen-tile__title')]/div")
            #while j<len(arts):
            while j<4:
                browser.find_elements_by_xpath("//div[contains(@class, 'lumen-tile__title')]/div")[j].click()
                time.sleep(5)
                try:
                    year = browser.find_element_by_xpath("//div[contains(@class, 'sticky-banner')]/a").text
                    try:
                        headline = browser.find_element_by_xpath("//p[contains(@class, 'kicker')]").text
                    except:
                        headline = "N/A"
                    words = browser.find_element_by_xpath("//div[contains(@class, 'body-block')]").text
                
                    try:
                        speaker = browser.find_element_by_xpath("//div[contains(@class, 'article-author')]/a").text
                    except:
                        speaker = browser.find_element_by_xpath("//div[contains(@class, 'article-author')]").text
                        
                    tittle = browser.find_element_by_xpath("//h1[contains(@class, 'title')]").text
                    page_url = browser.current_url
                    
                    print(page_url)
                    print(year)
                    print(headline)
                    print(speaker)
                    print(tittle)       
                    
                    
                    #return item
                except:
                    pass
                
                print("Creating Item")
                items = WebscrapyItem()
                items["year"] = year
                items["speaker"] = speaker
                items["topic"] = tittle
                items["url"] = page_url
                items["headline"] = headline
                items["words"] = words
                print("This is the item")
                print(items["year"])
                print("See the item up")
                browser.back()
                j=j+1
                item.append(items)  
               
            i=i+1
            time.sleep(5)
            browser.back()
        time.sleep(5)
        print("Beginin of item list")
        print(item)
        print("End of item list")
        browser.close()
        print("Finishing firefox")
        return item
        


