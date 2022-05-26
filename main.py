import datetime
import os

import doctor

# from rich.console import Console
li_doctor = []
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


def load_numero_dossier(li_patients, nom, postnom, prenom, genre):
    """This function will generate a unique directory nomber for given patient
    :param li_patients:
    :param nom:
    :param postnom:
    :param prenom:
    :param genre:
    """
    dateact = datetime.datetime.now()
    annee = str(dateact.year)
    place = str(len(li_patients) + 1)

    return genre.upper() + nom[0] + postnom[0] + prenom[0] + annee[-2:] + place.zfill(4)


def find_patient_npp(li_patients, nom, postnom, prenom):
    for i in range(len(li_patients)):
        if nom == li_patients[i][0] and postnom == li_patients[i][1] and prenom == li_patients[i][2]:
            return i
        else:
            return None


def add_new_patient(li_patients, nom, postnom, prenom, tel, poids, taille, genre, age):
    """

    :param li_patients:
    :param nom:
    :param postnom:
    :param prenom:
    :param tel:
    :param poids:
    :param taille:
    :param genre:
    :param age:
    :return: list of patient informations
    """
    i = find_patient_npp(li_patients, nom, postnom, prenom)
    if isinstance(i, int):
        print("::present::")
        imc = poids / (taille ** 2)

        li_patient_temp = [
            nom.upper(),
            postnom.upper(),
            prenom.capitalize(),
            tel,
            str(poids),
            str(taille),
            genre.upper(),
            str(age),
            li_patients[i][8],
            str(imc)
        ]
        for k in range(li_patients[i]):
            li_patients[i][k] = li_patient_temp[k]
        # li_patients[i] = li_patient_temp[:]
        pass
    else:
        numero_dossier = load_numero_dossier(li_patients, nom, postnom, prenom, genre)
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

    return li_patient[0]


def find_patients(li_patients, nom):
    if len(li_patients) == 0:
        return None

    else:
        nom = nom.upper()
        li_place = []
        for i in range(len(li_patient)):
            if nom == li_patients[i][0] or nom == li_patients[i][1] \
                    or nom.capitalize() == li_patients[i][2] or nom == " ".join(li_patients[i][:3]).upper():
                li_place.append(i)
        if len(li_place) == 0:
            return 0
        else:
            return li_place


def find_patient(li_patients, numero_dossier):
    mattt = numero_dossier
    mat_p = 0
    for i in range(len(li_patients)):
        if mattt == li_patients[i][8]:
            print(f"{' ':>30}", " ".join(li_patient[i]))
            return i

        if mat_p == 0 and i == len(li_patient) - 1:
            return 0


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
        # print(f"{' ':>27}", i + 1, " ".join(li_doctor[i]))
        # print(li_doctor)
        nom = li_doctor[i][0]
        psnom = li_doctor[i][1]
        prenom = li_doctor[i][2]
        tel = li_doctor[i][3]
        mat = li_doctor[i][4]
        spe = li_doctor[i][5]
        print(
            f"{nom:10} "
            f"{psnom:7} "
            f"{prenom:7} "
            f"{tel:10} "
            f"{mat:7} "
            f"{spe:4} "
        )
    seppep()
    pass


def save_complaints(num_dossier, plainte):
    # plainte = input("la Plainte: ")
    di_patient[num_dossier] = plainte
    pass


def save_doctor_schedule(matricule):
    # oui elle fait beaucoup trop de chose :)
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
                li_doctor_shedule.append([matricule, li_jour[jour_p]])
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
                    li_doctor_shedule.append([matricule, li_jour[jour_p_1], li_jour[jour_p_2]])
                    break

            elif choix[1] == '-':
                try:
                    jour_p_1 = int(choix[0])
                    jour_p_2 = int(choix[-1])
                except ValueError:
                    print("Valeur invalid!")
                else:
                    li_doctor_shedule_temp = [matricule]
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
                        print("Mauvais separateur!")
                        # break
                    pass
                elif i % 2 == 0:
                    try:
                        val = int(choix[i])
                    except ValueError:
                        print("Valeur invalide!")
                    else:
                        li_val.append(val)
            for i in li_val:
                li_jours.append(li_jour[i])
            li_doctor_shedule.append(li_jours)
            break
    pass


def doctor_schedule(matricule):
    if len(li_doctor) > 0:
        for i in range(len(li_doctor_shedule)):
            if li_doctor_shedule[i][0] == matricule:
                return li_doctor_shedule[i][1:]
    pass


