import nltk
from nltk.corpus import stopwords
import spacy

nltk.download('stopwords')


nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):

    text = text.lower()

    doc = nlp(text)

    stop_words = set(stopwords.words('english'))
    
    filtered_tokens = [token.text for token in doc if token.text not in stop_words]
    return " ".join(filtered_tokens)
text = "This is a sample sentence for demonstrating text preprocessing using NLTK and spaCy."
processed_text = preprocess_text(text)

print("Original Text:", text)
print("Processed Text:", processed_text)
