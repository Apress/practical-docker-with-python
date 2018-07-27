#!/usr/bin/env python3

from os import getenv

if getenv('NAME') is None:
    name = 'World'
else:
    name = getenv('NAME')

print("Hello, {}!".format(name))
