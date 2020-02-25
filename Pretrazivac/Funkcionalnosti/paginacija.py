import math

def paginacija(lista):
    number = 10 # na googlu ima 10 linkova na jednoj pretrazi
    first = 0
    last = 0

    if number > lista.__len__():
        last = lista.__len__()
    else:
        last = number
    poruka = ""
    while True:
        ispis(lista, first, last,poruka,number)
        print()

        option = pom(poruka)

        if option == "N" or option == "n":
            poruka=""
            #first += number
            #last += number
            #if last > lista.__len__():
            #    last = lista.__len__()
            if last + number > lista.__len__():
                last = lista.__len__()
                if first+number > lista.__len__():
                    first = first
                    poruka = "Dosli ste do kraja fajla!"
                else:
                    first +=number
                    poruka = "Dosli ste do kraja fajla!"
            else:
                first+=number
                last+=number
        elif option == "B" or option == "b":
            poruka=""
            if first - number < 0:
                first = 0
                last = number #mislim da fali if kad je broj stranica manji od number
                poruka="Na pocetku fajla ste!"
                if last> lista.__len__():
                    last= lista.__len__()
            else:
                last = first
                first -= number
        elif option == "C" or option == "c":
            #no = input("Unesi broj : ")
            while True:
                try:
                    no = int(input("Unesi broj : "))
                    break
                except ValueError:
                    print('Unesite prirodan broj.')

            if int(no) < 0:
                print("Greska pri unosu! Unesi broj" )
            else:
                if int(no)< last-first:
                    poruka=""

                if int(no) < last - first:
                    poruka = ""
                number = int(no)
                if first + number > lista.__len__():
                    last = lista.__len__()
                else:
                    if first == lista.__len__():
                        last = first
                        first -= number
                    else:
                        last = first + number
        elif option == "x" or option == "X":
            return

def ispis(lista, first, last,poruka,broj):
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------------------")

    print("                                    RANK & PAGES:" ,int(math.ceil(last/broj)))

    if poruka == "Na pocetku fajla ste!":
        print(poruka)
    for i in range(first, last, 1):
        print( str(round(lista[i].getRang(),2)) + " " + lista[i].getPage() )

    if poruka=="Dosli ste do kraja fajla!":
        print(poruka)


def pom(poruka):
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------------------")

    print("\t\tIzaberite jednu od ponudjenih opcija: ")
    while True:
        if poruka!="Na pocetku fajla ste!":
            print("BACK (B)")
        if poruka != "Dosli ste do kraja fajla!":
            print("NEXT (N)")
        #    print(colors.CYAN + "\t\tBACK (B)" + colors.END)
        print("Promeni broj linkova na stranici (C)")
        print("Exit (X)")
        print()
        option = input("Unesi : ")

        if poruka != "Dosli ste do kraja fajla!":
            if option.upper() not in ("B", "N", "C", "X"):
                  print("Pogresan unos!")
                  continue
        else:
             if option.upper() not in ("B", "C", "X"):
                 print("Pogresan unos!")
                 continue
             if option.upper() in ("B","X"):
                 poruka=""


        if poruka != "Na pocetku fajla ste!":
            if option.upper() not in ("B", "N", "C", "X"):
                  print("Pogresan unos!")
                  continue
        else:
            if option.upper() not in ("N", "C", "X"):
                print("Pogresan unos!")
                continue
        if option.upper() in ("N", "X"):
            poruka = ""


        return option