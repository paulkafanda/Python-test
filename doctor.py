import datetime
# from main import seppep


def seppep():
    print('\n' * 2)


def find_doctor(li_doc: list, matricule: str):
    """
    this fonction check if a doctor are or not registered by him matricule
    :param li_doc: list that will contain all doctors information_s
    :param matricule: string that is the doctor's matricule\n

    :return: int position of doctor in li_doc
    :return: None if not found
    """
    mattt = matricule.upper()
    for i in range(len(li_doc)):
        if mattt == li_doc[i][4]:
            return i

    return None


def load_matricule(li_doctor: list, nom: str, postnom: str):
    """This fonction genered a matricule
    :param li_doctor: list of all doctors
    :param nom: name of the doctor
    :param postnom: sub name of the doctor
    """
    dateact = datetime.datetime.now()
    annee = str(dateact.year)
    place = str(len(li_doctor) + 1)

    return annee[-2:] + (nom[0]).upper() + (postnom[0]).upper() + place.zfill(3)


def find_doctor_npp(li_doctors, nom, postnom, prenom):
    for i in range(len(li_doctors)):
        if nom == li_doctors[i][0] and postnom == li_doctors[i][1] and prenom == li_doctors[i][2]:
            return i

    return None


def add_new_doctor(li_doctors: list, nom: str, postnom: str, prenom: str, tel: str, specialisation: str):
    """

    :param li_doctors: list tof all doctors
    :param nom: name of a doctor ex(KAFANDA)
    :param postnom: sub name of a doctor ex(NDALA)
    :param prenom: first name oex(Paul)
    :param tel: num de tel
    :param specialisation: ex(Pediatre)
    :return: void
    """
    nom = nom.upper()
    postnom = postnom.upper()
    prenom = prenom.capitalize()
    specialisation = specialisation.upper()

    # li_doctors = []
    i = find_doctor_npp(li_doctors, nom, postnom, prenom)
    if isinstance(i, int):
        li_doctors[i][3] = tel
        li_doctors[i][5] = specialisation
        pass
    else:
        matricule = load_matricule(li_doctors, nom, postnom)
        li_doctors.append(
            [
                nom,
                postnom,
                prenom,
                tel,
                matricule,
                specialisation
            ]
        )


def show_doctor(li_doctors):
    if len(li_doctors) == 0:
        return None
    else:
        for i in range(len(li_doctors)):
            print(
                f"{li_doctors[i][0]:10} "
                f"{li_doctors[i][1]:7} "
                f"{li_doctors[i][2]:7} "
                f"{li_doctors[i][3]:10} "
                f"{li_doctors[i][4]:7} "
                f"{li_doctors[i][5]:4} "
            )
    seppep()
    pass


def save_doctor_schedule(li_doctor_shedules: list, matricule: str, horaire: str):
    """
    Cette fonction gere l'agenda de tout les medecin de l'hopital
    En generale elle modifie li_doctor_schidules
    """
    # oui elle fait beaucoup trop de chose :)
    li_jour = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"]

    # menu_day()        MUST USE IN MAIN

    # Si la choix est vide l'on doit reentrer une valeur
    # si choix contient 1 car on essaie de le convertir en entier
    # puis on ajoute dans li_doctor_shedule, le jour qui porte cet indice dans li_jour

    if len(horaire) == 1:
        jour_p = int(horaire)
        li_doctor_shedules.append([matricule, li_jour[jour_p]])

    # On ajoute ce jour
    # li_doctor_shedule.append([li_jour[jour_p]])
    elif len(horaire) == 3:
        if horaire[1] == ';':
            jour_p_1 = int(horaire[0])
            jour_p_2 = int(horaire[-1])
            li_doctor_shedules.append([matricule, li_jour[jour_p_1], li_jour[jour_p_2]])

        elif horaire[1] == ':':

            jour_p_1 = int(horaire[0])
            jour_p_2 = int(horaire[-1])
            li_doctor_shedule_temp = [matricule]

            if jour_p_1 < jour_p_2:
                for i in range(jour_p_1, jour_p_2+1):
                    li_doctor_shedule_temp.append(li_jour[i])
                li_doctor_shedules.append(li_doctor_shedule_temp)

            else:
                for i in range(jour_p_2, jour_p_1 + 1):
                    li_doctor_shedule_temp.append(li_jour[i])
                li_doctor_shedules.append(li_doctor_shedule_temp)

    elif 3 < len(horaire) <= 13:
        li_val = []
        li_jours = []

        for i in range(len(horaire)):
            if i % 2 == 0:
                val = int(horaire[i])
                li_val.append(val)
        li_val_c = []

        for i in li_val:
            if i in li_val_c:
                pass
            else:
                li_val_c.append(i)

        li_val_c.sort()
        for i in li_val_c:
            li_jours.append(li_jour[i])
        li_doctor_shedules.append(li_jours)
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


def doctor_appointment(li_doctors, li_doctor_schedules, matricule):
    # print(li_doctor_schedules)
    p_doc = find_doctor(li_doctors, matricule)      # must be modified
    if isinstance(p_doc, int):
        work = doctor_schedule(li_doctors, li_doctor_schedules, matricule)
        # print(work)
        if isinstance(work, list):
            return work

    else:
        return None
