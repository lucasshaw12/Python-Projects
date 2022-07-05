#! python3
# Using regular expressions, fill in the placeholder words 'ADJECTIVE, NOUN, VERB'
# with values obtained from the input()
import re

# Create the file then write the phrase to the file 
madlibFile = open(f'madlibs.txt', 'w')
madlibFile.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events. ')
madlibFile.close()

# Open the read to file to identify the words to replace
madlibFile = open(f'madlibs.txt')
madlibFileText = madlibFile.read()
madlibFile.close()

# Find the shelve variables within the madlibs.txt
madlib_regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')   
for word in madlib_regex.findall(madlibFileText):
    for i in word:
        if i != '':
            reg = re.compile(r'{}'.format(i))
            inp_word = input('input a word for {}: '.format(i))
            madlibFileText = reg.sub(inp_word, madlibFileText, 1)

print(madlibFileText)

madlibFile = open('madlibs.txt', 'w')
madlibFile.write(madlibFileText)
madlibFile.close()