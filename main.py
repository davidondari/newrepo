
hallo = open("C:\\USERS\\HP 15\\DESKTOP\\PYTHON PROJECT\\sayhi.txt", "w")
hallo.write('we are not the same,Im a martian \n')
hallo.close()

hallo = open('sayhi.txt')
print(hallo.readlines())
hallo.close()