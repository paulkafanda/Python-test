

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
