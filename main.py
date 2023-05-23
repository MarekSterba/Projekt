from pojistenec import seznam_pojistencu, Pojistenec

#nadpis
print("-" * 30)
print("Evidence pojistenych")
print("-" * 30)

print("Vyberte si akci:\n1 - Pridat pojisteneho\n2 - Vypsat vsechny pojistene\n3 - Vyhledat pojisteneho\n4 - Konec")
pokracovat = "ano"
while (pokracovat == "ano"):
    operace = int(input(""))

#pridani pojisteneho    
    if (operace == 1):
        jmeno = input("Zadejte jmeno pojisteneho:\n")
        prijmeni = input("Zadejte prijmeni:\n")
        mobil = input("Zadejte telefonni cislo:\n")
        vek = input("Zadejte vek:\n")
        seznam_pojistencu.append(Pojistenec(jmeno, prijmeni, vek, mobil))
        print("Data byla ulozena. Pokracujte libovolnou klavesou...")

#vypis pojistencu
    elif (operace == 2):
        for pojistenec in seznam_pojistencu:
            print(pojistenec)

#vyhledani pojistence
    elif (operace == 3):
        jmeno = input("Zadejte jmeno pojisteneho:\n")
        prijmeni = input("Zadejte prijmeni:\n")
        for pojistenec in seznam_pojistencu:
            if pojistenec.jmeno == jmeno and prijmeni == prijmeni:
                print(pojistenec)
#konec
    elif (operace == 4):
        print("Konec")
#spatne cislo
    else:
        print("Zadal jsi spatne cislo!")
    pokracovat = input("Prejete si zadat dalsi operaci? [ano/ne]: ")
    print("Vyberte si akci:\n1 - Pridat pojisteneho\n2 - Vypsat vsechny pojistene\n3 - Vyhledat pojisteneho\n4 - Konec")
print("Dekuji za zadani!")



