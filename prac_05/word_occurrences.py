"""
CP1404/CP5632 Practical
Word Occurrences
Estimated time: 20 minutes
Actual time: (record your actual time)

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
