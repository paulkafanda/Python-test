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
    li_doctors = []
    dateact = datetime.datetime.now()
    annee = str(dateact.year)
    place = str(len(li_doctor) + 1)
    matricule = annee[-2:] + (nom[1]).upper() + (postnom[1]).upper() + place.zfill(3)

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
    return li_doctors[0][:]
