"""Decrypt text challenge3."""

import re

file_to_decrypt = open("3_text.txt", "r")
long_str = file_to_decrypt.read()

long_str = long_str.replace('\r', '').replace('\n', '')

splitted_list = re.findall('[a-z][^a-z]*', long_str)

for i, unit in enumerate(splitted_list):
    previous_unit = splitted_list[i - 1]
    if len(unit) == 4 and len(previous_unit) == 4:
        print unit[0]

"""
Message is 'linkedlist', going to linkedlist.html says to open linkedlist.php.
"""
