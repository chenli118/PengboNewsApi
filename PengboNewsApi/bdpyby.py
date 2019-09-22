# -*- coding: utf-8 -*-
import sys
from bypy import ByPy

def run():
    bp = ByPy()
    bp.syncup(localdir=u'', remotedir=u'youtube/', deleteremote=False)

if __name__=="__main__":
    run()
