#!/usr/bin/env python
# coding: utf-8

# In[31]:


# import libraries
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
import time

# set up
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=True)


# In[2]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[3]:


# print the html
print(soup.prettify())


# In[4]:


# news_title = soup.find('div', class_='content_title').find('a').text
# news_title = news_title.replace('\n', '').replace('\r', '')
# news_title
soupyBody = soup.body
news_title = soupyBody.find("div", class_="content_title").find('a').text
news_title

# news_p = soupyBody.find("div", class_="article_teaser_body")
# news_p


# In[5]:


# =========================== Finding url of image on jet propulsion labratory =========================== #
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[6]:


# print the html
print(soup.prettify())


# In[7]:


main_section = soup.find("section", class_="main_feature")

background_image_url = main_section.find("article", class_="carousel_item")['style']
raw_url = background_image_url.split("'")[1]
featured_image_url = 'https://www.jpl.nasa.gov' + raw_url
featured_image_url


# In[8]:


# =========================== Finding weather from Mars Weather Report Twitter =========================== #
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[9]:


# print the html
print(soup.prettify())


# In[10]:


mars_weather = soup.find("div", class_="js-tweet-text-container").find("p", class_="tweet-text").text
mars_weather


# In[11]:


# =========================== MARS FACTS =========================== #
url = 'https://space-facts.com/mars/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[32]:


mars_table = soup.find_all('table')[0] # Grab the first table
mars_table = str(mars_table)

new_table = pd.read_html(mars_table)
new_table = new_table[0]
new_table


# In[34]:


# =========================== HEMISPHERE IMAGES =========================== #

hemisphere_image_urls = [
    {'title':'Cerberus hemisphere','img_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},
    {'title':'schiaparelli','img_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},
    {'title':'valles marineris','img_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'},
    {'title':'syrtis major','img_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}   
]
hemisphere_image_urls


# In[ ]:





# In[ ]:




