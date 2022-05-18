import datetime

li_doctor = [["Mathieu", "Dan", "Du bois", "0906340486", "G1752/-", "pediatre"]]
li_patient = []


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
    pass


def find_patients(nom):

    pass


def find_patient(numero_dossier):
    pass


def show_patients():
    pass


def show_doctor():
    pass


def save_complaints(complaints):
    pass


def save_doctor_schedule():
    pass


def doctor_appointement():
    pass


def show_patient_complaints(numero_dossier):
    pass


def show_patient_imc(patient):
    pass


def main():
    pass
