#! /usr/bin/env python3

import os
import re
import pdb

CHAPTER_VSPACE = {}
CHAPTER_VSPACE[1] = "\\psalmEnd{1}"
CHAPTER_VSPACE[2] = "\\psalmEndNewPage"
CHAPTER_VSPACE[3] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[4] = "\\psalmEndNewPage"
CHAPTER_VSPACE[5] = "\\psalmEnd{1}"
CHAPTER_VSPACE[6] = "\\psalmEnd{2}"
CHAPTER_VSPACE[7] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[8] = "\\psalmEndDecorateNewPage{1.0}"
CHAPTER_VSPACE[9] = "\\psalmEndDecorateNewPage{1.25}"
CHAPTER_VSPACE[10] = "\\psalmEnd{1}"
CHAPTER_VSPACE[11] = "\\psalmEndNewPage"
CHAPTER_VSPACE[12] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[13] = "\\psalmEndNewPage"
CHAPTER_VSPACE[14] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[15] = "\\psalmEnd{1}"
CHAPTER_VSPACE[16] = "\\psalmEndNewPage"
CHAPTER_VSPACE[17] = "\\psalmEnd{1}"
CHAPTER_VSPACE[18] = "\\psalmEnd{1}"
CHAPTER_VSPACE[19] = "\\psalmEnd{1}"
CHAPTER_VSPACE[20] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[21] = "\\psalmEndNewPage"
CHAPTER_VSPACE[22] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[23] = "\\psalmEndNewPage"
CHAPTER_VSPACE[24] = "\\psalmEndNewPage"
CHAPTER_VSPACE[25] = "\\psalmEnd{1}" # START HERE
CHAPTER_VSPACE[26] = "\\psalmEnd{1}"
CHAPTER_VSPACE[27] = "\\psalmEnd{1}"
CHAPTER_VSPACE[28] = "\\psalmEnd{1}"
CHAPTER_VSPACE[29] = "\\psalmEnd{1}"
CHAPTER_VSPACE[30] = "\\psalmEnd{1}"
CHAPTER_VSPACE[31] = "\\psalmEnd{1}"
CHAPTER_VSPACE[32] = "\\psalmEnd{1}"
CHAPTER_VSPACE[33] = "\\psalmEnd{1}"
CHAPTER_VSPACE[34] = "\\psalmEnd{1}"
CHAPTER_VSPACE[35] = "\\psalmEnd{1}"
CHAPTER_VSPACE[36] = "\\psalmEnd{1}"
CHAPTER_VSPACE[37] = "\\psalmEnd{1}"
CHAPTER_VSPACE[38] = "\\psalmEnd{1}"
CHAPTER_VSPACE[39] = "\\psalmEnd{1}"
CHAPTER_VSPACE[40] = "\\psalmEnd{1}"
CHAPTER_VSPACE[41] = "\\psalmEnd{1}"
CHAPTER_VSPACE[42] = "\\psalmEnd{1}"
CHAPTER_VSPACE[43] = "\\psalmEnd{1}"
CHAPTER_VSPACE[44] = "\\psalmEnd{1}"
CHAPTER_VSPACE[45] = "\\psalmEnd{1}"
CHAPTER_VSPACE[46] = "\\psalmEnd{1}"
CHAPTER_VSPACE[47] = "\\psalmEnd{1}"
CHAPTER_VSPACE[48] = "\\psalmEnd{1}"
CHAPTER_VSPACE[49] = "\\psalmEnd{1}"
CHAPTER_VSPACE[50] = "\\psalmEnd{1}"
CHAPTER_VSPACE[51] = "\\psalmEnd{1}"
CHAPTER_VSPACE[52] = "\\psalmEnd{1}"
CHAPTER_VSPACE[53] = "\\psalmEnd{1}"
CHAPTER_VSPACE[54] = "\\psalmEnd{1}"
CHAPTER_VSPACE[55] = "\\psalmEnd{1}"
CHAPTER_VSPACE[56] = "\\psalmEnd{1}"
CHAPTER_VSPACE[57] = "\\psalmEnd{1}"
CHAPTER_VSPACE[58] = "\\psalmEnd{1}"
CHAPTER_VSPACE[59] = "\\psalmEnd{1}"
CHAPTER_VSPACE[60] = "\\psalmEnd{1}"
CHAPTER_VSPACE[61] = "\\psalmEnd{1}"
CHAPTER_VSPACE[62] = "\\psalmEnd{1}"
CHAPTER_VSPACE[63] = "\\psalmEnd{1}"
CHAPTER_VSPACE[64] = "\\psalmEnd{1}"
CHAPTER_VSPACE[65] = "\\psalmEnd{1}"
CHAPTER_VSPACE[66] = "\\psalmEnd{1}"
CHAPTER_VSPACE[67] = "\\psalmEnd{1}"
CHAPTER_VSPACE[68] = "\\psalmEnd{1}"
CHAPTER_VSPACE[69] = "\\psalmEnd{1}"
CHAPTER_VSPACE[70] = "\\psalmEnd{1}"
CHAPTER_VSPACE[71] = "\\psalmEnd{1}"
CHAPTER_VSPACE[72] = "\\psalmEnd{1}"
CHAPTER_VSPACE[73] = "\\psalmEnd{1}"
CHAPTER_VSPACE[74] = "\\psalmEnd{1}"
CHAPTER_VSPACE[75] = "\\psalmEnd{1}"
CHAPTER_VSPACE[76] = "\\psalmEnd{1}"
CHAPTER_VSPACE[77] = "\\psalmEnd{1}"
CHAPTER_VSPACE[78] = "\\psalmEnd{1}"
CHAPTER_VSPACE[79] = "\\psalmEnd{1}"
CHAPTER_VSPACE[80] = "\\psalmEnd{1}"
CHAPTER_VSPACE[81] = "\\psalmEnd{1}"
CHAPTER_VSPACE[82] = "\\psalmEnd{1}"
CHAPTER_VSPACE[83] = "\\psalmEnd{1}"
CHAPTER_VSPACE[84] = "\\psalmEnd{1}"
CHAPTER_VSPACE[85] = "\\psalmEnd{1}"
CHAPTER_VSPACE[86] = "\\psalmEnd{1}"
CHAPTER_VSPACE[87] = "\\psalmEnd{1}"
CHAPTER_VSPACE[88] = "\\psalmEnd{1}"
CHAPTER_VSPACE[89] = "\\psalmEnd{1}"
CHAPTER_VSPACE[90] = "\\psalmEnd{1}"
CHAPTER_VSPACE[91] = "\\psalmEnd{1}"
CHAPTER_VSPACE[92] = "\\psalmEnd{1}"
CHAPTER_VSPACE[93] = "\\psalmEnd{1}"
CHAPTER_VSPACE[94] = "\\psalmEnd{1}"
CHAPTER_VSPACE[95] = "\\psalmEnd{1}"
CHAPTER_VSPACE[96] = "\\psalmEnd{1}"
CHAPTER_VSPACE[97] = "\\psalmEnd{1}"
CHAPTER_VSPACE[98] = "\\psalmEnd{1}"
CHAPTER_VSPACE[99] = "\\psalmEnd{1}"
CHAPTER_VSPACE[100] = "\\psalmEnd{1}"
CHAPTER_VSPACE[101] = "\\psalmEnd{1}"
CHAPTER_VSPACE[102] = "\\psalmEnd{1}"
CHAPTER_VSPACE[103] = "\\psalmEnd{1}"
CHAPTER_VSPACE[104] = "\\psalmEnd{1}"
CHAPTER_VSPACE[105] = "\\psalmEnd{1}"
CHAPTER_VSPACE[106] = "\\psalmEnd{1}"
CHAPTER_VSPACE[107] = "\\psalmEnd{1}"
CHAPTER_VSPACE[108] = "\\psalmEnd{1}"
CHAPTER_VSPACE[109] = "\\psalmEnd{1}"
CHAPTER_VSPACE[110] = "\\psalmEnd{1}"
CHAPTER_VSPACE[111] = "\\psalmEnd{1}"
CHAPTER_VSPACE[112] = "\\psalmEnd{1}"
CHAPTER_VSPACE[113] = "\\psalmEnd{1}"
CHAPTER_VSPACE[114] = "\\psalmEnd{1}"
CHAPTER_VSPACE[115] = "\\psalmEnd{1}"
CHAPTER_VSPACE[116] = "\\psalmEnd{1}"
CHAPTER_VSPACE[117] = "\\psalmEnd{1}"
CHAPTER_VSPACE[118] = "\\psalmEnd{1}"
CHAPTER_VSPACE[119] = "\\psalmEnd{1}"
CHAPTER_VSPACE[120] = "\\psalmEnd{1}"
CHAPTER_VSPACE[121] = "\\psalmEnd{1}"
CHAPTER_VSPACE[122] = "\\psalmEnd{1}"
CHAPTER_VSPACE[123] = "\\psalmEnd{1}"
CHAPTER_VSPACE[124] = "\\psalmEnd{1}"
CHAPTER_VSPACE[125] = "\\psalmEnd{1}"
CHAPTER_VSPACE[126] = "\\psalmEnd{1}"
CHAPTER_VSPACE[127] = "\\psalmEnd{1}"
CHAPTER_VSPACE[128] = "\\psalmEnd{1}"
CHAPTER_VSPACE[129] = "\\psalmEnd{1}"
CHAPTER_VSPACE[130] = "\\psalmEnd{1}"
CHAPTER_VSPACE[131] = "\\psalmEnd{1}"
CHAPTER_VSPACE[132] = "\\psalmEnd{1}"
CHAPTER_VSPACE[133] = "\\psalmEnd{1}"
CHAPTER_VSPACE[134] = "\\psalmEnd{1}"
CHAPTER_VSPACE[135] = "\\psalmEnd{1}"
CHAPTER_VSPACE[136] = "\\psalmEnd{1}"
CHAPTER_VSPACE[137] = "\\psalmEnd{1}"
CHAPTER_VSPACE[138] = "\\psalmEnd{1}"
CHAPTER_VSPACE[139] = "\\psalmEnd{1}"
CHAPTER_VSPACE[140] = "\\psalmEnd{1}"
CHAPTER_VSPACE[141] = "\\psalmEnd{1}"
CHAPTER_VSPACE[142] = "\\psalmEnd{1}"
CHAPTER_VSPACE[143] = "\\psalmEnd{1}"
CHAPTER_VSPACE[144] = "\\psalmEnd{1}"
CHAPTER_VSPACE[145] = "\\psalmEnd{1}"
CHAPTER_VSPACE[146] = "\\psalmEnd{1}"
CHAPTER_VSPACE[147] = "\\psalmEnd{1}"
CHAPTER_VSPACE[148] = "\\psalmEnd{1}"
CHAPTER_VSPACE[149] = "\\psalmEnd{1}"
CHAPTER_VSPACE[150] = "\\psalmEnd{1}"

