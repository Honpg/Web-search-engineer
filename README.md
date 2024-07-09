# Web Search Engine for Books

Welcome to the Web Search Engine for Books project! This repository contains the code and documentation for a web search engine specifically designed to help users find books efficiently. Below, you will find a detailed description of the project, including the process of creating the web application, data collection methods, and evaluation metrics.

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Data Collection](#data-collection)
- [Web Application Development](#web-application-development)
- [Evaluation](#evaluation)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

This project aims to develop a robust and efficient web search engine tailored for book searches. It provides users with the ability to search for books based on various criteria, including title, author, genre, and more.

## Project Overview

The project is divided into three main parts:

1. **Data Collection**: Gathering and preprocessing book data from various sources.
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
