#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# File medls.py
import sys
from prettytable import PrettyTable


class NameTooSmallError(Exception):
    pass

class Medication:
    """A class for managing medication lists"""
    count = 0
    medList = []
    def __init__(self, name, dose, freq):
        try:
            if len(name) < 2:
                raise NameTooSmallError()
        except NameTooSmallError:
            print('Enter a valid medication name with more than 1 character.')
            sys.exit()
        self.name=name
        self.dose=dose
        self.freq=freq
        Medication.count += 1
        Medication.medList.append([name, dose, freq])

    def medCount(self):
        """Displays the total number of medications"""
        return('Total number of medications: {}'.format(Medication.count))
    def display(self):
        """Displays the name, dose and frequency of the medication"""
        x = PrettyTable()
        x.field_names = ["Medication", "Dose", "Frequency"]
        x.add_row([self.name, self.dose, self.freq])
        return(x)
    def displayAll(self):
        """Displays a list of medications in ASCII format"""
        x = PrettyTable()
        x.field_names = ["Medication", "Dose", "Frequency"]
        for i in range(len(Medication.medList)):
            x.add_row([Medication.medList[i][0], Medication.medList[i][1], Medication.medList[i][2]])
        return(x)

class Antibiotic(Medication):
    """A class for managing antibiotic medications which is a child class of Medication"""
    count = 0
    def __init__(self, name, dose, freq, duration):
        Medication.__init__(self, name, dose, freq)
        self.duration = duration
        Antibiotic.count += 1
    def abxCount(self):
        """Displays the total number of antibiotics"""
        return('Total number of antibiotics: {}'.format(Antibiotic.count))
    def display(self):
        """Displays the name, dose, frequency and duration of the antibiotic"""
        x = PrettyTable()
        x.field_names = ["Antibiotic", "Dose", "Frequency", "Duration"]
        x.add_row([self.name, self.dose, self.freq, self.duration])
        return(x)
