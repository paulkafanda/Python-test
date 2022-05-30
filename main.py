import os
import patient
import doctor

# from rich.console import Console


# fonction anonyme qui nettoye le terminal
# clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')





def menu_day(marge=30):     # MUST CHECK:::
    print(
        f"{'':>{marge}} {'0: LUNDI'}",
        f"{'':>{marge}} {'1: MARDI'}",
        f"{'':>{marge}} {'2: MERCREDI'}",
        f"{'':>{marge}} {'3: JEUDI'}",
        f"{'':>{marge}} {'4: VENDREDI'}",
        f"{'':>{marge}} {'5: SAMEDI'}",
        f"{'':>{marge}} {'6: DIMANCHE'}",
        sep='\n', end='\n'*2
    )
















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
          f"{' ':>{marge}}{'10:':3} save patient complaints".upper(),
          f"{' ':>{marge}}{'11:':3} verify doctor appointment".upper(),
          f"{' ':>{marge}}{'12:':3} show patient imc".upper(),
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
    # debut = 0
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
                # doc = \
                doctor.add_new_doctor(li_doctor, nom, postnom, prenom, tel, specialisation)
                # li_doctor.append(doc)
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

                # k = patient.find_patient_npp(li_patient, nom, postnom, prenom)
                # n_p =
                patient.add_new_patient(li_patient, nom, postnom, prenom, tel, poids, taille, genre, age)
                # print(n_p)
                """if isinstance(k, int):
                    for i in range(4, 9):
                        li_patient[k][i] = n_p[i]
                else:
                    li_patient.append(n_p)
                # 2patient.add_new_patient(li_doctor, nom, postnom, prenom, tel, poids, taille, genre, age)
                pass"""
            case 3:
                print(f"{' ':>30} :LISTES DES DOCTEURS:\n")
                if len(li_doctor) == 0:
                    print("Pas encore de Docteur")
                else:
                    doctor.show_doctor(li_doctor)
                pass

            case 4:
                print(f"{' ':>20} :LISTE DES PATIENTS:\n")
                if len(li_patient) == 0:
                    print("Pas encore de Patient!")
                else:
                    patient.show_patients(li_patient)     # MUST CHECK::::
                pass

            case 5:
                print(f"{' ':>20} :RECHERCHE DES PATIENTS:\n")
                nom = input("Le nom | Post-nom | Prenom du Patient: ")
                p = patient.find_patients(li_patient, nom)
                if isinstance(p, list):
                    print(p)
                elif isinstance(p, int):
                    print("Not find!")
                else:
                    print("No Info!")
                # pass

            case 6:
                print(f"{' ':>20} :RECHERCHE D'UN PATIENT PRECI:\n")
                numero_dossier = (input("Le numero du dossier: ")).upper()
                p = patient.find_patient(li_patient, numero_dossier)
                if isinstance(p, int):
                    print(li_patient[p])
                else:
                    print("No info!")

            case 7:
                print(f"{' ':>20} :NETTOYAGE DU TERMINAL:\n")
                clear()
                titre()
                pass

            case 8:
                print(f"{' ':>20} :AFFICHAGE DE L'IMC D'UN PATIENT DONNE:\n")
                numero_dossier = (input("Le numero du dossier: ")).upper()
                imc = patient.show_patient_imc(li_patient, numero_dossier)        # MUST CHECH:::
                if isinstance(imc, str):
                    print(imc)
                else:
                    print("No info!")
                pass

            case 9:
                print(f"{' ':>20} :ENREGISTREMENT DE L'HORRAIRE DU MEDCIN:\n")
                matricule = input("Le matricule du medecin: ")
                p_doc = doctor.find_doctor(li_doctor, matricule)      # MUST BE MODIFIED

                # Si le medecin existe
                if isinstance(p_doc, int):
                    # Affichage de la liste des jours
                    menu_day()

                    while 1:
                        horaire = input(
                            "Choisissez un jour ex:1 pour Mardi\n"
                            "Ou des jours ex: 2;3 pour Mecredi et Jeudi\n"
                            "Ou encore une plage de jours ex: 0:6 pour les jours compris entre Lundi & Dimanche"
                        )
                        while len(horaire) == 0:
                            horaire = input("Saisi invalide\nReasseyez: ")

                        if len(horaire) == 1:
                            try:
                                int(horaire)
                            except ValueError:
                                print("Valeur invalide!")
                                # choix = input()
                            else:
                                doctor.save_doctor_schedule(li_doctor_shedule, matricule, horaire)
                                break
                        # Si la longueur est de 3 car
                        elif len(horaire) == 3:
                            if horaire[1] == ';':
                                try:
                                    int(horaire[0])
                                    int(horaire[-1])
                                    # break
                                except ValueError:
                                    print("Valeur invalid!")
                                else:
                                    doctor.save_doctor_schedule(li_doctor_shedule, matricule, horaire)
                                    break

                            elif horaire[1] == '-':
                                try:
                                    int(horaire[0])
                                    int(horaire[-1])
                                except ValueError:
                                    print("Valeur invalid!")
                                else:
                                    doctor.save_doctor_schedule(li_doctor_shedule, matricule, horaire)
                                    break
                            else:
                                print("Mauvais separateur")
                        # ::
                        elif 3 < len(horaire) <= 13:
                            li_val = []
                            li_jours = []
                            val = 0
                            ok_s, ok_v = 0, 0
                            # print(f"la longeure de choix est de: {len(horaire)}")
                            for i in range(len(horaire)):
                                if i % 2 != 0 and i != 0:
                                    if horaire[i] != ';':
                                        # print(f"238 {choix[i]}")
                                        print("Mauvais separateur!")
                                        ok_s = 0
                                    else:
                                        ok_s = 1
                                elif i % 2 == 0:
                                    try:
                                        int(horaire[i])
                                    except ValueError:
                                        print("Valeur invalide!")
                                        ok_v = 0
                                    else:
                                        ok_s = 1
                            if ok_s == 1 and ok_v == 1:
                                doctor.save_doctor_schedule(li_doctor_shedule, matricule, horaire)
                            break
                else:
                    print(f"{' ':>20}Docteur introuvable!\n")

                pass
            case 10:

                pass

            case 11:
                print(f"{' ':>20} :AFFICHAGE DE L'AGENDA DU MEDECIN:\n")
                matricule = (input("Le matricule du Medecin: ")).upper()
                doctor.doctor_appointment(li_doctor, li_doctor_shedule, matricule)
                pass

            case _:
                # Quitter le Programme
                clear()
                print(f"\n{' ':>20} {' FIN ':#^50}")
                break
    pass


if __name__ == '__main__':
    main()
