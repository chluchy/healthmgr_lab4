#!/usr/bin/env python
# coding: utf-8

# In[6]:


import unittest
from TestAdddoc import TestAdddoc
from TestDoctordb import TestDrdb
from testinsdose_mod import TestInsDose
from testmedmgr_mod import TestMedLs
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestAdddoc))
    suite.addTest(unittest.makeSuite(TestDrdb))
    suite.addTest(unittest.makeSuite(TestInsDose))
    suite.addTest(unittest.makeSuite(TestMedLs))
    runner=unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()


# In[4]:





# In[ ]:




