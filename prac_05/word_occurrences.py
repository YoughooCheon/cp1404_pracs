"""
CP1404/CP5632 Practical
Word Occurrences
URL: https://github.com/YoughooCheon/cp1404_pracs/blob/master/prac_05/word_occurrences.py

function main
    get text input from user
    word_counts = call count_word_occurrences with text
    call print_word_counts with word_counts

function count_word_occurrences(text)
    create empty dictionary called word_counts
    split text into words
    for each word in words
        if word is in word_counts
            increment the count
        else
            add word to word_counts with count 1
    return word_counts

function print_word_counts(word_counts)
    sort word_counts by word
    find the length of the longest word
    for each word and count in sorted word_counts
        print word and count formatted with alignment

main()
"""
def main():
    """Get user input, count word occurrences, and print results."""
    text = input("Enter text: ")
    word_counts = count_word_occurrences(text)
    print_word_counts(word_counts)

def count_word_occurrences(text):
    """Return a dictionary with word counts from the input text."""
    word_counts = {}
    words = text.split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def print_word_counts(word_counts):
    """Print word counts sorted alphabetically with aligned formatting."""
    sorted_words = sorted(word_counts.items())
    max_length = max(len(word) for word in word_counts.keys())

    for word, count in sorted_words:
        print(f"{word:{max_length}} : {count}")

if __name__ == "__main__":
    main()