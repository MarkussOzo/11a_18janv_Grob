# 2.    Izveidot Python programmu, kas nolasītu un izdrukātu tikai otrās kolonnas datus no CSV faila.

import csv

def otrais(csv_fails):
    with open(csv_fails, 'r', newline='', encoding='utf-8') as fails:
        lasitajs = csv.reader(fails)
        for rinda in lasitajs:
            if len(rinda) > 1:
                print(rinda[1])

csv_fails = '2.uzd.csv'
otrais(csv_fails)
