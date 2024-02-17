# Sentiment_analysis

## Introduction

This repository contains two implementations of sentiment analysis using machine learning techniques. The project focuses on analyzing the sentiment of a given text, providing insights into the emotions expressed.

### Sentiment Analysis with NLTK

In this implementation, the NLTK (Natural Language Toolkit) library is used for sentiment analysis. The process involves tokenization, removing stop words, and analyzing sentiment using the VADER sentiment intensity analyzer. Additionally, the project visualizes the emotions detected through bar charts.

### Sentiment Analysis without NLTK

This implementation does not use NLTK and focuses on a simpler approach to sentiment analysis. It involves basic text processing steps, such as lowercasing and removing punctuation, followed by tokenization and stop word removal. The emotions detected are visualized using bar charts.

## Project Structure

- `Data`: Contains the input text file (`read.txt`) and the emotion mapping file (`emotion.txt`).
- `NLTK_SentimentAnalysis.py`: Python script for sentiment analysis using NLTK.
- `Simple_SentimentAnalysis.py`: Python script for sentiment analysis without NLTK.

Requirements
Python 3.x
Libraries: NLTK, Matplotlib
License
This project is licensed under the MIT License.

Acknowledgments
Special thanks to NLTK for providing a powerful tool for natural language processing.
Feel free to explore and contribute to the project! If you encounter any issues or have suggestions, please open an issue or submit a pull request.
