# CS342 Final Project #2
# Ezgi Cakir
# Template Design Method for Doctors and Nurses

from abc import ABC, abstractmethod


class HealthProfessional(ABC):
    def patient_procedures(self, label):
        self.id = label
        self.wear_mask()
        # self.sanitize_hands()
        self.read_patient_file()
        self.diagnosis()
        self.care_samples()
        self.prescription()

    def wear_mask(self):
        print(self.id + " wears a mask.")

    # def sanitize_mask(self):
    #     print(self.id + " sanitizes the hands.")

    def read_patient_file(self):
        print(self.id + " reads the patient file.")

    @abstractmethod
    def diagnosis(self):
        pass

    @abstractmethod
    def care_samples(self):
        pass

    @abstractmethod
    def prescription(self):
        pass


class Doctor(HealthProfessional):
    def diagnosis(self):
        print("Diagnoses the patient according to symptoms.")

    def care_samples(self):
        print("Directs patient to the relevant units of the hospital for samples to be taken.")

    def prescription(self):
        print("Writes the prescription for the diagnosis.\n")


class Nurse(HealthProfessional):
    def diagnosis(self):
        print("Supports the treatment based on doctor's diagnosis.")

    def care_samples(self):
        print("Takes blood samples to be tested.")

    def prescription(self):
        print("Explains the drugs on the prescription for the treatment.\n")


def main():
    doc = Doctor()
    nurse = Nurse()
    doc.patient_procedures("Doctor")
    nurse.patient_procedures("Nurse")


if __name__ == "__main__":
    main()