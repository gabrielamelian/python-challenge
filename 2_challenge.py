"""Decrypt text challenge2."""

from collections import Counter

file_to_decrypt = open("2_text.txt", "r")
char_frequency = Counter(file_to_decrypt.read())

for char, frequency in char_frequency.iteritems():
    if (frequency == 1):
        print char

"""Solution is equality.html."""
