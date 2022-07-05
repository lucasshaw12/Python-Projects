#! python3
# Remove all white space from the start and end of a sentence

def textStrip(text):
    import re
    
    # detect the string within text1
    phrase_regex = re.compile(r'\w+')
    stmt = phrase_regex.search(text)

    # remove whitespace from beginning and end
    whitespace_regex = re.compile(r'^\s+|\s+$')
    strip_whitespace = whitespace_regex.sub('', text)

    return strip_whitespace

phrase = input('Enter some text, the function will remove all "spaces" from the start and end: \n')
sentence = textStrip(phrase)
print(sentence)
