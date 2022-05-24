import datetime
import os

# from rich.console import Console
li_doctor = [["Mathieu", "Dan", "Du bois", "0906340486", "G1752/-", "pediatre"]]
li_patient = []
di_patient = {}
li_doctor_shedule = []
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
    for i in range(len(li_patient)):
        if nom == li_patient[i][0] or nom == li_patient[i][1] \
                or nom.capitalize() == li_patient[i][2] or nom == " ".join(li_patient[i][:3]):
            print(
                  f"{li_patient[i][0]:10} "
                  f"{li_patient[i][1]:10} "
                  f"{li_patient[i][2]:10} "
                  f"{li_patient[i][3]:10} "
                  f"{li_patient[i][4]:5} "
                  f"{li_patient[i][5]:4} "
                  f"{li_patient[i][6]:1} "
                  f"{li_patient[i][7]:3} "
                  f"{li_patient[i][8]:10} "
                  f"{li_patient[i][9]:5}"
            )
            # print(f"{' ':>30}", " ".join(li_patient[i]))
            # pass
    # pass


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
        # 2
        # print(f"{' ':>30}", i + 1, " ".join(li_patient[i]))
        print(
            f"{li_patient[i][0]:10} "
            f"{li_patient[i][1]:10} "
            f"{li_patient[i][2]:10} "
            f"{li_patient[i][3]:10} "
            f"{li_patient[i][4]:5} "
            f"{li_patient[i][5]:4} "
            f"{li_patient[i][6]:1} "
            f"{li_patient[i][7]:3} "
            f"{li_patient[i][8]:10} "
            f"{li_patient[i][9]:5}"
        )
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
    li_jour = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"]
    print(
        f"\n{'':>30} {'0: LUNDI'}"
        f"\n{'':>30} {'1: MARDI'}"
        f"\n{'':>30} {'2: MERCREDI'}"
        f"\n{'':>30} {'3: JEUDI'}"
        f"\n{'':>30} {'4: VENDREDI'}"
        f"\n{'':>30} {'5: SAMEDI'}"
        f"\n{'':>30} {'6: DIMANCHE'}\n"
    )

    # Si la choix est vide l'on doit reentrer une valeur
    # si choix contient 1 car on essaie de le convertir en entier
    # puis on ajoute dans li_doctor_shedule, le jour qui porte cet indice dans li_jour
    # if len(choix) == 1:
    while 1:
        choix = input(
            "Choisissez un jour ex:1 pour Mardi\n"
            "Ou des jours ex: 2;3 pour Mecredi et Jeudi\n"
            "Ou encore une plage de jours ex: 0:6 pour les jours compris entre Lundi & Dimanche"
        )

        while len(choix) == 0:
            choix = input("Saisie invalid!\nVotre choix: ")

        if len(choix) == 1:
            try:
                jour_p = int(choix)
            except ValueError:
                print("Valeur invalide!")
                # choix = input()
            else:
                li_doctor_shedule.append([li_jour[jour_p]])
                break

        # On ajoute ce jour
        # li_doctor_shedule.append([li_jour[jour_p]])
        elif len(choix) == 3:
            if choix[1] == ';':
                try:
                    jour_p_1 = int(choix[0])
                    jour_p_2 = int(choix[-1])
                    # break
                except ValueError:
                    print("Valeur invalid!")
                else:
                    li_doctor_shedule.append([li_jour[jour_p_1], li_jour[jour_p_2]])
                    break

            elif choix[1] == '-':
                try:
                    jour_p_1 = int(choix[0])
                    jour_p_2 = int(choix[-1])
                except ValueError:
                    print("Valeur invalid!")
                else:
                    li_doctor_shedule_temp = []
                    if jour_p_1 < jour_p_2:
                        for i in range(jour_p_1, jour_p_2+1):
                            li_doctor_shedule_temp.append(li_jour[i])
                        li_doctor_shedule.append(li_doctor_shedule_temp)

                    else:
                        for i in range(jour_p_2, jour_p_1 + 1):
                            li_doctor_shedule_temp.append(li_jour[i])
                        li_doctor_shedule.append(li_doctor_shedule_temp)
                    break
                    pass
            else:
                print("Mauvais separateur")
        elif 3 < len(choix) <= 13:
            li_val = []
            li_jours = []
            val = 0
            print(f"la longeure de choix est de: {len(choix)}")
            for i in range(len(choix)):
                if i % 2 != 0 and i != 0:
                    if choix[i] != ';':
                        # print(f"238 {choix[i]}")
                        print(f"238 {choix[i]}Mauvais separateur!")
                        break
                    pass
                elif i % 2 == 0:
                    try:
                        val = int(choix[i])
                    except ValueError:
                        print(f"246 {choix[i]}Valeur invalide!")
                    else:
                        li_val.append(val)
            for i in li_val:
                li_jours.append(li_jour[i])
            li_doctor_shedule.append(li_jours)
            break
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
                nom = input("Le nom du Patient: ")
                find_patients(nom)
                # pass

            case 6:
                numero_dossier = (input("Le numero du dossier: ")).upper()
                find_patient(numero_dossier)
                pass

            case 7:
                clear()
                titre()
                pass

            case 8:
                numero_dossier = (input("Le numero du dossier: ")).upper()
                show_patient_imc(numero_dossier)
                pass

            case 9:
                save_doctor_schedule()

            case _:
                clear()
                print(li_doctor_shedule)
                print(f"\n{' ':>20} {' FIN ':#^50}")
                break
    pass


if __name__ == '__main__':
    main()
