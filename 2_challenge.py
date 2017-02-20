"""Decrypt text challenge2."""

import collections

file_to_decrypt = open("2_text.txt", "r")

print collections.Counter(file_to_decrypt.read())
