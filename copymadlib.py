import re, copy

textnew = open("tryme.txt")
textcontent = textnew.read()
textnew.close()

# locate instances of keywords
keyregex = re.compile(r"ADJECTIVE|NOUN|VERB|ADVERB", re.I)
matches = keyregex.findall(textcontent)

# prompt user to replace keywords with their own input

answers = copy.copy(matches)

for i in range(len(answers)):
    print("what is your replacement for ", answers[i])
    answers[i] = input()

# create a new text file with the end result

for i in range(len(matches)):
    findmatch = re.compile(matches[i])
    textcontent = findmatch.sub(answers[i], textcontent, count=1)

print(textcontent)
textedited = open("tryme.txt", "w")
textedited.write(textcontent)
textedited.close()
