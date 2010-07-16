# -*- coding: iso-8859-1 -*-

import re
from entry import *

class Account (object) :

    def __init__(self):
        self.entries = []

    def add_entry(self, date, mode, label, amount):
        e = Entry(date, mode, label, amount)
        self.entries.append(e)

    @property
    def balance(self):
        """
        Compute the balance by adding values of each entry
        """
        return reduce (lambda x,y: x+y,
                       map(lambda e : e.amount, self.entries),
                       0)

    @property
    def bank_balance(self) :
        """
        Compute the balance as reported on the bank statement
        """
        return reduce (lambda x,y: x+y,
                       map(lambda e : e.amount,
                           filter(lambda e:e.bank, self.entries)),
                       0)

    def read(self, filename) :
        """
        Read data in a file
        """
        self.entries = []
        ln = 0
        with open(filename, "r") as f :
            line = f.readline()
            ln += 1
            while line != "\n" :
                splittedLine = re.split("[\t]", line)
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
        with open(filename, "w") as f :
            f.write(str(self))

    def sort (self) :
        """
        Sort entries by increasing dates
        """
        self.entries.sort(lambda x,y: cmp(x.date,y.date))

    def __str__(self) :
        output = ""
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
    a.add_entry("10/07/2010", "CB Aurélie",
                "Crédit Lyonnais Toulouse Montplaisir", "-500")
    a.add_entry("09/07/2010", "CB Aurélie", "Crédit Agricole Toulouse Rangueil",
                "-500")
    a.entries[0].bank = True
    a.entries[1].bank = True

    a.sort()
    with open("test-comptes.cpt", "w") as f:
        f.write (str(a))
