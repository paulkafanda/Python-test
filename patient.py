import datetime
from main import seppep


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
    for i in range(len(li_patients)):
        if mattt == li_patients[i][8]:
            return i

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
