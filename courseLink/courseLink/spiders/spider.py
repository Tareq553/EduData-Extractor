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
    'https://www.reed.co.uk/courses/one-education/p1812',
    'https://www.reed.co.uk/courses/janets/p1778',
    'https://www.reed.co.uk/courses/studyhub/p2675',
    'https://www.reed.co.uk/courses/training-express-ltd/p2079',
    'https://www.reed.co.uk/courses/academy-for-health-fitness/p2261',
    'https://www.reed.co.uk/courses/nextgen-learning/p3221',
    'https://www.reed.co.uk/courses/skill-up/p2339',
    'https://www.reed.co.uk/courses/institute-of-beauty-and-makeup/p2509',
    'https://www.reed.co.uk/courses/the-animal-care/p2520',
    'https://www.reed.co.uk/courses/compliance-central/p2584',
    'https://www.reed.co.uk/courses/institute-of-mental-health/p2821',
    'https://www.reed.co.uk/courses/kingston-open-college/p2975',
    'https://www.reed.co.uk/courses/thames-college/p3085',
    'https://www.reed.co.uk/courses/imperial-academy/p3050',
    'https://www.reed.co.uk/courses/apex-learning/p2601',
    'https://www.reed.co.uk/courses/cambridge-open-academy/p3240',
    'https://www.reed.co.uk/courses/discover-training/p3276',
    'https://www.reed.co.uk/courses/learning-path-ltd/p3268',
    'https://www.reed.co.uk/courses/study-booth/p3293',
    'https://www.reed.co.uk/courses/nano-training/p3312',
    'https://www.reed.co.uk/courses/knowledge-gate/p3320'
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
            # id = int(all.css("h2.course-card-title>a::attr(href)").get().split("/")[3].replace("#", ""))
            # try:
            #     s = int(
            #         all.css(".students-icon ::text").get().replace(",", "").replace("enquiries", "").replace("students",
            #                                                                                                  "").strip())
            # except:
            #     s = 0
            yield {
                'courseLink': link
                # 'courseId': id,
                # 'unitSold': s
            }
