import nltk
from collections import Counter
from nltk.tokenize import word_tokenize

# Download necessary NLTK data files (only need to do this once)
nltk.download('punkt')

def load_text_file(file_path):
    """Load and return the content of a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def tokenize_text(text):
    """Tokenize the text into words."""
    tokens = word_tokenize(text.lower())  # Convert to lowercase for consistency
    return tokens

def calculate_term_frequency(tokens):
    """Calculate the term frequency of each token."""
    term_frequency = Counter(tokens)
    return term_frequency

def display_top_tokens(term_frequency, top_n=5):
    """Display the top N most frequent tokens."""
    print(f"Top {top_n} most frequent tokens:")
    for token, frequency in term_frequency.most_common(top_n):
        print(f"{token}: {frequency}")

def main():
    # Path to the text file
    file_path = input("Enter the path to the text file: ")

    # Load the text file
    text = load_text_file(file_path)

    # Tokenize the text
    tokens = tokenize_text(text)

    # Calculate term frequency
    term_frequency = calculate_term_frequency(tokens)

    # Display the top 5 most frequent tokens
    display_top_tokens(term_frequency, top_n=5)

if __name__ == "__main__":
    main()