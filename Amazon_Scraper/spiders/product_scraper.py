import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from lxml import etree

import json

class ProductScraper(scrapy.Spider):
    """3
    Make use of start_request()
    """
    name = 'productsw'
    start_url = 'https://www.amazon.com'
    def start_requests(self):
        urls = ['https://Amazon.com']


def get_urls():
    driver = webdriver.Chrome()   #open a new browser window and do the navigation
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("lang=en_US")
    options.add_argument('--log-level=1')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    desired_capabilities = options.to_capabilities()
    amazon_driver = webdriver.Chrome(desired_capabilities=desired_capabilities)



    #set implicit wait
