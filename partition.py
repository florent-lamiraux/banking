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

categories = {u"énergie" : [u"electricité edf", u"gaz engie",],
              u"eau" : [u"eau veolia",],
              u"téléphonie" : [u"sfr abonnement téléphone mobile aurélie",
                               u"abonnement adsl orange"],
              u"revenus" : [u"caf de haute-garonne", u"pôle emploi",
                            u"salaire cnrs florent", u"salaire aurélie",],
              u"santé" : [u"cotisation mgen",],
              u"école" : [u"la prairie"],
              u"automobile" : [u"automobile",],
              u"maison" : [u"echéance prêt", u"travaux maison"],
              u"impôts" : [u"taxe foncière", u"taxe d'habitation",
                           u"impôt sur le revenu",],
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
