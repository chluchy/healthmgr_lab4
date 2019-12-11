#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# File insdose.py
import sys

class NegNumError(Exception):
    pass

def bbdosing(kg):
    """Function to estimate the total daily insulin dose and the basal insulin dose based on weight in kg."""
    
    try:
        if kg <= 0:
            raise ValueError()
        total = round(kg * 0.5, 1)
        basal = round(total * 0.4, 1)
        bolus = round(total * 0.6, 1)
    except ValueError:
        return('Please enter a positive number greater than 0.')
    except TypeError:
        return('Please enter a number.')
#     except:
#         return(sys.exc_info(),"occurred.")
    else:
        return('''Based on your weight in kg:
    Your estimated total daily insulin dose is {} units.
    Your estimated daily dose for basal insulin is {} units.
    Your estimated daily dose for bolus insulin is {} units.
    Generally, bolus insulin is divided evenly between meals.'''.format(total, basal, bolus))

# 500 ÷ Total Daily Insulin Dose = 1 unit insulin covers so many grams of carbohydrate
def carbratio(tdi):
    """Uses the "Rule of 500" to estimate the insulin to carbohydrate ratio using the total daily insulin dose."""
    try:
        if tdi < 0:
            raise NegNumError()        
        r = round(500/tdi,1)
    except NegNumError:
        return('Please enter a positive number greater than 0.')
    except ZeroDivisionError:
        return('Please enter a positive number greater than 0.')
    except TypeError:
        return('Please enter a number.')
    else:
        return('Based on your daily insulin requirement, your estimated insulin to carb ratio is {}, meaning that 1 unit of rapid acting insulin will cover {} g of carbohydrates.'.format(r, r))

# Correction Factor/Dose = 100 divided by the Total Daily Insulin Dose (TDI) = 1 unit of insulin will reduce the blood sugar so many mmol/l
def cfact(tdi):
    """Uses the "100 Rule for Rapid Acting Insulin" to estimate the correction factor/dose of insulin."""
    try:
        if tdi < 0:
            raise NegNumError()
        f = round(100/tdi, 1)
    except NegNumError:
        return('Please enter a positive number greater than 0.')
    except ZeroDivisionError:
        return('Please enter a positive number greater than 0.')
    except TypeError:
        return('Please enter a number.')
    else:
        return('Your correction factor/dose is {}, meaning that 1 unit of rapid acting insulin will decrease your blood sugar by {} mmol/l.'.format(f, f))

# Carbohydrate coverage at a meal = Total grams of CHO in the meal ÷ grams of CHO disposed by 1 unit of insulin (gcarb)
def carbcorr(carb, ratio):
    """Estimates the carbohydrate correction dose based on the number of carbohydrates to be consumed in grams and the known insulin to carbohydrate ratio."""
    try:
        if ratio < 0 or carb < 0:
            raise NegNumError()
        corr = carb/ratio
    except NegNumError:
        return('Please enter only positive numbers greater than 0 as inputs.')
    except ZeroDivisionError:
        return('Please enter a positive number greater than 0 for the insulin to carboydrate ratio.')
    except TypeError:
        return('Please enter only numbers as inputs.')
    else:    
        return('Your carbohydrate correction dose is {}.'.format(corr))
