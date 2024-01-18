# 1.	Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā). (3 punkti)

with open("1.uzd.txt") as text:
    fail = text.read()
    print(fail)