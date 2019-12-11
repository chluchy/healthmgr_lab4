#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
import healthmgr.medmgr.medls as mm
class TestMedLs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up instances of parent class Medication and child class
        Antibiotic for testing. Also set counts of medication to 0
        """
        #print('setupClass')
        cls.med1 = mm.Medication('aspirin', '80mg', 'daily')
        cls.med2 = mm.Antibiotic('amoxicillin', '500mg', 'three times daily', '14 days')
        cls.med3 = mm.Antibiotic('septra', '2 DS', 'two times daily', '7 days')
        cls.med4 = mm.Medication('furosemide', '40mg', 'daily as needed')
        cls.medCount = mm.Medication.count
        cls.abxCount = mm.Antibiotic.count

    @classmethod
    def tearDownClass(cls): #reset 'database' at teardown
        """Reset 'database' of medications at teardown"""
        #print('teardownClass')
        cls.med1 = None
        cls.med2 = None
        cls.med3 = None
        cls.med4 = None
        mm.Medication.count = 0
        mm.Antibiotic.count = 0
    
#     def test_name(self):
#         self.assertEqual(med5 = mm.Medication('a', '80mg', 'daily'), )
#         self.assertEqual(mm.Medication(55, '80mg', 'daily'), )

    def test_counts(self):
        """Test the functions medCount and abxCount from module medmgr"""
        print('test_count_functions')
        self.assertEqual(self.medCount, 4)
        self.assertEqual(self.abxCount, 2)
        self.assertTrue(type(self.medCount) == int)
        self.assertIsInstance(self.medCount, int)
        self.assertEqual(self.med1.medCount(), 'Total number of medications: 4')
        self.assertEqual(self.med2.abxCount(), 'Total number of antibiotics: 2')

    def test_display(self):
        """Test the functions display and displayAll which displays the
        medication name, dose, frequency and duration (for Antibiotic class
        medications only). The display() and displayAll() functions output a
        Pretty Table which are considered objects.
        """
        print('test_display_functions')
        #print(type(self.med1.display()))
        self.assertEqual(self.med1.name, 'aspirin')
        self.assertEqual(self.med3.dose, '2 DS')
        self.assertEqual(self.med4.freq, 'daily as needed')
        self.assertEqual(self.med2.duration, '14 days')
        self.assertIsInstance(self.med2, mm.Antibiotic, msg=None)
        self.assertNotIsInstance(self.med1, mm.Antibiotic, msg=None)
        self.assertIsInstance(self.med2, mm.Medication, msg=None)
        self.assertIsInstance(self.med1.display(), object)
        self.assertIsInstance(self.med3.displayAll(), object)

unittest.main(argv=[''], verbosity=2, exit=False)
