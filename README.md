# Mission to Mars Web scraping 

## Overview 

This project includes code to scrape mars related webpages, gather the data to save in a Mongo DB database, and display a web page served up via flask. 

The following websites were scraped: 
- https://mars.nasa.gov/news/
- https://spaceimages-mars.com/
- https://galaxyfacts-mars.com/
- https://marshemispheres.com/

## Steps 

1 - Ensure that MongoDB is installed locally. Update the DB connection string in app.py

2 - Ensure your environment has the following: Pandas, BeautifulSoup, Splinter, ChromeDriverManager, Flask, PyMongo

3 - Start the flask application, app.py

4 - Go to http://127.0.0.1:5000/ (local) and click "Click to scrape data" to execute 
