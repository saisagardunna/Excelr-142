from textblob import TextBlob
def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity
    polarity = blob.sentiment.polarity
    
    # Determine the sentiment based on the polarity score
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    return sentiment, polarity

# Input text
text = input("Enter the text to analyze: ")

# Analyze the sentiment
sentiment, polarity = analyze_sentiment(text)

# Display the result
print(f"Sentiment: {sentiment}")
print(f"Polarity Score: {polarity}")