# -*- coding: iso-8859-1 -*-

import datetime as dt
import decimal
import re

decimal.getcontext().prec = 10

class Entry (object) :
    """
    Contient les données nécessaires au calcul d'une ligne du livre de compte.
    """
    def __init__(self, date, mode, label, amount):

        if type (date) is dt.date:
            self.date = date
        else:
            self.date = stringToDate(date)
        self.mode = mode
        self.label = label
        self.amount = decimal.Decimal(amount)
        self.bank = False

    def copy(self):
        """
        Copy the object
        """
        e = Entry(dateToString(self.date), self.mode, self.label,
                  str(self.amount))
        e.bank = self.bank
        return e

    def __str__(self):
        output = u""
        output += dateToString(self.date)
        output +=","+self.mode
        output +=","+self.label
        output +=","+str(self.amount)
        output +=","+str(self.bank)
        return output

    def save(self, f):
        f.write(dateToString(self.date))
        f.write(","+self.mode)
        f.write(","+self.label)
        f.write(","+str(self.amount))
        f.write(","+str(self.bank))

def stringToDate(dateStr) :
    if dateStr == "":
        return dt.date.max
    d = re.split("/", dateStr)
    if len(d) is not 3:
        raise RuntimeError("La date s'écrit jj/mm/aaaa.")

    j = int(d[0])
    m = int(d[1])
    a = int(d[2])

    return dt.date(a, m, j)

def dateToString(date) :
    if date == dt.date.max:
        return ""
    else:
        return ("%2i"%date.day+"/"+"%2i"%date.month+"/"+"%4i"%date.year)
