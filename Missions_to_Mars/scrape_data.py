from bs4 import BeautifulSoup
from bs4.element import XMLProcessingInstruction
import requests
import pandas as pd
import datetime as dt
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    News_header, News_article = get_mars_news()

    mars_data = {
        'news_title' : News_header,
        'news_article' : News_article,
        'featured_image' : get_mars_images(browser)
  #      'mars_facts' : mars_facts(),
  #      'hemispheres' : img_urls_titles,
  #      'last_modified' : dt.datetime.now()
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data


def get_mars_news():
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news_title = soup.find('div', class_='content_title').get_text()
    news_title = news_title.replace('\n', '')

    news_article =  soup.find('div', class_='rollover_description_inner').get_text()
    news_article = news_article.replace('\n', '')

    print(news_title)
    return news_title, news_article 

def get_mars_images(browser):

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all elements that contain image
    for item in soup.find_all('img', class_='headerimage fade-in'):
        featuredimage = item['src']

    featuredimage = url + featuredimage
    print(featuredimage)
    return featuredimage


# def get_mars_facts():


#     return X


# def get_mars_hemispheres():


#     return X