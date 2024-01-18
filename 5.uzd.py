#5.    Izveidot Python programmu, kas ļauj lietotājam ievadīt savu vārdu terminālī. Ievadīto vārdu pēc tam ierakstīt teksta failā (piemēram, "lietotajs.txt"). Programmai jābūt spējīgai apstrādāt kļūdas, piemēram, faila nepieejamību vai rakstīšanas problēmas. Pēc ierakstīšanas izvadīt paziņojumu par veiksmīgu darbību vai kļūdu gadījumā attiecīgu kļūdas ziņojumu.

def vards():
        lietotajs = input("Ievadiet savu vārdu: ")

        with open("lietotajs.txt", 'w', encoding='utf-8') as fails:
            fails.write(lietotajs)

        print("vards veiksmīgi ierakstīts failā 'lietotajs.txt!!!'.")
        
vards()
