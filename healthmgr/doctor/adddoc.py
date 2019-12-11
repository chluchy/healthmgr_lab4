#!/usr/bin/env python
# coding: utf-8

# In[24]:

class NegativeError(Exception):
    pass
class NoWaitList(Exception):
    pass
class LongWaitList(Exception):
    pass


class doctor:
    """ Create an instance of doctor with parameters name, current patients and max patients"""
    def __init__(self,name,pcurr,pmax):
        try:
            if int(pcurr)<0 or int(pmax)<0:
                raise NegativeError()
            int(pcurr)
            int(pmax)
            self.name=name
            self.pcurr=pcurr
            self.pmax=pmax
            self.pavail=int(self.pmax)-int(self.pcurr) # calculates spots available for new patients
        except ValueError:
            print ("Please enter numbers for both current patients and max patients")
        except NegativeError:
            print ("Patient counts must be greater than zero")


class specialist(doctor):
    """Create an instance of a specialist with inherited class of doctor and additional methods"""
    def __init__(self,name,spec,pcurr,pmax):
        doctor.__init__(self,name,pcurr,pmax)
        self.spec=spec
    def newp(self): # method to add a patient
        if self.pavail > 0:
            self.pcurr += 1
            return("Accepting new patients, please call")
        else:
            return("There's options to join a waitlist")
    def waitlist(self): # method to add a patient willing to be on the wait list
        try:
            self.pcurr += 1
            wl_spot = self.pcurr - self.pmax
            if wl_spot <0:
                raise NoWaitList()
            new_p_permonth = 4
            wait_time = wl_spot/new_p_permonth
            if wait_time > 12:
                raise LongWaitList()
            return ("You're position {} on the waitlist, and should be seen in {} months".format(wl_spot,wait_time))
        except NoWaitList:
            return('There is no wait list, call to book an appointment')
        except LongWaitList:
            return('The wait list is longer than a year, we are no longer accepting new patients')
