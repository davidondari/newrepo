import re

# open a text file
textnew = open("tryme.txt")
textcontent = textnew.readlines()
textnew.close()

# create a regex to detect presence of specific words
if re.search(r"ADJECTIVE", textcontent) != "None":
    adj = input("please enter an adjective:\n")
    re.sub(adj, textnew.readlines(), 1)
elif textnew.search(r"NOUN", textnew) != "None":
    noun = input("please enter a noun:\n")
    re.sub(noun, textnew.readlines(), 1)
elif textnew.search(r"VERB", textnew) != "None":
    verb = input("please enter a verb:\n")
    re.sub(verb, textnew.readlines(), 1)
else:
    print("no text found")


# search through the text and prompt a user input
# replace the regex words
# close the file
