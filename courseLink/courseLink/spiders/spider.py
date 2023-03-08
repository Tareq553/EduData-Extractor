# Import required modules
import scrapy
import numpy as np
import requests
from bs4 import BeautifulSoup
from itertools import chain
from ..items import CourselinkItem

# These are the prodivers we would like to scrape
providerCoverPage = [
    # Our courses
    'https://www.reed.co.uk/courses/vision2learn/p131',
    'https://www.reed.co.uk/courses/janets/p1778'
]


# This function generates cover pages for each provider
def generateCoverPage(url):
    """url = provider directory link,
    return = cover pages"""

    coverPage = []
    r = requests.get(url)
    s = BeautifulSoup(r.text, "lxml")
    totalCourse = int(s.find("span", class_="h1").text.strip().replace(",", ""))
    totalPage = int(np.ceil(totalCourse / 100))
    for pg in range(1, totalPage + 1):
        coverPage.append(url + f"?pageno={pg}&sortby=MostPopular&pagesize=100")
    return coverPage


class CourseLinkScraper(scrapy.Spider):
    name = "courseLink"
    urls = list(map(generateCoverPage, providerCoverPage))
    urls = list(chain.from_iterable(urls))
    start_urls = urls

    def parse(self, response):
        items = CourselinkItem()
        for all in response.css("article.course-card"):
            link = all.css("h2.course-card-title>a::attr(href)").get()
            yield {
                'courseLink': link
            }
