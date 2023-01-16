# ikman-scraper

### About the scraper
This is a simple web scraper i have wrote to scrape apartment advertisements data in Colombo area from ikman.lk website.
To write this, I used BeautifulSoup library and Requests library. 
Here i have tried to 3 main information from ads. 
This scraper is only able scrape data from single static page

### Data
Those are tittles,rental and informations about the apartment.

### Problems
When i was writing this, i have ran into problem with a 'div' container. The problem is, The information about the apartment(number of rooms and bathrooms) was written under 'div' container with no 'class ID'. So i was failed to scrape those information. I have tried several methods using CSS selectors, tried to navigate from "find" method and used for loops. But stil failed to scrape. So i scraped all data including tittle,rental price and information.

## Will develop into a web crawler
I'm looking to develop this into web crawler that can scrape multipage across website.
