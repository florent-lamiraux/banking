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
        
        # Parse date string into a datetime.date object
        d = re.split("/", date)
        if len(d) is not 3:
            raise RuntimeError("La date s'écrit jj/mm/aaaa.")
        
        j = int(d[0])
        m = int(d[1])
        a = int(d[2])

        self.date = dt.date(a, m, j)
        self.mode = mode
        self.label = label
        self.amount = decimal.Decimal(amount)
        self.bank = False

    def __str__(self):
        d = self.date
        output = "%2i"%d.day+"/"+"%2i"%d.month+"/"+"%4i"%d.year
        output +="\t"+self.mode+"\t"+self.label+"\t"+str(self.amount)
        output +="\t"+str(self.bank)
        return output
