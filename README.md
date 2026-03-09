Largest Economies Web Scraping Project
Overview

This mini project demonstrates how to use Python, Pandas, and NumPy to extract economic data from a webpage and process it into a clean dataset.

The script scrapes a Wikipedia page containing information about the largest economies in the world by GDP (nominal), processes the data, and exports the top 10 economies to a CSV file.

Technologies Used

Python

Pandas

NumPy

Web Scraping using pandas.read_html()

Data Source

The data is collected from an archived version of the Wikipedia page:

List of countries by GDP (nominal)

https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29

Project Workflow

The script performs the following steps:

Extract all tables from the webpage using Pandas.

Select the relevant table containing GDP data.

Clean the DataFrame by:

Replacing column headers with numerical indices.

Selecting relevant columns (Country and IMF GDP values).

Selecting the top 10 economies.

Convert GDP values from Million USD to Billion USD.

Round values to two decimal places.

Rename the columns for clarity.

Export the final dataset to a CSV file.

Output

The script generates a file:

Largest_economies.csv

Example output:

Country	GDP (Billion USD)
United States	26954.00
China	17700.00
Germany	4300.00
Japan	4200.00
India	3700.00
