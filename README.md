# SOP-Creator-Data-Mining

## Overview

This project is part of a Data Mining course, aiming to create Statements of Purpose (SOPs) for universities using a dataset of universities. The primary objectives of the project include data cleaning, keyword extraction, and generating SOPs. Due to constraints, the original plan of crawling websites for SOPs was abandoned in favor of utilizing OpenAI's GPT-3 with the assistance of an OpenAI API key.

## Project Description

The University SOP Generator project encompasses the following key components:

1. Data Cleaning: The initial dataset of universities requires cleaning to ensure data quality and consistency.

2. Keyword Extraction: Extract relevant keywords from the dataset to be used in the SOPs.

3. SOP Generation: Utilize OpenAI's GPT-3 and an OpenAI API key to generate Statements of Purpose for universities based on the extracted keywords.

4. Website Crawling (Unused): Although the main.py file contains code for website crawling using Selenium, this feature was not implemented in the main notebook code due to limitations and cost factors.

5. Word Cloud Visualization: Generate word clouds to visualize the most frequent keywords extracted from the dataset.

## Prerequisites

Before running this project, ensure you have the following:

- Python installed on your system.
- Required Python libraries and dependencies installed (specified in the project's requirements file).
- An OpenAI API key to access the GPT-3 model.

## Installation

1. Clone this repository or download the source files.

2. Install the necessary Python packages using pip or your preferred package manager:

   ```bash
   pip install -r requirements.txt

3. Configure your OpenAI API key by following the provided instructions.

4. Run the main notebook code to perform data cleaning, keyword extraction, and SOP generation.

5. Optionally, run main.py if you wish to utilize Selenium for website crawling (note that this feature is not integrated into the main notebook code).

## Usage

1. Execute the main notebook to clean the dataset and generate SOPs.

2. Review the generated SOPs and adjust them as needed.

3. Execute main.py if you decide to use Selenium for website crawling (make sure you've configured the script accordingly).

4. Visualize the extracted keywords using word cloud visualization.

## Dataset
To replicate the project, you can download the universities dataset from the provided files uploaded in this repository.

## Authors
Helia Ghahraman, Mehrnaz Sadeghieh

Thank you for exploring our University SOP Generator project. We hope this tool assists you in generating Statements of Purpose for universities efficiently and effectively.
