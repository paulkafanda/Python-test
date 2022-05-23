import datetime
import os

# from rich.console import Console
li_doctor = [["Mathieu", "Dan", "Du bois", "0906340486", "G1752/-", "pediatre"]]
li_patient = []
di_patient = {}
len_doc, len_pat = len(li_doctor), len(li_patient)
debut = 0

# fonction anonyme qui nettoye le terminal
# clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


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
    place = str(len(li_doctor) + 1)
    matricule = annee[-2:] + (nom[1]).upper() + (postnom[1]).upper() + place.zfill(3)

    li_doctor.append(
        [
            nom.upper(),
            prenom.capitalize(),
            postnom.upper(),
            tel,
            matricule.upper(),
            specialisation.upper()
        ]
    )
    pass


def add_new_patient(nom, postnom, prenom, tel, poids, taille, genre, age):
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
    imc = poids / (taille ** 2)

    li_patient.append(
        [
            nom.upper(),
            postnom.upper(),
            prenom.capitalize(),
            tel,
            str(poids),
            str(taille),
            genre.upper(),
            str(age),
            numero_dossier.upper(),
            str(imc)
        ]
    )
    # save_complaints(num_dossier, plainte)
    pass


def find_patients(nom):
    nom = nom.upper()
    for i in range(len_pat):
        if nom == li_patient[i][0] or nom == li_patient[i][1] \
                or nom.capitalize() == li_patient[i][2] or nom == " ".join(li_patient[i][:3]):
            print(f"{' ':>30}", " ".join(li_patient[i]))
            pass
    pass


def find_patient(numero_dossier):
    mattt = numero_dossier
    mat_p = 0
    for i in range(len(li_patient)):
        if mattt == li_patient[i][8]:
            print(f"{' ':>30}", " ".join(li_patient[i]))
            mat_p = 1
            break
        if mat_p == 0 and i == len(li_patient) - 1:
            print(f"{' ':>30}Inconnu!")
    pass


def show_patients():
    for i in range(len(li_patient)):
        print(f"{' ':>30}", i + 1, " ".join(li_patient[i]))
    seppep()
    pass


def show_doctor():
    for i in range(len(li_doctor)):
        print(f"{' ':>27}", i + 1, " ".join(li_doctor[i]))
    seppep()
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
            print(f"{' ':>30}", li_patient[i][9])
            mat_p = 1
            break
        if mat_p == 0 and i == len(li_patient) - 1:
            print(f"{' ':>30}Inconnu!")
    pass


def show_patient_imc(numero_dossier):
    mattt = numero_dossier
    mat_p = 0
    for i in range(len(li_patient)):
        if mattt == li_patient[i][8]:
            print(f"{' ':>30}", li_patient[i][9])
            mat_p = 1
            break
        if mat_p == 0 and i == len(li_patient) - 1:
            print(f"{' ':>30}Inconnu!")
    pass


def menu():
    print(f"{' ':>30}{'1:':3} {'add_new_doctor':30}".upper(),
          f"{' ':>30}{'2:':3} {'add_new_patient':30}".upper(),
          f"{' ':>30}{'3:':3} {'show_doctor':30}".upper(),
          f"{' ':>30}{'4:':3} {'show_patients':30}".upper(),
          f"{' ':>30}{'5:':3} {'5':30}".upper(),
          f"{' ':>30}{'6:':3} 6".upper(),
          f"{' ':>30}{'7:':3} nettoyer le terminal".upper(),
          f"{' ':>30}{'un autre nombre pour quitter':30}".upper(),
          sep="\n")


def nppt():
    nom = input(f"{' ':>30}le nom: ")
    postnom = input(f"{' ':>30}le Post-nom: ")
    prenom = input(f"{' ':>30}le Prenom: ")
    tel = input(f"{' ':>30}le Tel: ")

    return nom, postnom, prenom, tel


def titre():
    print(
        f"\n{' ':>20} {' DEBUT ':#^50}",
        f"{' ':>29} {'PROGRAMME-DE-GESTION-D-UN-HOPITAL':#^33}",
        f"{' ':>20} {' DEBUT ':#^50}",
        sep='\n', end='\n' * 2
    )


def seppep():
    print('\n' * 2)


def main():
    """

    """
    titre()
    while 1:
        menu()
        while 1:
            try:
                choice = int(input(f"\n{' ':>30}Votre choix: "))
                break
            except ValueError:
                print(f"{' ':>30}^Valeur invalide, entrez un nombre")

        match choice:
            case 1:
                nom, postnom, prenom, tel = nppt()
                specialisation = input(f"{' ':>30}la Specialisation: ")
                add_new_doctor(nom, postnom, prenom, tel, specialisation)
                pass

            case 2:
                nom, postnom, prenom, tel = nppt()
                while 1:
                    try:
                        poids = float(input(f"{' ':>30}Le poids: "))
                        break
                    except ValueError:
                        print(f"{' ':>30}Entrez un nombre!")

                while 1:
                    try:
                        taille = float(input(f"{' ':>30}La taille: "))
                        break
                    except ValueError:
                        print(f"{' ':>30}Entrer un nombre!")

                genre = input(f"{' ':>30}Le genre: ")

                while 1:
                    try:
                        age = int(input(f"{' ':>30}L'age: "))
                        break
                    except ValueError:
                        print(f"{' ':>30}Entrez un nombre!: ")

                add_new_patient(nom, postnom, prenom, tel, poids, taille, genre, age)

                pass
            case 3:
                show_doctor()
                pass

            case 4:
                show_patients()
                pass

            case 5:
                nom = (input("Le nom du Patient: ")).upper()
                find_patients(nom)
                pass

            case 6:
                numero_dossier = (input("Le numero du dossier: ")).upper()
                find_patient(numero_dossier)
                pass

            case 8:
                numero_dossier = (input("Le numero du dossier: ")).upper()
                show_patient_imc(numero_dossier)
                pass

            case 7:
                clear()
                titre()
                pass

            case _:
                clear()
                print(f"\n{' ':>20} {' FIN ':#^50}")
                break
    pass


if __name__ == '__main__':
    main()
