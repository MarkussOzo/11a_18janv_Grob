import csv

with open ("2.uzd.csv", "r") as otrais:
    fun = csv.reader(otrais)
    print(fun)