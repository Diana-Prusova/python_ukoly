"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Diana Průšová
email: di.prusova@gmail.com
discord: Diana P. / Wild Diana#5386
"""
import math

# ULOŽENÉ HODNOTY
texts = ["""
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
"""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
]

registr_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

oddelovac = "-" * 45

analyzovany_text = list()
num_znaku = dict()
pocet_znaku = list()

vysledky = {
    "num slov": 0,
    "title": 0,
    "upper": 0,
    "lower": 0,
    "num čísel": 0,
    "suma čísel": 0
}

# VLASTNÍ KÓD
jmeno = (input("Zadejte své přihlašovací jméno: ")).lower()
heslo = input("Zadejte své heslo: ")

if jmeno in registr_uzivatele.keys() and heslo == registr_uzivatele[jmeno]:
    print(f"{oddelovac}\nVítej v našem analyzátoru textu, {jmeno.capitalize()}!")
    print(f"Máme pro tebe tři texty k analýze.\n{oddelovac}")
    vyber = input("Zvolte si text zadáním čísla od 1 do 3: ")

    if not vyber.isdigit():
        print("Byla zadána chybná hodnota. Ukončuji program...")
    elif int(vyber) not in range(1, len(texts) + 1):
        print(f"Text s hodnotou {vyber} bohžel nemáme v databázi. Ukončuji program...")
    else:
    # OČIŠTĚNÍ SLOV
        for slovo_cleaning in (texts[int(vyber) - 1]).split():
            analyzovany_text.append(slovo_cleaning.strip(".,:;?!"))
            vysledky["num slov"] += 1
    # SČÍTÁNÍ HLEDANÝCH HODNOT       
        for slovo in analyzovany_text:
            if slovo.istitle():
                vysledky["title"] += 1
            elif slovo.isupper():
                vysledky["upper"] += 1
            elif slovo.islower():
                vysledky["lower"] += 1
            elif slovo.isdigit():
                vysledky["num čísel"] += 1
                vysledky["suma čísel"] += int(slovo)
    # POČÍTÁNÍ DÉLKY SLOV       
        for slovo in analyzovany_text:
            delka_slova = len(slovo)
            if delka_slova not in num_znaku.keys():
                num_znaku[delka_slova] = 1
            else:
                num_znaku[delka_slova] += 1

        for klic, hodnota in list(num_znaku.items()):
            pocet_znaku.append((klic, hodnota))

        pocet_znaku = sorted(pocet_znaku)

    # VÝPIS VÝSLEDKU    

        print(oddelovac, "\nTento text obsahuje:")
        print(f"""
        - {vysledky["num slov"]} slov
        - {vysledky['title']} slov začínající velkým písmenem
        - {vysledky['upper']} slov zapsaných velkým písmem
        - {vysledky['lower']} slov zapsaných malým písmem
        - {vysledky['num čísel']} čísle
        - čísla v celkové hodnotě {vysledky['suma čísel']}
        """)
        print(f"{oddelovac}\nDÉLKA|VÝSKYT(graf)      |VÝSKYT(číselně)\n{oddelovac}")
        for index_key, hodnota in pocet_znaku:
            hvezdy = "*" * hodnota
            print(f"{index_key:>5}|{hvezdy:<18}|{hodnota}")

else:
    print("Neregistrovaný úživatel, ukončuji program...")
