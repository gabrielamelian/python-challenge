import string

to_decrypt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alphabet = list(string.ascii_lowercase)

def decrypt(letter):
    if (letter in alphabet):
        decoded_letter_index = alphabet.index(letter) + 2
        max_index = len(alphabet) -1
        if (decoded_letter_index >= max_index):
            return alphabet[decoded_letter_index - len(alphabet)]
        return alphabet[decoded_letter_index]
    return letter

print ''.join(map(decrypt, to_decrypt))

# Solution using maketrans()

alphabet_string = "abcdefghijklmnopqrstuvwxyz"
cypher = "cdefghijklmnopqrstuvwxyzab"

translator = string.maketrans(alphabet_string, cypher)

print to_decrypt.translate(translator)
print "map".translate(translator)
