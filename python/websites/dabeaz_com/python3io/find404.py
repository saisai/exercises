# find404.py
#
# Find set of all URLs with a 404 error

from timethis import timethis

with timethis("Find 404 urls - text"):
    error_404_urls = set()
    for line in open("access-log"):
        fields = line.split()
        if fields[-2] == '404':
            error_404_urls.add(fields[-4])

    for name in error_404_urls:
        print(name)


with timethis("Find 404 urls - binary"):
    error_404_urls = set()
    for line in open("access-log","rb"):
        fields = line.split()
        if fields[-2] == b'404':
            error_404_urls.add(fields[-4])

    error_404_urls = { n.decode('latin-1')
                       for n in error_404_urls }

    for name in error_404_urls:
        print(name)
