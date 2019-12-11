#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from healthmgr.medmgr.insdose import *

class TestInsDose(unittest.TestCase):
    def test_bbdosing(self):
        """ Test of bbdosing function to make sure the right output of
        total/basal/bolus insulin doses are obtained depending on the input
        weight. 
        """

        #print('bbdosing_test')
        self.assertEqual(bbdosing(60), '''Based on your weight in kg:
    Your estimated total daily insulin dose is 30.0 units.
    Your estimated daily dose for basal insulin is 12.0 units.
    Your estimated daily dose for bolus insulin is 18.0 units.
    Generally, bolus insulin is divided evenly between meals.''')
        self.assertEqual(bbdosing(75), '''Based on your weight in kg:
    Your estimated total daily insulin dose is 37.5 units.
    Your estimated daily dose for basal insulin is 15.0 units.
    Your estimated daily dose for bolus insulin is 22.5 units.
    Generally, bolus insulin is divided evenly between meals.''')
        self.assertEqual(bbdosing(80), '''Based on your weight in kg:
    Your estimated total daily insulin dose is 40.0 units.
    Your estimated daily dose for basal insulin is 16.0 units.
    Your estimated daily dose for bolus insulin is 24.0 units.
    Generally, bolus insulin is divided evenly between meals.''')
        self.assertEqual(bbdosing(-5), 'Please enter a positive number greater than 0.')
        self.assertEqual(bbdosing(0), 'Please enter a positive number greater than 0.')
        self.assertEqual(bbdosing('sam'), 'Please enter a number.')


    def test_carbratio(self):
        """ Test of carbratio function which calculates the insulin to carb
        ratio based on input total daily insulin dose. 
        """
        
        #print('carbratio_test')
        self.assertEqual(carbratio(40), 'Based on your daily insulin requirement, your estimated insulin to carb ratio is 12.5, meaning that 1 unit of rapid acting insulin will cover 12.5 g of carbohydrates.')
        self.assertEqual(carbratio(48), 'Based on your daily insulin requirement, your estimated insulin to carb ratio is 10.4, meaning that 1 unit of rapid acting insulin will cover 10.4 g of carbohydrates.')
        self.assertEqual(carbratio(-8), 'Please enter a positive number greater than 0.')
        self.assertEqual(carbratio(0), 'Please enter a positive number greater than 0.')
        self.assertEqual(carbratio('sam'), 'Please enter a number.') 

     
    def test_cfact(self):
        """ Test of cfact function which calculates the correction factor based
        on input total daily insulin dose. Test also deals with errors including 
        ValueErrors and ZeroDivisionErrors
        """
        #print('cfact_test')
        self.assertEqual(cfact(40), 'Your correction factor/dose is 2.5, meaning that 1 unit of rapid acting insulin will decrease your blood sugar by 2.5 mmol/l.')
        self.assertEqual(cfact(48), 'Your correction factor/dose is 2.1, meaning that 1 unit of rapid acting insulin will decrease your blood sugar by 2.1 mmol/l.')
        self.assertEqual(cfact(-8), 'Please enter a positive number greater than 0.')
        self.assertEqual(cfact(0), 'Please enter a positive number greater than 0.')
        self.assertEqual(cfact('sam'), 'Please enter a number.') 

            
    def test_carbcorr(self):
        """ Test of carbcorr function which calculates the carb correction dose
        based 2 inputs: carbratio and the total daily insulin dose. Inputs can
        can only be positive numbers. Test deals errors including ValueErrors
        and ZeroDivisionErrors.
        """
        #print('carbcorr_test')
        self.assertEqual(carbcorr(60, 10), 'Your carbohydrate correction dose is 6.0.')
        self.assertEqual(carbcorr(60, 12.5), 'Your carbohydrate correction dose is 4.8.')
        self.assertEqual(carbcorr(-8, 10), 'Please enter only positive numbers greater than 0 as inputs.')
        self.assertEqual(carbcorr(60, -5), 'Please enter only positive numbers greater than 0 as inputs.')
        self.assertEqual(carbcorr(-60, -5), 'Please enter only positive numbers greater than 0 as inputs.')
        self.assertEqual(carbcorr(60, 0), 'Please enter a positive number greater than 0 for the insulin to carboydrate ratio.')
        self.assertEqual(carbcorr('sam', 10), 'Please enter only numbers as inputs.')
        self.assertEqual(carbcorr(60, 'sam'), 'Please enter only numbers as inputs.')
        self.assertEqual(carbcorr('bob', 'sam'), 'Please enter only numbers as inputs.')
#         with self.assertRaises(NegNumError):
#             carbcorr(60, -8)
#             carbcorr(0, 10)
#             carbcorr(-60, 10)
#         with self.assertRaises(ZeroDivisionError):
#             carbcorr(60, 0)      
unittest.main(argv=[''], verbosity=2, exit=False)
