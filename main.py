import datetime, os
# from rich.console import Console
li_doctor = [["Mathieu", "Dan", "Du bois", "0906340486", "G1752/-", "pediatre"]]
li_patient = []
di_patient = {}
len_doc, len_pat = len(li_doctor), len(li_patient)
debut = 0

# fonction anonyme qui nettoye le terminal
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
# clear()


def add_new_doctor(nom, postnom, prenom,
                   tel, specialisation):
    """

    :param nom: ex(KAFANDA)
    :param postnom: ex(NDALA)
    :param prenom: ex(Paul)
    :param tel: num de tel
    :param specialisation: ex(Pediatre)
    :return: void
    """
    dateact = datetime.datetime.now()
    annee = str(dateact.year)
    place = str(len(li_doctor)+1)
    matricule = annee[-2:] + (nom[1]).upper() + (postnom[1]).upper() + place.zfill(3)

    li_doctor.append([nom, prenom, postnom,
                      tel, matricule, specialisation])
    pass


def add_new_patient(nom, postnom, prenom,
                    tel, poids, taille, genre,
                    age):
    """

    :param nom:
    :param postnom:
    :param prenom:
    :param tel:
    :param poids:
    :param taille:
    :param genre:
    :param age:
    :return:
    """
    dateact = datetime.datetime.now()
    annee = str(dateact.year)
    place = str(len(li_patient) + 1)
    numero_dossier = genre.upper() + nom[0] + postnom[0] + prenom[0] + annee[-2:] + place.zfill(4)
    imc = poids/(taille**2)

    li_patient.append([nom, postnom, prenom,
                       tel, poids, taille, genre, age, numero_dossier, imc])
    # save_complaints(num_dossier, plainte)
    pass


def find_patients(nom):
    nom = nom.upper()
    for i in range(len_pat):
        if nom == li_patient[i][0] or nom == li_patient[i][1] or\
                nom == li_patient[i][2] or nom == " ".join(li_patient[i][:3]):
            print(" ".join(li_patient[i]))
            pass
    pass


def find_patient(numero_dossier):
    mattt = numero_dossier
    mat_p = 0
    for i in range(len(li_patient)):
        if mattt == li_patient[i][8]:
            print(" ".join(li_patient[i]))
            mat_p = 1
            break
        if mat_p == 0 and i == len(li_patient) - 1:
            print("Inconnu!")
    pass


def show_patients():
    for i in range(len(li_patient)):
        print('\n', i+1, " ".join(li_patient[i]))
    pass


def show_doctor():
    for i in range(len(li_doctor)):
        print('\n', i+1, " ".join(li_doctor[i]))
    pass


def save_complaints(num_dossier, plainte):

    # plainte = input("la Plainte: ")
    di_patient[num_dossier] = plainte
    pass


def save_doctor_schedule():
    pass


def doctor_appointement():
    pass


def show_patient_complaints(numero_dossier):
    mattt = numero_dossier
    mat_p = 0
    for i in range(len(li_patient)):
        if mattt == li_patient[i][8]:
            print(li_patient[i][9])
            mat_p = 1
            break
        if mat_p == 0 and i == len(li_patient) - 1:
            print("Inconnu!")
    pass


def show_patient_imc(numero_dossier):
    mattt = numero_dossier
    mat_p = 0
    for i in range(len(li_patient)):
        if mattt == li_patient[i][8]:
            print(li_patient[i][9])
            mat_p = 1
            break
        if mat_p == 0 and i == len(li_patient) - 1:
            print("Inconnu!")
    pass


def menu():
    print(f"{' ':>30}{'1:':3} {'add_new_doctor':30}".upper(),
          f"{' ':>30}{'2:':3} {'add_new_patient':30}".upper(),
          f"{' ':>30}{'3:':3} {'show_doctor':30}".upper(),
          f"{' ':>30}{'4:':3} {'show_patients':30}".upper(),
          f"{' ':>30}{'5:':3} {'5':30}".upper(),
          f"{' ':>30}{'6:':3} 6".upper(),
          f"{' ':>30}{'7:':3} 7".upper(),
          f"{' ':>30}{'un autre nombre pour quitter':30}".upper(),
          sep="\n")


def nppt():
    nom = input("le nom: ")
    postnom = input("le Post-nom: ")
    prenom = input("le Prenom: ")
    tel = input("le Tel: ")

    return nom, postnom, prenom, tel


def main():
    "{'FIN':#^63}"
    print(f"{' ':>30}{'PROGRAMME DE GESTION D`UN HOPITAL':#^33}")
    while 1:
        menu()
        while 1:
            try:
                choice = int(input("\nVotre choix: "))
                break
            except ValueError:
                print("^Valeur invalide, entrez un nombre")

        match choice:
            case 1:
                nom, postnom, prenom, tel = nppt()
                specialisation = input("la Specialisation: ")
                add_new_doctor(nom, postnom, prenom, tel, specialisation)
                pass
            case 2:
                nom, postnom, prenom, tel = nppt()
                while 1:
                    try:
                        poids = float(input("Le poids: "))
                        break
                    except ValueError:
                        print("Entrez un nombre!: ")

                while 1:
                    try:
                        taille = float(input("La taille: "))
                        break
                    except ValueError:
                        print("Entrer un nombre!: ")

                genre = input("Le genre: ")

                while 1:
                    try:
                        age = float(input("L'age: "))
                        break
                    except ValueError:
                        print("Entrez un nombre!: ")

                add_new_patient(nom, postnom, prenom, tel, poids, taille, genre, age)

                pass
            case 3:
                show_doctor()
                pass
            case 4:
                show_patients()
                pass
            case 5:
                pass
            case 6:
                pass
            case _:
                clear()
                print(f"\n{'FIN':#^63}")
                break
    pass


if __name__ == '__main__':
    main()