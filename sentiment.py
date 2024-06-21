import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the Excel file
df = pd.read_excel('scrapping_030623.xlsx', sheet_name='Sheet1')

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Create a new DataFrame to store the results
results_df = pd.DataFrame(columns=['Positive', 'Neutral', 'Negative', 'Compound'])

# Function to preprocess text
def preprocess_text(row):
    # Combine all cell contents in the row into a single string
    text = ' '.join([str(cell) for cell in row])
    return text

# Function to analyze sentiment
def analyze_sentiment(text):
    # Analyze the sentiment of the text
    sentiment_scores = analyzer.polarity_scores(text)
    return sentiment_scores

# Process each row in the DataFrame
for i in range(len(df)):
    text = preprocess_text(df.iloc[i])
    sentiment_scores = analyze_sentiment(text)
    
    # Save the detailed sentiment scores in the results DataFrame
    results_df.loc[i] = [sentiment_scores['pos'], sentiment_scores['neu'], sentiment_scores['neg'], sentiment_scores['compound']]

# Save the results to a new Excel file
results_df.to_excel('output.xlsx', index=False)
