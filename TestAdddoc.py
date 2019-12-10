from healthmgr.doctor import adddoc as ad
import unittest
class TestAdddoc(unittest.TestCase):
    def setUp(self):
        self.p1=ad.specialist('smith','pediatrics',124,111)
        self.p2=ad.specialist('carter','infectious disease',167,229)
        self.p3=ad.specialist('chen','surgery',155,247)
        self.p4=ad.doctor('jones',230,121)
        self.p5=ad.doctor('johnson',5,-5)
        self.p6=ad.doctor('hluchy',5,'dog')
        self.p7=ad.specialist('bortles','pediatrics',500,2)
    def test_add(self):
        self.assertEqual(self.p1.name,'smith')
        self.assertNotEqual(self.p1.name,'carter')
        self.assertEqual(self.p2.pavail,62)
        self.assertIsInstance(self.p1,ad.doctor)
        self.assertIsInstance(self.p1,ad.specialist)
        self.assertIsInstance(self.p4,ad.doctor)
        self.assertNotIsInstance(self.p4,ad.specialist)
        self.assertNotIsInstance(self.p5,ad.specialist)
        self.assertNotIsInstance(self.p6,ad.specialist)
    def test_methods(self):
        self.assertEqual(self.p1.newp(),"There's options to join a waitlist")
        self.assertEqual(self.p2.newp(),"Accepting new patients, please call")
        self.assertNotEqual(self.p3.newp(),"There's options to join a waitlist")
        self.assertEqual(self.p1.waitlist(),"You're position 14 on the waitlist, and should be seen in 3.5 months")
        self.assertNotEqual(self.p1.waitlist(),"You're position 14 on the waitlist, and should be seen in 3.5 months")
        self.assertEqual(self.p2.waitlist(),'There is no wait list, call to book an appointment')
        self.assertEqual(self.p7.waitlist(),'The wait list is longer than a year, we are no longer accepting new patients')
    def tearDown(self):
        self.p1=None
        self.p2=None
        self.p3=None
        self.p4=None

unittest.main(argv=[''], verbosity=2,exit=False)
