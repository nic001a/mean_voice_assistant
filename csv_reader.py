# this file is just to prototype function and link
# csv reading and google api return
# just ignore it

import csv

with open('curse_eng.csv') as csv_file:
    csv_read = csv.reader(csv_file)
    for row in csv_read:
       # print(row[0])
        print(row)
# bro i SAID ignore it what u doing here


def curse_reader(swear_word, nlp_return):
    if swear_word in nlp_return:
        return swear_word

# u done ?
