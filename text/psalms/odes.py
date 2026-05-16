#! /usr/bin/env python3

import os
import re
import pdb

ODE_VSPACE = {}

KEY_PRINTER_LINEBREAK = "$PRX"
TEX_LINEBREAK = "\\linebreak"

path = os.path.dirname(os.path.realpath(__file__))
f = open(path + "/odes-vetus.csv", "r")

current_ode = 0
line = f.readline()
while line:
  if '#' == line[0]:
    line = f.readline()
    continue

  s = line.split('^')
  ode = s[0]
  count = s[1]
  text = s[2].rstrip() # removes ending whitespace and '\n'

  is_count = s[1][0] != 'x'

  text = text.replace("¿", "¿~")
  text = text.replace("?", "~?")
  text = text.replace(";", "~;")
  text = text.replace("«", "«~")
  text = text.replace("»", "~»")
  text = text.replace(KEY_PRINTER_LINEBREAK, TEX_LINEBREAK)

  if current_ode != ode:
    print("\\odeChapter{" + ode + "}\n")
    current_ode = ode

  if not is_count:
    print(text + "\n")
  else:
    if count == "10":
      print("\\indentOn\n")

    print("\\odeCount{" + count + "}" + text + "\n")

    if count == "1":
      print("\\indentOff\n")


  line = f.readline()

f.close()