def doctor_appointement(matricule):
    if len(li_doctor) == 0:
        print("Il n'y a pas encore de medecin!")
    else:
        p_doc = doctor.find_doctor(li_doctor, matricule)      # must be modified
        if p_doc == 1:
            work = doctor_schedule(matricule)
            print(f"Vous travaillerez: {work}")
            pass
        else:
            print("Medecin introuvable!")
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
            return 0
    pass


def menu():
    print(f"{' ':>30}{'1:':3} {'add_new_doctor':30}".upper(),
          f"{' ':>30}{'2:':3} {'add_new_patient':30}".upper(),
          f"{' ':>30}{'3:':3} {'show_doctor':30}".upper(),
          f"{' ':>30}{'4:':3} {'show_patients':30}".upper(),
          f"{' ':>30}{'5:':3} {'find patient by him name':30}".upper(),
          f"{' ':>30}{'6:':3} {'find patient by him code'}".upper(),
          f"{' ':>30}{'7:':3} nettoyer le terminal".upper(),
          f"{' ':>30}{'8:':3} {'show patient imc'}".upper(),
          f"{' ':>30}{'9:':3} {'save doctor schedule'}".upper(),
          f"{' ':>30}{'10:':3} {'find patient by him code'}".upper(),
          f"{' ':>30}{'11:':3} {'verify doctor appointment'}".upper(),
          f"{' ':>30}{'un autre nombre pour quitter':30}".upper(),
          sep="\n")


def nppt():
    nom = input(f"{' ':>30}le nom: ").upper()
    postnom = input(f"{' ':>30}le Post-nom: ").upper()
    prenom = input(f"{' ':>30}le Prenom: ").capitalize()
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
                print(f"{' ':>20} :AJOUT D'UN DOCTEUR:\n")
                nom, postnom, prenom, tel = nppt()
                specialisation = input(f"{' ':>30}la Specialisation: ")
                doc = doctor.add_new_doctor(li_doctor, nom, postnom, prenom, tel, specialisation)[:]
                li_doctor.append(doc)
                pass

            case 2:
                print(f"{' ':>20} :ENREGISTREMENT 'UN PATIENT:\n")
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
                k = find_patient_npp(li_patient, nom, postnom, prenom)
                if isinstance(k, int):
                    pass
                else:
                    add_new_patient(li_doctor, nom, postnom, prenom, tel, poids, taille, genre, age)

                pass
            case 3:
                print(f"{' ':>30} :LISTES DES DOCTEURS:\n")
                show_doctor()
                pass

            case 4:
                print(f"{' ':>20} :LISTE DES PATIENTS:\n")
                show_patients()
                pass

            case 5:
                print(f"{' ':>20} :RECHERCHE DES PATIENTS:\n")
                nom = input("Le nom du Patient: ")
                find_patients(nom)
                # pass

            case 6:
                print(f"{' ':>20} :RECHERCHE D'UN PATIENT PRECI:\n")
                numero_dossier = (input("Le numero du dossier: ")).upper()
                find_patient(numero_dossier)
                pass

            case 7:
                print(f"{' ':>20} :NETTOYAGE DU TERMINAL:\n")
                clear()
                titre()
                pass

            case 8:
                print(f"{' ':>20} :AFFICHAGE DE L'IMC D'UN PATIENT DONNE:\n")
                numero_dossier = (input("Le numero du dossier: ")).upper()
                show_patient_imc(numero_dossier)
                pass

            case 9:
                print(f"{' ':>20} :ENREGISTREMENT DE L'HORRAIRE DU MEDCIN:\n")
                matricule = input("Le matricule du medecin: ")
                p_doc = doctor.find_doctor(li_doctor, matricule)      # MUST BE MODIFIED
                if p_doc == 1:
                    save_doctor_schedule(matricule)
                else:
                    print(f"{' ':>20}Docteur introuvable!\n")

                pass
            case 10:

                pass

            case 11:
                print(f"{' ':>20} :AFFICHAGE DE L'AGENDA DU MEDECIN:\n")
                matricule = (input("Le matricule du Medecin: ")).upper()
                doctor_appointement(matricule)
                pass

            case _:
                clear()
                # print(li_doctor_shedule)
                print(f"\n{' ':>20} {' FIN ':#^50}")
                break
    pass


if __name__ == '__main__':
    main()
