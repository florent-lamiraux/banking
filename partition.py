#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import os
import argparse
import codecs
from account import Account
from decimal import Decimal

parser = argparse.ArgumentParser(description='Compute partition of data')
parser.add_argument ('--filename', type=str)
args = parser.parse_args()

# parse filename. If not provided, search for year-comptes.cpt
if args.filename:
    filename = args.filename
else:
    year = os.getenv ('PWD').split('/') [-1]
    filename = year + '-comptes.cpt'

a = Account ()
a.read (filename = filename)

categories = {u"�nergie" : [u"electricit� edf", u"gaz engie",],
              u"eau" : [u"eau veolia",],
              u"t�l�phonie" : [u"sfr abonnement t�l�phone mobile aur�lie",
                               u"abonnement adsl orange"],
              u"revenus" : [u"caf de haute-garonne", u"p�le emploi",
                            u"salaire cnrs florent", u"salaire aur�lie",],
              u"sant�" : [u"cotisation mgen",],
              u"�cole" : [u"la prairie"],
              u"automobile" : [u"automobile",],
              u"maison" : [u"ech�ance pr�t", u"travaux maison"],
              u"imp�ts" : [u"taxe fonci�re", u"taxe d'habitation",
                           u"imp�t sur le revenu",],
              u"dons" : [u"handicap international", u"don "],
              u"sport musique" : [u"taekwondo", u"ecole de musique ramonville",
                                  u"musique conservatoire"]}

accounts = dict ()
total = dict ()

for k, labels in categories.iteritems ():
    accounts [k] = list ()
    total [k] = Decimal (0.00)
    for l in labels:
        a2 = Account ()
        fileout =  "bilan/" + l + ".cpt"
        toBeRemoved = list ()
        for e in a.entries:
            if e.label.lower ().find (l) != -1:
                a2.entries.append (e)
                toBeRemoved.append (e)
        for e in toBeRemoved:
            a.entries.remove (e)
        accounts [k].append ([l, a2.balance ()])
        total [k] += a2.balance ()
        a2.save (fileout)
a.save ("bilan/other.cpt")

with codecs.open ("bilan/synthese", "w", encoding='utf-8') as f:
    for k in categories.keys ():
        f.write (u"{0}\t: {1}\n".format (k, total [k]))
        for l, amount in accounts [k]:
            f.write (u"  {0}\t: {1}\n".format (l, amount))
