# Digital Dementia Sentiment Analysis Repository

Welcome to the Digital Dementia Sentiment Analysis repository. This repository contains the code and data used in our research on sentiment analysis related to digital dementia using Twitter data. Below is a detailed description of each file included in this repository.

## Files and Descriptions

1. **Data Cleaning.ipynb**:
   - **Description**: This notebook outlines the basic steps for cleaning the collected Twitter data. It includes handling missing values, removing duplicates, and performing initial data statistics.
   - **Key Steps**:
     - Loading raw data
     - Handling missing values
     - Removing duplicates
     - Basic statistical analysis

2. **Further Cleaning and Lexicon-Based Method.ipynb**:
   - **Description**: This notebook goes beyond basic cleaning by performing advanced text preprocessing. It includes tokenization, lemmatization, and Part-of-Speech (POS) tagging. Additionally, it implements three lexicon-based sentiment analysis approaches.
   - **Key Steps**:
     - Tokenization
     - Lemmatization
     - POS tagging
     - Implementation of lexicon-based sentiment analysis methods

3. **Initial Data Analysis.ipynb**:
   - **Description**: This notebook focuses on the initial analysis of the cleaned Twitter data. It includes creating word clouds and analyzing word frequency to identify common terms and themes.
   - **Key Steps**:
     - Generating word clouds
     - Analyzing word frequency
     - Visualizing common terms

4. **Data Analysis for Lexicon-Based Methods.ipynb**:
   - **Description**: This notebook provides detailed statistics and visualizations for the lexicon-based sentiment analysis. It includes statistical analysis for each city and stage of the data, as well as visualizations to better understand the sentiment distribution.
   - **Key Steps**:
     - Statistical analysis by city and stage
     - Data visualizations
     - Interpretation of results

5. **Supervised Approaches.ipynb**:
   - **Description**: This notebook demonstrates the implementation of supervised machine learning classifiers for sentiment analysis. It includes training, evaluation, and comparison of different models.
   - **Key Steps**:
     - Implementation of supervised classifiers (e.g., SVM, Random Forest, etc.)
     - Model training
     - Model evaluation and comparison

## Repository Structure

- `datasets/`: Contains the raw and cleaned datasets used in the analysis.
- `models/`: Contains the saved models and related files.
- `visualizations/`: Contains the generated visualizations and plots.

## Getting Started

1. Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/Brochan8/ddm_sentiment.git
