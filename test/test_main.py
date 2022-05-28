from unittest import TestCase
import main


class Test(TestCase):
    def test_find_patient_npp(self):
        self.li_patients = [['KABULO', 'ILUNGA', 'Serge']]
        i = main.find_patient_npp(self.li_patients, 'KABULO', 'ILUNGA', 'Serge')
        if isinstance(i, int):
            pass
            # statself.fail()
        else:
            raise TypeError

    def test_save_complaints(self):
        self.li_patitients = [
            ['KABULO', 'ILUNGA', 'Serge', '0990983055', 80, 1.8, 'F', 20, 'FKIS22001', 24.55],
            ['KABONGO', 'MUKENI', 'Sabin', '0990983055', 80, 1.8, 'M', 20, 'MKMS22002', 24.55]
        ]
        li_complain = [['FKIS22001', 'malaria'], ['MKMS22002', 'maux de ventre']]
        i = main.save_complaints(self.li_patitients, li_complain, 'MKMS22002', 'typhoide')
        if i == 0:
            self.fail("FATAL ERROR")
        else:
            pass
            # print(self.li_patitients)
            # print(li_complain)
