#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import os
import datetime as dt
import argparse
from account import Account
from entry import stringToDate

def lookFornext25 (date):
    d = date
    while d.day != 25:
        d += dt.timedelta (days = 1)
    return d

parser = argparse.ArgumentParser(description='Compute balance at given date')
parser.add_argument ('--date', type=str)
parser.add_argument ('--filename', type=str)
args = parser.parse_args()

# parse date. If not provided set date to next 25 starting from yesterday
if args.date:
    date = stringToDate (args.date)
else:
    date = lookFornext25 (dt.date.today ())

# parse filename. If not provided, search for year-comptes.cpt
if args.filename:
    filename = args.filename
else:
    year = os.getenv ('PWD').split('/') [-1]
    filename = year + '-comptes.cpt'

a = Account ()
a.read (filename = filename)

print ('balance on {0} = {1}'.format (date, a.balance (date = date)))
print ('bank balance          = {0}'.format (a.bank_balance))
