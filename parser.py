import csv

with open('foozball_excerpt_2011.csv', 'rb') as foozball:
    reader = csv.reader(foozball)
    for row in reader:
        print 'lol wat', row[-1]
