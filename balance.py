#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import argparse
from account import Account
from entry import stringToDate

parser = argparse.ArgumentParser(description='Compute balance at given date')
parser.add_argument ('--date', type=str)
parser.add_argument ('--filename', type=str)
args = parser.parse_args()

date = stringToDate (args.date)

a = Account ()
a.read (filename = args.filename)

print ('balance =      {0}'.format (a.balance (date = date)))
print ('bank balance = {0}'.format (a.bank_balance))
