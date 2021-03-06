# -*- coding: iso-8859-1 -*-

import re
from entry import *
import codecs
import datetime as dt

def bankOrder(e1, e2):
    """
    Sort entries as on bank statement
    """
    modeOrder = {u'CB Florent':0, u'e-CB':0, u'CB Aur�lie':1}
    if e1.bank and e2.bank:
        return 0

    if not e1.bank and e2.bank:
        return 1

    if e1.bank and not e2.bank:
        return -1

    # if both entries are not on previous statement, sort by date
    # Sort by date
    return cmp(e1.date, e2.date)

class Account (object) :

    def __init__(self):
        self.entries = []

    def add_entry(self, date, mode, label, amount):
        e = Entry(date, mode, label, amount)
        self.entries.append(e)

    def balance(self, date = dt.date.max):
        """
        Compute the balance by adding values of each entry before a given date.
        """
        total = 0
        for e in self.entries:
            if e.date <= date:
                total += e.amount
        return total

    @property
    def bank_balance(self) :
        """
        Compute the balance as reported on the bank statement
        """
        total = 0
        for e in self.entries:
            if e.bank:
                total += e.amount
        return total

    def read(self, filename) :
        """
        Read data in a file
        """
        self.entries = []
        ln = 0
        with codecs.open(filename, 'r', encoding='utf-8') as f :
            line = f.readline()
            ln += 1
            while line != "\n" :
                splittedLine = re.split("[,]", line)
                if len(splittedLine) != 5:
                    raise RuntimeError ("line %i is invalid."%ln)
                date = splittedLine[0]
                mode = splittedLine[1]
                label = splittedLine[2]
                amount = splittedLine[3]
                bank = splittedLine[4]
                e = Entry(date, mode, label, amount)
                if bank == "True\n" :
                    e.bank = True
                self.entries.append(e)
                line = f.readline()
                ln += 1

    def save(self, filename) :
        """
        Write data in a file
        """
        with codecs.open(filename, 'w', encoding='utf-8') as f :
            for e in self.entries :
                e.save(f)
                f.write('\n')

            f.write( "\n")
            f.write( 3*"\t"+"balance: "+str(self.balance()))
            f.write( "\t"+"bank: "+str(self.bank_balance))

    def search(self, expr, entries, field = 'label') :
        """
        Return the list of entries the field of which contains an expression.
        """
        # If expr is lower case, search is case insensitive
        if expr.lower() == expr:
            def lower(s):
                return s.lower()
        else:
            def lower(s) :
                return s

        result = []
        for e in entries:
            if re.search(expr, lower(e.__dict__[field])):
                result.append(e)
        return result

    def sort (self) :
        """
        Sort entries by increasing dates
        """
        self.entries.sort(key = lambda e:e.date)

    def __str__(self) :
        output = u""
        for e in self.entries :
            output += str(e) +"\n"

        output += "\n"
        output += 3*"\t"+"balance: "+str(self.balance)
        output += "\t"+"bank: "+str(self.bank_balance)
        return output

if __name__ == "__main__":

    a = Account()
    a.add_entry("01/07/2010", "Sans objet", "Montant initial", "5000")
    a.add_entry("09/07/2010", "CB Florent", "Chronodrive.com", "-83.12")
    a.add_entry("10/07/2010", u"CB Aur�lie",
                u"Cr�dit Lyonnais Toulouse Montplaisir", "-500")
    a.add_entry("09/07/2010", u"CB Aur�lie", u"Cr�dit Agricole Toulouse Rangueil",
                "-500")
    a.entries[0].bank = True
    a.entries[1].bank = True

    a.sort()
    a.save('test-comptes.cpt')
