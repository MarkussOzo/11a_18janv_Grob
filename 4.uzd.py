# 4.	Izveidot Python programmu, kur  lietotājs ievada gan faila nosaukumu, gan faila formātu (paplašinājumu), un atkarībā no faila paplašinājuma tiek nolasīts faila saturs.  Nolasītā informācija ir jāizdrukā terminālī. Ievērot iespejamās kļūdas!

def cetri():
    try:
        
        fails_nosaukums = input("ievadiet faila nosaukumu: ")

        fails_paplasinajums = input("ievadiet faila paplašinājumu : ")

        pilns_ceļš = f"{fails_nosaukums}.{fails_paplasinajums}"

        with open(pilns_ceļš, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print(f"faila '{pilns_ceļš}' saturs:")
            print(saturs)

    except FileNotFoundError:
        print(f"fails '{pilns_ceļš}' nav atrasts.")
    
cetri()
