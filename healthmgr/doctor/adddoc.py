#!/usr/bin/env python
# coding: utf-8

# In[24]:


class doctor:
    """ Create an instance of doctor with parameters name, current patients and max patients"""
    def __init__(self,name,pcurr,pmax):
        self.name=name
        self.pcurr=pcurr
        self.pmax=pmax
        self.pavail=int(self.pmax)-int(self.pcurr) # calculates spots available for new patients

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
        self.pcurr += 1
        wl_spot = self.pcurr - self.pmax
        new_p_permonth = 4
        wait_time = wl_spot/new_p_permonth
        return ("You're position {} on the waitlist, and should be seen in {} months".format(wl_spot,wait_time))
