# -*- coding: iso-8859-1 -*-

import re
from entry import *

class Account (object) :

    def __init__(self, initialAmount = 0):
        self.initialAmount = initialAmount
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
                       self.initialAmount)

    @property
    def bank_balance(self) :
        """
        Compute the balance as reported on the bank statement
        """
        return reduce (lambda x,y: x+y,
                       map(lambda e : e.amount,
                           filter(lambda e:e.bank, self.entries)),
                       self.initialAmount)

    def read(self, filename) :
        """
        Read data in a file
        """
        self.initialAmount = 0
        self.entries = []
        with open(filename, "r") as f :
            # First line
            ln = 1
            line = f.readline()
            splittedLine = re.split("[\t]", line)
            if splittedLine[3] != "Initial amount" :
                print splittedLine
                raise RuntimeError("Error line %i of file %s"%(ln, filename))
            self.initialAmount = decimal.Decimal(splittedLine[4])
            ln += 1
            line = f.readline()
            ln += 1
            while line != "\n" :
                splittedLine = re.split("[\t]", line)
                if len(splittedLine) is not 4:
                    raise RuntimeError ("line %i is invalid."%ln)
                date = splittedLine[0]
                mode = splittedLine[1]
                label = splittedLine[2]
                amount = splittedLine[3]
                e = Entry(date, mode, label, amount)
                self.entries.append(e)
                line = f.readline()
                ln += 1

    def save(self, filename) :
        """
        Write data in a file
        """
        with open("filename", "w") as f :
            f.write(self.__str__())

    def sort (self) :
        """
        Sort entries by increasing dates
        """
        self.entries.sort(self.entries, lambda x,y: cmp(x.date,y.date))

    def __str__(self) :
        self.entries.sort()
        output = 3*"\t"+ "Initial amount\t" +  str(self.initialAmount)+"\n"
        for e in self.entries :
            output += e.__str__() +"\n"
        
        output += "\n"
        output += 3*"\t"+"balance: "+str(self.balance)
        output += "\t"+"bank: "+str(self.bank_balance)
        return output

if __name__ == "__main__":

    a = account(5000)
    a.add_entry("09/07/2010", "CB Florent", "Chronodrive.com", "-83.12")
    a.add_entry("10/07/2010", "CB Aurélie",
                "Crédit Lyonnais Toulouse Montplaisir", "-500")
    a.add_entry("09/07/2010", "CB Aurélie", "Crédit Agricole Toulouse Rangueil",
                "-500")
    a.entries[1].bank = True

    with open("comptes", "w") as f:
        f.write (a.__str__())
