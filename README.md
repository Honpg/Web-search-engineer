# Web Search Engine for Books

Welcome to the Web Search Engine for Books project! This repository contains the code and documentation for a web search engine specifically designed to help users find books efficiently. Below, you will find a detailed description of the project, including the process of creating the web application, data collection methods, and evaluation metrics.

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Data Collection](#data-collection)
- [Web Application Development](#web-application-development)
- [Project Structure](#project-structure)
- [Evaluation](#evaluation)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

This project aims to develop a robust and efficient web search engine tailored for book searches. It provides users with the ability to search for books based on various criteria, including title, author, genre, and more.

## Project Overview

The project is divided into three main parts:

1. **Data Collection**: Gathering and preprocessing book data from Goodreads sources.
2. **Web Application Development**: Creating a user-friendly web interface for searching books.
3. **Evaluation**: Assessing the performance and accuracy of the search engine.

## Data Collection

### Sources

Data was collected from multiple online sources, including:

- Open Library API
- Google Books API
- Goodreads API

### Process

1. **Data Extraction**: APIs and web crawlers (using Scrapy and Selenium) were used to extract relevant book data, such as titles, authors, publication dates, genres, and summaries.
2. **Data Cleaning**: The raw data was cleaned using Python libraries such as pandas and numpy to remove duplicates, incorrect entries, and incomplete records. This involved aggregating and transforming the data into a format suitable for analysis and visualization. Notably, the GoodreadsScraper component includes functions for cleaning and aggregating data, extracting Kindle prices using Selenium, and handling multivalued attributes.
3. **Data Storage**: The cleaned data was stored in a structured database (MongoDB) to facilitate efficient querying.

### Tools and Technologies

- Python for data extraction and cleaning
- Scrapy and Selenium for web scraping
- pandas and numpy for data cleaning and processing
- MongoDB for data storage

### Example Usage of GoodreadsScraper

The GoodreadsScraper component of this project allows for detailed and efficient data extraction from Goodreads, including author and book data.

#### Author Crawls

To crawl all authors on the Goodreads website:

```bash
python3 crawl.py author
```

#### List Crawls
To crawl books from the first 50 pages of a Listopia list:

```bash
python3 crawl.py list --list_name="1.Best_Books_Ever" --start_page=1 --end_page=50 --output_file_suffix="best_001_050"
```
#### My Books (Shelf) Crawls
To crawl books from a specific user's shelf:

```bash
python3 crawl.py my-books --shelf="read" --user_id="50993735-emma-watson"
```

### Data Enrichment
Additional steps to enrich the data include cleaning and aggregating jsonlines files and extracting Kindle prices using Selenium.

#### Cleaning and Aggregating
To concatenate and clean multiple jsonlines files:

```bash
cat book_*.jl > all_books.jl
cat author_*.jl > all_authors.jl
python3 cleanup.py --filenames best_books_01_50.jl young_adult_01_50.jl --output goodreads.csv
```
Using pandas for data cleaning:
```bash
import pandas as pd
import numpy as np

all_books = pd.read_json('all_books.jl', lines=True)
all_authors = pd.read_json('all_authors.jl', lines=True)

all_books.drop_duplicates(inplace=True)
all_authors.drop_duplicates(inplace=True)
```
#### Extracting Kindle Price
To populate the Kindle price:

```bash
pip3 install selenium
python3 populate_kindle_price.py -f goodreads.csv -o goodreads_with_kindle_price.csv
```
## Web Application Development
### Frameworks and Libraries
The web application was built using the following technologies:

- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python web framework)
- Database: MongoDB
  
### Features
- Search Functionality: Users can search for books by title, author, genre, or keywords.
- Advanced Filters: Filters for publication date, language, and more.
- User Interface: A clean and intuitive interface for easy navigation and use.
  
### Development Process
- Setting Up the Environment: Installing necessary dependencies and setting up the Flask environment.
- Creating Routes: Defining the main routes for the application, including the home page, search results, and book details.
- Implementing Search Logic: Writing the search algorithms to query the database and return relevant results.
- Frontend Design: Designing the frontend to ensure a user-friendly experience.
  
## Project Structure
The project is organized into the following directories and files:
```bash
Web-search-engineer/
├── SEG_ETL_Index_Model/
│   ├── Project.ipynb
│   ├── change_format_date.ipynb
├── SEG_Goodreadscraper/
│   ├── GoodreadsScraper/
│   │   ├── spiders/
│   │   │   ├── __init__.py
│   │   │   ├── custom_filters.py
│   │   │   ├── items.py
│   │   │   ├── middlewares.py
│   │   │   ├── pipelines.py
│   │   │   ├── settings.py
│   ├── .gitignore
│   ├── LICENSE
│   ├── README.md
│   ├── amazon_price_extractor.py
│   ├── chromedriver
│   ├── cleanup.py
│   ├── crawl.py
│   ├── populate_kindle_price.py
│   ├── requirements.txt
│   ├── scrapy.cfg
├── SEG_UI/
│   ├── .idea/
│   │   ├── inspectionProfiles/
│   │   │   ├── Project_Default.xml
│   │   │   ├── profiles_settings.xml
│   │   ├── .gitignore
│   │   ├── SEG_UI.iml
│   │   ├── misc.xml
│   │   ├── modules.xml
│   ├── static/
│   │   ├── images/
│   │   │   ├── background.jpg
│   │   ├── styles.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── detail.html
│   │   ├── home_results.html
│   ├── Web_app.py
├── .gitignore
├── README.md
```
### Directory and File Descriptions

#### `SEG_ETL_Index_Model/`
This directory contains Jupyter notebooks used for Extract, Transform, and Load (ETL) processes, and indexing models.

- **`Project.ipynb`**: Main project notebook for ETL and indexing.
- **`change_format_date.ipynb`**: Notebook for date format conversion tasks.

#### `SEG_Goodreadscraper/`
This directory contains the Goodreads scraping components.

- **`GoodreadsScraper/`**: Subdirectory for the Goodreads scraper.
  - **`spiders/`**: Contains Scrapy spiders used for web scraping.
  - **`__init__.py`**: Initialization file for the scraper module.
  - **`custom_filters.py`**: Custom filter functions for data processing.
  - **`items.py`**: Defines the items (data structures) to be scraped.
  - **`middlewares.py`**: Middleware components for Scrapy.
  - **`pipelines.py`**: Pipelines for processing the scraped data.
  - **`settings.py`**: Configuration settings for Scrapy.
- **`.gitignore`**: Git ignore file to exclude certain files from being committed.
- **`LICENSE`**: License file for the project.
- **`README.md`**: README file specific to the Goodreads scraper.
- **`amazon_price_extractor.py`**: Script to extract prices from Amazon.
- **`chromedriver`**: ChromeDriver executable for Selenium.
- **`cleanup.py`**: Script for cleaning and processing the scraped data.
- **`crawl.py`**: Main script to run the web scraping process.
- **`populate_kindle_price.py`**: Script to populate Kindle prices using Selenium.
- **`requirements.txt`**: List of dependencies required for the scraper.
- **`scrapy.cfg`**: Configuration file for Scrapy.

#### `SEG_UI/`
This directory contains the web application components.

- **`.idea/`**: Configuration files for the integrated development environment (IDE).
  - **`inspectionProfiles/`**: Contains inspection profiles for the project.
    - **`Project_Default.xml`**: Default inspection profile.
    - **`profiles_settings.xml`**: Settings for profiles.
  - **`.gitignore`**: Git ignore file for the IDE settings.
  - **`SEG_UI.iml`**: Module file for the IDE.
  - **`misc.xml`**: Miscellaneous configuration for the IDE.
  - **`modules.xml`**: Modules configuration for the IDE.
- **`static/`**: Static files (e.g., images, CSS) for the web application.
  - **`images/`**: Contains image files.
    - **`background.jpg`**: Background image for the application.
  - **`styles.css`**: CSS file for styling the web application.
- **`templates/`**: HTML templates for the web application.
  - **`base.html`**: Base template for the web application.
  - **`detail.html`**: Template for the detail page.
  - **`home_results.html`**: Template for the home and search results page.
- **`Web_app.py`**: Main script for running the web application.
- **`.gitignore`**: Git ignore file to exclude certain files from being committed.
  
## Evaluation

- **Time to Build a Document**: 0.5s
- **Query Latency**: 0.3s per query
- **Index Vector**: Dimension 768
- **Create Index**: 0.2ms
- **Create Index Vector**: 1s
- **Number of Documents**:
  - **Books**: 9708
  - **Authors**: 4606
- **Database Size**: 120.47MB
- **Average Document Size**: 11.67KB
- **Index Size**: 966.65KB

### Testing on Books:
- **Number of Tokens**: 25071
- **Number of Relevant Results Retrieved**: 6268
- **Precision at P=5**: 0.25

These results indicate the system's efficiency in indexing and querying large datasets and the accuracy of the search results.

## Installation

To set up the project locally, follow these steps:

### Clone the repository:
```bash
git clone https://github.com/Honpg/Web-search-enginee.git
```

### Navigate to the project directory:
```bash
cd Web-search-enginee
```

### Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Run the application:
```bash
flask run
```
## Usage
1.Open your web browser and go to [http://localhost:5000.](http://127.0.0.1:5000)

2.Use the search bar to enter your query.

3.Apply filters to narrow down the search results.

4.Click on a book title to view more details.

## Contributing
We welcome contributions from the community. To contribute:

1.Fork the repository

2.Create a new branch:
``` bash
git checkout -b feature-branch
```
3.Make your changes and commit them:
```bash
git commit -m "Add new feature"
```

4.Push to the branch:
```bash
git push origin feature-branch
```

5.Create a pull request on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
We would like to thank the contributors and the open-source community for their invaluable support and resources.
