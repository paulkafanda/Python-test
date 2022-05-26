import datetime


def find_doctor(li_doc: list, matricule: str):
    """
    this fonction check if a doctor are or not registered by him matricule
    :param li_doc: list that will contain all doctors information_s
    :param matricule: string that is the doctor's matricule
    """
    mattt = matricule.upper()
    for i in range(len(li_doc)):
        if mattt == li_doc[i][4]:
            return 1
        elif i == len(li_doc) - 1:
            return 0


def load_matricule(li_doctor: list, nom: str, postnom: str):
    """This fonction genered a matricule
    :param li_doctor: list of all doctors
    :param nom: name of the doctor
    :param postnom: sub name of the doctor
    """
    dateact = datetime.datetime.now()
    annee = str(dateact.year)
    place = str(len(li_doctor) + 1)

    return annee[-2:] + (nom[1]).upper() + (postnom[1]).upper() + place.zfill(3)


def add_new_doctor(li_doctor: list, nom: str, postnom: str, prenom: str, tel: str, specialisation: str):
    """

    :param li_doctor: list tof all doctors
    :param nom: name of a doctor ex(KAFANDA)
    :param postnom: sub name of a doctor ex(NDALA)
    :param prenom: first name oex(Paul)
    :param tel: num de tel
    :param specialisation: ex(Pediatre)
    :return: void
    """
    li_doctors = []
    matricule = load_matricule(li_doctor, nom, postnom)

    li_doctors.append(
        [
            nom.upper(),
            postnom.upper(),
            prenom.capitalize(),
            tel,
            matricule.upper(),
            specialisation.upper()
        ]
    )
    return li_doctors[0]
