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

def get_most_common_words(tokens, top_n=10):
    """Get the top N most common words."""
    word_count = Counter(tokens)
    return word_count.most_common(top_n)

def display_most_common_words(most_common_words):
    """Display the most common words."""
    print("Top 10 most common words:")
    for word, frequency in most_common_words:
        print(f"{word}: {frequency}")

def main():
    # Path to the text file
    file_path = input("Enter the path to the text file: ")

    # Load the text file
    text = load_text_file(file_path)

    # Tokenize the text
    tokens = tokenize_text(text)

    # Get the 10 most common words
    most_common_words = get_most_common_words(tokens, top_n=10)

    # Display the most common words
    display_most_common_words(most_common_words)

if __name__ == "__main__":
    main()