import datetime
import os

import doctor

# from rich.console import Console


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

        li_patients.append(
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

    return li_patients[0]


def find_patients(li_patients, nom):
    if len(li_patients) == 0:
        return None

    else:
        nom = nom.upper()
        li_place = []
        for i in range(len(li_patients)):
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
            # print(f"{' ':>30}", " ".join(li_patients[i]))
            return i

        # if mat_p == 0 and i == len(li_patient) - 1:
    return None


def show_patients(li_patients):
    for i in range(len(li_patients)):
        # 2
        # print(f"{' ':>30}", i + 1, " ".join(li_patient[i]))
        print(
            f"{li_patients[i][0]:10} "
            f"{li_patients[i][1]:10} "
            f"{li_patients[i][2]:10} "
            f"{li_patients[i][3]:10} "
            f"{li_patients[i][4]:5} "
            f"{li_patients[i][5]:4} "
            f"{li_patients[i][6]:1} "
            f"{li_patients[i][7]:3} "
            f"{li_patients[i][8]:10} "
            f"{li_patients[i][9]:5}"
        )
    seppep()
    pass


def show_doctor(li_doctors):
    for i in range(len(li_doctors)):
        # print(f"{' ':>27}", i + 1, " ".join(li_doctor[i]))
        # print(li_doctor)
        nom = li_doctors[i][0]
        psnom = li_doctors[i][1]
        prenom = li_doctors[i][2]
        tel = li_doctors[i][3]
        mat = li_doctors[i][4]
        spe = li_doctors[i][5]
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


def find_fiche_complaint(li_complains, numero_dossier):
    for i in range(len(li_complains)):
        if numero_dossier == li_complains[i][0]:
            return i
    return None


def save_complaints(li_patients: list, li_complains: list, num_dossier: str, plainte: str):
    i = find_patient(li_patients, num_dossier)
    k = find_fiche_complaint(li_complains, num_dossier)

    # S'il esiste(le patient)
    if isinstance(i, int):
        # S'il n'y pas encore de Plainte donc pas de fiche
        if len(li_complains) == 0:
            li_complains.append(num_dossier)
            li_complains.append(plainte)

        # S'il a deja une fiche
        elif isinstance(k, int):
            li_complains[k].append(plainte)

        # S'il n'a pas encore de fiche
        elif not isinstance(k, int):
            li_complains.append([num_dossier, plainte])
        return 1
    else:
        return 0


def menu_day(marge=30):
    print(
        f"\n{'':>{marge}} {'0: LUNDI'}",
        f"\n{'':>{marge}} {'1: MARDI'}",
        f"\n{'':>{marge}} {'2: MERCREDI'}",
        f"\n{'':>{marge}} {'3: JEUDI'}",
        f"\n{'':>{marge}} {'4: VENDREDI'}",
        f"\n{'':>{marge}} {'5: SAMEDI'}",
        f"\n{'':>{marge}} {'6: DIMANCHE'}",
        sep='\n', end='\n'*2
    )


def save_doctor_schedule(li_doctors, li_doctor_shedules, matricule):
    # oui elle fait beaucoup trop de chose :)
    li_jour = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"]


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
                li_doctor_shedules.append([matricule, li_jour[jour_p]])
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
                    li_doctor_shedules.append([matricule, li_jour[jour_p_1], li_jour[jour_p_2]])
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
                        li_doctor_shedules.append(li_doctor_shedule_temp)

                    else:
                        for i in range(jour_p_2, jour_p_1 + 1):
                            li_doctor_shedule_temp.append(li_jour[i])
                        li_doctor_shedules.append(li_doctor_shedule_temp)
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
            li_doctor_shedules.append(li_jours)
            break
    pass


def doctor_schedule(li_doctors: list, li_doctor_shedules: list, matricule: str):
    matricule = matricule.upper()

    # si il y'a au moins 1 medecin
    if len(li_doctors) > 0:
        for i in range(len(li_doctor_shedules)):
            if li_doctor_shedules[i][0] == matricule:
                return li_doctor_shedules[i][1:]
    else:
        return None
    pass


def doctor_appointement(li_doctors, li_doctor_schedules, matricule):
    if len(li_doctors) == 0:
        print("Il n'y a pas encore de medecin!")
    else:
        p_doc = doctor.find_doctor(li_doctors, matricule)      # must be modified
        if p_doc == 1:
            work = doctor_schedule(li_doctors, li_doctor_schedules, matricule)
            print(f"Vous travaillerez: {work}")
            pass
        else:
            print("Medecin introuvable!")
    pass


def show_patient_complaints(li_patients, numero_dossier):
    mattt = numero_dossier
    mat_p = 0
    for i in range(len(li_patients)):
        if mattt == li_patients[i][8]:
            print(f"{' ':>30}", li_patients[i][9])
            mat_p = 1
            break
        if mat_p == 0 and i == len(li_patients) - 1:
            print(f"{' ':>30}Inconnu!")
    pass


def show_patient_imc(li_patients, numero_dossier):
    li_status_imc = [
        "Insuffisance pondérale (maigreur)",
        "Corpulence normale",
        "Surpoids",
        "Obésité modérée",
        "Obésité sévère",
        "Obésité morbide ou massive"
    ]
    f = find_patient(li_patients, numero_dossier)

    if isinstance(f, int):
        imc = li_patients[f][9]

        if imc < 18.5:
            return li_status_imc[0]
        elif 18.5 <= imc < 25:
            return li_status_imc[1]
        elif 25 <= imc < 30:
            return li_status_imc[2]
        elif 30 <= imc < 35:
            return li_status_imc[3]
        elif 35 <= imc < 40:
            return li_status_imc[4]
        else:
            return li_status_imc[5]

    else:
        return None


def menu(marge=30):
    """This function show menu whith a left marge
    :param marge: left marge that print will have
    """
    print(f"{' ':>{marge}}{'1:':3} add_new_doctor".upper(),
          f"{' ':>{marge}}{'2:':3} add_new_patient".upper(),
          f"{' ':>{marge}}{'3:':3} show_doctor".upper(),
          f"{' ':>{marge}}{'4:':3} show_patients".upper(),
          f"{' ':>{marge}}{'5:':3} find patient by him name".upper(),
          f"{' ':>{marge}}{'6:':3} find patient by him code".upper(),
          f"{' ':>{marge}}{'7:':3} nettoyer le terminal".upper(),
          f"{' ':>{marge}}{'8:':3} show patient imc".upper(),
          f"{' ':>{marge}}{'9:':3} save doctor schedule".upper(),
          f"{' ':>{marge}}{'10:':3} find patient by him code".upper(),
          f"{' ':>{marge}}{'11:':3} verify doctor appointment".upper(),
          f"{' ':>{marge}}{'un autre nombre pour quitter':30}".upper(),
          sep="\n")


def nppt(marge=25):
    nom = input(f"{' ':>{marge}}le nom: ").upper()
    postnom = input(f"{' ':>{marge}}le Post-nom: ").upper()
    prenom = input(f"{' ':>{marge}}le Prenom: ").capitalize()
    tel = input(f"{' ':>{marge}}le Tel: ")

    return nom, postnom, prenom, tel


def titre(marge=29):
    print(
        f""
        f"{' ':>{marge-9}} {' DEBUT ':#^50}",
        f"{' ':>{marge}} {'PROGRAMME-DE-GESTION-D-UN-HOPITAL':#^33}",
        f"{' ':>{marge-9}} {' DEBUT ':#^50}",
        sep='\n', end='\n' * 2
    )


def seppep():
    print('\n' * 2)


def main():
    """

    """
    li_doctor = []
    li_patient = []
    # di_patient = {}
    li_complain = []
    li_doctor_shedule = []
    # len_doc, len_pat = len(li_doctor), len(li_patient)
    debut = 0
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
                show_doctor(li_doctor)
                pass

            case 4:
                print(f"{' ':>20} :LISTE DES PATIENTS:\n")
                show_patients(li_patient)     # MUST CHECK::::
                pass

            case 5:
                print(f"{' ':>20} :RECHERCHE DES PATIENTS:\n")
                nom = input("Le nom du Patient: ")
                find_patients(li_patient, nom)
                # pass

            case 6:
                print(f"{' ':>20} :RECHERCHE D'UN PATIENT PRECI:\n")
                numero_dossier = (input("Le numero du dossier: ")).upper()
                find_patient(li_patient, numero_dossier)
                pass

            case 7:
                print(f"{' ':>20} :NETTOYAGE DU TERMINAL:\n")
                clear()
                titre()
                pass

            case 8:
                print(f"{' ':>20} :AFFICHAGE DE L'IMC D'UN PATIENT DONNE:\n")
                numero_dossier = (input("Le numero du dossier: ")).upper()
                show_patient_imc(li_patient, numero_dossier)        # MUST CHECH:::
                pass

            case 9:
                print(f"{' ':>20} :ENREGISTREMENT DE L'HORRAIRE DU MEDCIN:\n")
                matricule = input("Le matricule du medecin: ")
                p_doc = doctor.find_doctor(li_doctor, matricule)      # MUST BE MODIFIED
                if p_doc == 1:
                    save_doctor_schedule(li_doctor_shedule, matricule)
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
