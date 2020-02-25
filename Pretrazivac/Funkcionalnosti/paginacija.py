import math

def paginacija(lista,r0,r1,r2,r3,r4):
    number = 10 # na googlu ima 10 linkova na jednoj pretrazi
    first = 0
    last = 0

    if number > lista.__len__():
        last = lista.__len__()
    else:
        last = number
    poruka = ""
    while True:
        ispis(lista, first, last,poruka,number,r0,r1,r2,r3,r4)
        print()

        option = pom(poruka)

        if option == "N" or option == "n":
            poruka=""
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
                last = number
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

def ispis(lista, first, last,poruka,broj,m0,m1,m2,m3,m4):
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------------------")

    print("                                    RANK & PAGES:" ,int(math.ceil(last/broj)))
    print("RANG\t\tBR RECI\t\tR1\t\t\tR2\t\t\tR3\t\t\tR4\t\t\t\t\t\t\t\t\t\t\tlink")
    if poruka == "Na pocetku fajla ste!":
        print(poruka)
    for i in range(first, last, 1):

        print("%0.3f\t\t%0.3f\t\t%0.3f\t\t%0.3f\t\t%0.3f\t\t%0.3f\t\t%s"%( lista[i].getRang(),m0[lista[i].getPage()],m1[lista[i].getPage()],m2[lista[i].getPage()],m3[lista[i].getPage()],m4[lista[i].getPage()],lista[i].getPage()))
        #print("%0.3f\t\t%0.3f\t\t%0.3f\t\t%0.3f\t\t%0.3f\t\t%0.3f\t\t" % ( m0[lista[i].getPage()], m1[lista[i].getPage()], m2[lista[i].getPage()], m3[lista[i].getPage()], m4[lista[i].getPage()]))
        #print( str(round(lista[i].getRang(),3)) + " " + lista[i].getPage() )

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