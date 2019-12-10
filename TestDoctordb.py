#import pandas as pd
from healthmgr.doctor import adddoc as ad
from healthmgr.doctor import doctordb as drdb
import unittest
class TestDrdb(unittest.TestCase):
    def setUp(self):
        """ Adds instances of specialist that can be passed into the dataframe functions.  Next
        creates and empty dataframe and adds the instances of specialist to it """
        self.p1=ad.specialist('smith','pediatrics',124,111)
        self.p2=ad.specialist('carter','infectious disease',167,229)
        self.p3=ad.specialist('chen','surgery',155,247)
        self.df=pd.DataFrame(columns=['name','specialty','patients','max_patients'])
        self.df=drdb.db_entry(self.df,self.p1)
        self.df=drdb.db_entry(self.df,self.p2)
        self.df=drdb.db_entry(self.df,self.p3)
    def test_entry(self):
        """ tests to see if the instances of specialist were successfully added to the dataframe"""
        self.assertEqual('smith',self.df.name[0])
        self.assertEqual('pediatrics',self.df.specialty[0])
        self.assertEqual(124,self.df.patients[0])
        self.assertEqual('carter',self.df.name[1])
        self.assertNotEqual('chen',self.df.name[1])
        self.assertEqual(247,self.df.max_patients[2])
    def test_search(self):
        """ queries the dataframe to see if doctors match a given specialty """
        self.assertEqual(drdb.doc_search(self.df,'surgery'),'Doctors matching that specialty include: chen')
        self.assertEqual(drdb.doc_search(self.df,'pediatrics'),'Doctors matching that specialty include: smith')
        self.assertEqual(drdb.doc_search(self.df,'infectious disease'),'Doctors matching that specialty include: carter')
        self.assertEqual(drdb.doc_search(self.df,'nephrology'),'Sorry, there are no doctors with that specialty')
        self.assertEqual(drdb.doc_search(self.df,'opthamology'),'Sorry, there are no doctors with that specialty')
    def tearDown(self):
        self.df=None
        self.p1=None
        self.p2=None
        self.p3=None
unittest.main(argv=[''], verbosity=2,exit=False)


# In[ ]:
