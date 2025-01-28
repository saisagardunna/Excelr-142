import re
from collections import Counter

def main():
    # Load the text file
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    # Tokenize the text (split into words, convert to lowercase)
    tokens = re.findall(r'\w+', text.lower())

    # Calculate term frequencies
    token_counts = Counter(tokens)

    # Get top 5 most frequent tokens
    top_tokens = token_counts.most_common(5)

    # Display results
    print("\nTop 5 most frequent tokens:")
    for token, count in top_tokens:
        print(f"{token}: {count}")

if __name__ == "__main__":
    main()