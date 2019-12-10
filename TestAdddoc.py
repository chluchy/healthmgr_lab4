
from healthmgr.doctor import adddoc as ad
import unittest
class TestAdddoc(unittest.TestCase):
    def setUp(self):
        """ create instances of specialist and doctor that can be used in subsequent tests"""
        self.p1=ad.specialist('smith','pediatrics',124,111)
        self.p2=ad.specialist('carter','infectious disease',167,229)
        self.p3=ad.specialist('chen','surgery',155,247)
        self.p4=ad.doctor('jones',230,121)
    def test_add(self):
        """ tests if instances of classes doctor and specialist were properly created"""
        self.assertEqual(self.p1.name,'smith')
        self.assertNotEqual(self.p1.name,'carter')
        self.assertEqual(self.p2.pavail,62)
        self.assertIsInstance(self.p1,ad.doctor)
        self.assertIsInstance(self.p1,ad.specialist)
        self.assertIsInstance(self.p4,ad.doctor)
        self.assertNotIsInstance(self.p4,ad.specialist)
    def test_methods(self):
        """ tests two methods on instances of specialist to see if an individual is accepting new patients right
        and if not, would they like to join a waitlist.  The waitlist is incremented with each request"""
        self.assertEqual(self.p1.newp(),"There's options to join a waitlist")
        self.assertEqual(self.p2.newp(),"Accepting new patients, please call")
        self.assertNotEqual(self.p3.newp(),"There's options to join a waitlist")
        self.assertEqual(self.p1.waitlist(),"You're position 14 on the waitlist, and should be seen in 3.5 months")
        self.assertNotEqual(self.p1.waitlist(),"You're position 14 on the waitlist, and should be seen in 3.5 months")
    def tearDown(self):
        self.p1=None
        self.p2=None
        self.p3=None
        self.p4=None

unittest.main(argv=[''], verbosity=2,exit=False)
