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
        output = dateToString(self.date)
        output +="\t"+self.mode
        output +="\t"+self.label
        output +="\t"+str(self.amount)
        output +="\t"+str(self.bank)
        return output

    def save(self, f):
        f.write(dateToString(self.date))
        f.write("\t"+self.mode)
        f.write("\t"+self.label)
        f.write("\t"+str(self.amount))
        f.write("\t"+str(self.bank))

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
