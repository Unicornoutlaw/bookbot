def count_words(text):
    """Returns the number of words in a given text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Returns a dictionary with character frequencies in the text (only alphabetic characters)."""
    char_count = {}
    text = text.lower()  # Convert to lowercase to avoid duplicates
    
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def print_report(word_count, char_frequencies):
    """Prints a formatted report of word and character counts."""
    print("\n--- Book Report ---\n")
    print(f"Total word count: {word_count}\n")
    
    print("Character frequencies:")
    sorted_chars = sorted(char_frequencies.items(), key=lambda x: x[0])  # Sort by character
    
    for char, count in sorted_chars:
        print(f"'{char}': {count}")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        # Count words
        word_count = count_words(file_contents)
        
        # Count character frequencies
        char_frequencies = count_characters(file_contents)
        
        # Print final report
        print_report(word_count, char_frequencies)

main()