KEY_PRINTER_LINEBREAK = "$PRX"
TEX_LINEBREAK = "\\linebreak"

def print_chapter(_chapter, _inscript, _body):
  if _inscript:
    text = "\\psalmInscription{" + _inscript + "} " + _body
  else:
    text = _body

  text = text.replace(KEY_PRINTER_LINEBREAK, TEX_LINEBREAK)
  text = text + CHAPTER_VSPACE[_chapter]

  print("\\psalmChapter{" + str(_chapter) + "}\n")
  print(text + "\n")

path = os.path.dirname(os.path.realpath(__file__))
f = open(path + "/psalms.csv", "r")

current_chapter = 0
current_verse = 0
inscript = ""
body = ""

line = f.readline()
while line:
  if '#' == line[0]:
    line = f.readline()
    continue

  s = line.split('^')
  chapter = int(s[0])
  verse = int(s[1])
  is_inscript = s[2][0] == 'i'
  text = s[3].rstrip() # removes ending whitespace and '\n'

  if current_chapter != chapter:
    if current_chapter == 25:
      break
    if current_chapter != 0:
      print_chapter(current_chapter, inscript.rstrip(), body.rstrip())

    current_chapter = chapter
    inscript = ""
    body = ""

  if is_inscript:
    inscript = (inscript +
      "\\psalmVerse{" + str(verse) + "}" + text + " ")

    current_verse = verse

  else:
    if current_verse == verse:
      body = body + text + " "
    else:
      body = (body + 
        "\\psalmVerse{" + str(verse) + "}" + text + " ")

    current_verse = verse

  line = f.readline()

print_chapter(current_chapter, inscript.rstrip(), body.rstrip())

f.close()


