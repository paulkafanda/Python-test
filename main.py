import datetime, os

li_doctor = [["Mathieu", "Dan", "Du bois", "0906340486", "G1752/-", "pediatre"]]
li_patient = []
len_doc, len_pat = len(li_doctor), len(li_patient)


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
    save_complaints(numero_dossier)
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
        print(i+1, " ".join(li_patient[i]))
    pass


def show_doctor():
    for i in range(len(li_doctor)):
        print(i+1, " ".join(li_doctor[i]))
    pass


def save_complaints(num_dossier):
    di_patient = {}
    plainte = input("la Plainte: ")
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


def main():
    pass
