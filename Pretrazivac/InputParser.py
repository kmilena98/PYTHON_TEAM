
def ParsirajU():
    upit = input("Unesite upit:")
    delovi = upit.strip().split()
    ispravan = True
    if delovi[0].upper() in ("AND", "OR") or delovi[-1].upper() in ("AND", "OR", "NOT"):
        print("Neispravan upit.")
        return ParsirajU()

    if len(delovi) == 3 and delovi[1].upper() in ("AND", "OR", "NOT"):
        operator = delovi[1]
        if (operator == "AND"):
            print(operator)
        elif (operator == "NOT"):
            print(operator)
        else:
            print(operator)
    else:
        print("obican")

    if len(delovi) > 3:
        for rec in delovi:
             if rec.upper() in ("AND", "OR", "NOT"):
                print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu --rec1 operator rec2--")
                ispravan = False
                while(not ispravan):
                    upit = input("Unesite upit:")






