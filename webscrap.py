import requests

res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
type(res)

res.raise_for_status()

playfile = open("romeo and juliet play.txt", "wb")

for chunk in res.iter_content(100000):
    playfile.write(chunk)

playfile.close()
