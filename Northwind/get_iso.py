#!/usr/bin/env python
#coding=utf-8

import os
import codecs

def read(filename, token="#ISO Code:"):
    section = None
    buffer = []
    with codecs.open(filename, 'rU', encoding="utf-8") as handle:
        for line in handle.readlines():
            line = line.strip()
            if line.startswith("#"):
                section = line
            elif section == token:
                buffer.append(line)
            else:
                pass

    return "".join([_ for _ in buffer if len(_) > 0])

files = [(_, read(_)) for _ in os.listdir('.') if _.endswith('.txt')]
for fn, iso in sorted(files):
    print(u"%3s\t%s" % (iso.decode('utf-8'), fn.decode('utf-8')))
