
import sys

if len(sys.argv) < 2:
    print("Add the link")

link = sys.argv[1]

results = [f.strip('\n') for f in open('links.txt', 'r', encoding='utf-8')]

for data in results:
    if data == link:
        print("Link exits")
    else:
        print("Link does not exist")
