# 3.	Izveidot Python programmu, kas nolasītu un izdrukātu trešās teksta faila rindas saturu.

def tresais(fails):
    try:
        with open(fails, 'r', encoding='utf-8') as f:
            rindas = f.readlines()
            if len(rindas) >= 3:
                tresa_rinda = rindas[2].strip()
                print(tresa_rinda)
            else:
                print("faila ir mazak par 3 rindam")
    except FileNotFoundError:
        print(f"faila '{fails}' nav atrasts")
    except Exception as e:
        print(f"kluda: {e}")

teksta_fails = '3.uzd.txt'
tresais(teksta_fails)
