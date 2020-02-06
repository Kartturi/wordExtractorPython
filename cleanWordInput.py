

def clean_word_from_spaces_commas(word):
    word_spaces_removed = word.strip()
    return word_spaces_removed[:-1] if word_spaces_removed[-1:] == ',' else word_spaces_removed
