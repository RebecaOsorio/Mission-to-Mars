# Mission to Mars

Robin is a data scientist who wants to build a web page that scrapes from  the latest news and it's **summary** ¹, an **image** ² and a **table** ³ that contains the Mars Facts vs the Earths' ones.

##  Resources

To accomplish this project, we used:

* **Data Source:** [Nasa News Website](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date%20desc,created_at%20desc&search=&category=19,165,184,204&blank_scope=Latest) ¹, [Space Images](https://spaceimages-mars.com/) ²,  [Galaxy Facts](https://galaxyfacts-mars.com/) ³, [Mars Hemispheres](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) ⁴

* **Software:** Jupyter Notebooks, Python 3.7.7, Matplotlib 3.5, Flask 1.1.2, Flask-PyMongo 2.3.0, Splinter 0.16.0, BeatifulSoup 4.1.0, Pandas 1.3.5, Mongo Shell Version 5.0.4.


## Requests
The written analysis has the following:

1.  Overview of the statistical analysis:
    
    -   The purpose of the analysis is well defined.  **(3 pt)**
2.  Results:
    
    -   There is a bulleted list that addresses the three key differences in weather between June and December.  **(6 pt)**
3.  Summary:
    
    -   There is a high-level summary of the results and there are two additional queries to perform to gather more weather data for June and December.  **(5 pt)**

## Overview

### Mission_to_Mars_Challenge.ipynb

The code scrapes  **full-resolution images of Mars’s hemispheres** ⁴ and its' **titles** using BeautifulSoup and Splinter. 
|![D1 - Hemisphire Image Full Size](https://user-images.githubusercontent.com/90414330/151499730-93423ebc-539d-4825-a80b-7b79f18fc5a4.png)| ![D1 - Mars Hemisphires](https://user-images.githubusercontent.com/90414330/151499019-dba27a3a-c7d6-4bb3-9648-1f149946e697.png) |
|-------------------------------------------------------------------------------------------------------------------------------|--|

It necessary to do 4 iterations so we could get the four hemispheres images, as describe below:
1. In a `for loop`, refresh the variable `click_on_image`, which looks for all the `<h3>` CSS elements in the Soup Object, as it contains each hemisphere link.
![D1 - Hemisphire Title](https://user-images.githubusercontent.com/90414330/151499709-13b6367d-2db7-4d69-ba27-28164f4b420d.png)
2. Navigate to the full-resolution image page contained in the last variable. ***a.*** Since `click_on_image` contains all the CSS elements, in our case the four images found in the page, we have to click on the the i-th element.
3. Scrape the relative URL to the full-resolution `.jpg`, by looking at the tags `<a target='_blank'>Sample</a>`
![D1 - Hemisphire Image Objective](https://user-images.githubusercontent.com/90414330/151499010-38b7ee2c-5d40-4121-a2a4-424153e8a2a1.png)

4. Scrape the title for the hemisphere image by looking at the `< h2/>` tags.
![D1 - Hemisphire Title](https://user-images.githubusercontent.com/90414330/151499989-45eb5fac-d06e-44e6-96b4-92f22705165d.png)

5.  Create an empty dictionary,  `hemispheres = {}`, inside the  `for`  loop. Where the keys are `title` and `img_url` for our scrapped variables.
6.  Use  `browser.back()`  to navigate back to the beginning to get the next hemisphere image. 

We ended with the following images.
![D1 - Dictionary](https://user-images.githubusercontent.com/90414330/151499713-ffba276a-0f3e-47a9-880d-55dfc35b700e.png)


### Update the Web App with Mars’s Hemisphere Images and Titles
Using Python and HTML skills, we’ll add the code  created in Deliverable 1 to the `scraping.py` file, update your Mongo database, and modify the `index.html` file so the webpage contains all the information collected in this module as well as the full-resolution images and titles for each hemisphere image.

1. It will be easier to export the code by downloading only `Delivery 1 Code.ipynb` as a `.py file`
![D2 - py Code](https://user-images.githubusercontent.com/90414330/151661207-44906864-7fc4-45ca-ac96-482d354cb101.png)

2. In the `scraping.py`  file, there is a dictionary called `data` that holds the information that we need to build the page. So, we have to update it and add the list of dictionaries that contains the URL strings and titles of each hemisphere image, we'll save them with the key `mars_hemispheres`.
![D2 - data Dictionary](https://user-images.githubusercontent.com/90414330/151661202-02e016eb-1d09-49c9-b8a0-542caa777f77.png)

3. Below the last scraping function, in the `scraping.py` file, we created a function that scrapes the hemisphere data by using the code from the `Delivery 1 Code.py` and returns the scraped data as a list of dictionaries with the URL string and title of each hemisphere image.
![D2 - Hemispheres Function](https://user-images.githubusercontent.com/90414330/151661203-b2fec9d3-cce9-4f28-a04a-ed47c3d21596.png)

4. It was necessary to modify the `index.html` file to access to the database, and retrieve the `img_url` and `title` looping thorough the   list of dictionaries using `{% for hemisphere in mars.hemispheres_images_list %}`. 
![D2 - HTML Cards Deck](https://user-images.githubusercontent.com/90414330/151661206-09549bdf-7134-4d44-a84c-42879b1f0adc.png)


After scrapping the data, we should have ended with the following

![D2 - Cards Deck Objective](https://user-images.githubusercontent.com/90414330/151661198-7df1b500-72c5-40c8-a182-52f8bf1719a7.png)

### Add Bootstrap 3 Components
Update of the web app to make it mobile-responsive, and add two additional Bootstrap 3 components to make it stand out.

| ![D3 - Final Delivery](https://user-images.githubusercontent.com/90414330/151664476-9bfc64b4-e3ed-4e5b-b633-3a38858ea596.png) | ![D3 - Final Delivery Hemispheres](https://user-images.githubusercontent.com/90414330/151664478-fa8b8efa-8133-4215-829b-ac89cb7cc6e4.png) | 
|--|--|

![D3 - Final Delivery Tablet](https://user-images.githubusercontent.com/90414330/151664470-1bda2941-babc-40eb-8c1d-766f716ac2a1.png)


> Written with [StackEdit](https://stackedit.io/).