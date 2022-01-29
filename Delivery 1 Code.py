
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# Convert the browser html to a soup object
html = browser.html
hemispheres_soup = soup(html, 'html.parser')


# 2. Create lists to hold the images and titles.
hemisphere_images = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    
    # Find the CSS element that holds all the links to the full-resolution images
    click_on_image = browser.find_by_css('h3')
    
    # Click the imahe
    click_on_image[i].click()
    
    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    img_sample_tag = img_soup.find('a',target="_blank",text='Sample')
    img_path = 'https://marshemispheres.com/' + img_sample_tag.get('href')
    
    title_html = img_soup.find('h2')
    img_title = title_html.get_text()
    
    hemispheres = {"img_url":img_path,
                "title":img_title}
    hemisphere_images.append(hemispheres)
    
    browser.back()


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_images

# 5. Quit the browser
browser.quit()


