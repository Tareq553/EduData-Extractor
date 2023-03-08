
# Scraping Project-3

## Motivation of this project
Aspiring data analysts need to have a strong understanding of how to collect and clean data in order to perform meaningful analysis. Web scraping is an essential skill for any data analyst, as it allows for the collection of large amounts of data from websites that can be used for further analysis.

## Technologies used
- Python 3.8.5
- Scrapy 2.4.1
- Pandas 1.2.3
- Beautiful Soup 4.9.3

## Project Details

It's a Web Scraping Project using Python and [Scrapy](https://docs.scrapy.org/en/latest/), a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. The goal of the project is to extract courses information from [Reed](https://www.reed.co.uk/), a popular job and online course provider site and save it to a CSV file for further analysis.


## Folder information
- courseInfo
- courseLink


**courseLink**(This folder will generate course link)




To generate course link, Go inside to courseLink folder and follow these commands

```bash
  cd [scrapy.cfg file path]
```
```bash
  scrapy crawl courseLink
``` 
We need to move generated CSV file into courseInfo folder.


**courseInfo**(This folder will generate course info)

To generate course Info, Go inside to courseInfo folder and follow these commands

```bash
  cd [scrapy.cfg file path]
```
```bash
  scrapy crawl courseInfo
``` 
## Extracted Data information
Extracted CSV will have total 22 columns.Those are:
- date	
- courseId	
- courseTitle	
- courseLink	
- subtitle
- courseProvider
- offerPrice	
- originalPrice	
- unitSold	
- category	
- haveCpd	
- cpdPoint	
- awardingBody	
- qualName	
- isRegulated	
- hasProfCert	
- savingsPercent	
- broadCategory1	
- broadCategory2	
- subCategory1	
- subCategory2	
- OnDemand

## Data Sample
![ALT](https://github.com/Tareq553/Scraping-Project-3/blob/main/courseInfo/Data_sample.png)




## Author

- [M Tareq Rahman](https://www.github.com/Tareq553)

