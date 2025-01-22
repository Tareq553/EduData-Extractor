
# EduData Extractor

## Project Overview
This web scraping project utilizes Python and the Scrapy framework to extract detailed information about courses offered on Reed.co.uk, a prominent platform for online courses and job listings. The project aims to automate the extraction of course details, which are then saved in a structured CSV format. This dataset can be utilized for further analysis, such as identifying trends in course pricing, popularity, and certification options across various categories.

The project demonstrates how data analysts can leverage web scraping to collect structured data for analysis and decision-making. By implementing this solution, users gain insights into various courses, providers, and certifications, aiding them in understanding market trends and making informed decisions.

## Motivation of this project
In the journey of becoming a proficient data analyst, acquiring the ability to collect and clean data is crucial for meaningful analysis. Web scraping is a vital skill that enables analysts to gather large datasets from online sources, paving the way for insightful analysis. This project focuses on leveraging web scraping techniques to extract structured data, providing a practical learning experience for aspiring data analysts.

## Technologies Used
- **Programming Language**: Python
- **Platform**: Jupyter Notebook
- **Libraries**:
  - Pandas, NumPy
  - Scrapy
  - Beautiful Soup

## Folder Structure and Instructions
- **courseLink**(This folder will generate course link)
To generate course link, Go inside to courseLink folder, open cmd(In windows) and follow these commands

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

