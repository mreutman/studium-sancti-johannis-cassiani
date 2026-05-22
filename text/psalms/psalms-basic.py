#! /usr/bin/env python3

import os
import re
import pdb

CHAPTER_VSPACE = {}
CHAPTER_VSPACE[1] = "\\psalmEnd"
CHAPTER_VSPACE[2] = "\\psalmEndExtra"
CHAPTER_VSPACE[3] = "\\psalmEndNewPage"
CHAPTER_VSPACE[4] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[5] = "\\psalmEndDecorateNewPage{1.5}"
CHAPTER_VSPACE[6] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[7] = "\\psalmEndNewPage"
CHAPTER_VSPACE[8] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[9] = "\\psalmEnd"
CHAPTER_VSPACE[10] = "\\psalmEndNewPage"
CHAPTER_VSPACE[11] = "\\psalmEnd"
CHAPTER_VSPACE[12] = "\\psalmEnd"
CHAPTER_VSPACE[13] = "\\psalmEndNewPage"
CHAPTER_VSPACE[14] = "\\psalmEnd"
CHAPTER_VSPACE[15] = "\\psalmEnd"
CHAPTER_VSPACE[16] = "\\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[17] = "\\psalmEndNewPage"
CHAPTER_VSPACE[18] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[19] = "\\psalmEndDecorateNewPage{1.5}"
CHAPTER_VSPACE[20] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[21] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[22] = "\\psalmEndDecorateNewPage{1.0}"
CHAPTER_VSPACE[23] = "\\psalmEnd"
CHAPTER_VSPACE[24] = "\\psalmEndNewPage"
CHAPTER_VSPACE[25] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[26] = "\\psalmEndNewPage"
CHAPTER_VSPACE[27] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[28] = "\\psalmEndDecorateNewPage{1.5}"
CHAPTER_VSPACE[29] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[30] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[31] = "\\psalmEndNewPage"
CHAPTER_VSPACE[32] = "\\psalmEnd"
CHAPTER_VSPACE[33] = "\\psalmEnd"
CHAPTER_VSPACE[34] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[35] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[36] = "\\psalmEndNewPage"
CHAPTER_VSPACE[37] = "\\psalmEnd"
CHAPTER_VSPACE[38] = "\\psalmEnd"
CHAPTER_VSPACE[39] = "\\psalmEndNewPage"
CHAPTER_VSPACE[40] = "\\psalmEnd"
CHAPTER_VSPACE[41] = "\\psalmEndNewPage"
CHAPTER_VSPACE[42] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[43] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[44] = "\\psalmEndDecorateNewPage{1.5}"
CHAPTER_VSPACE[45] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[46] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[47] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[48] = "\\psalmEndNewPage"
CHAPTER_VSPACE[49] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[50] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[51] = "\\psalmEndDecorateNewPage{2.0}"
CHAPTER_VSPACE[52] = "\\psalmEnd"
CHAPTER_VSPACE[53] = "\\psalmEnd"
CHAPTER_VSPACE[54] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[55] = "\\psalmEndNewPage"
CHAPTER_VSPACE[56] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[57] = "\\psalmEndNewPage"
CHAPTER_VSPACE[58] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[59] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[60] = "\\psalmEnd"
CHAPTER_VSPACE[61] = "\\psalmEndNewPage"
CHAPTER_VSPACE[62] = "\\psalmEnd"
CHAPTER_VSPACE[63] = "\\psalmEnd"
CHAPTER_VSPACE[64] = "\\psalmEnd"
CHAPTER_VSPACE[65] = "\\psalmEndDecorateNewPage{1.5}"
CHAPTER_VSPACE[66] = "\\psalmEnd"
CHAPTER_VSPACE[67] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[68] = "\\psalmEndExtra"
CHAPTER_VSPACE[69] = "\\psalmEndNewPage" #HERE
CHAPTER_VSPACE[70] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[71] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[72] = "\\psalmEnd"
CHAPTER_VSPACE[73] = "\\psalmEnd"
CHAPTER_VSPACE[74] = "\\psalmEnd"
CHAPTER_VSPACE[75] = "\\psalmEndDecorateNewPage{1.0}"
CHAPTER_VSPACE[76] = "\\psalmEndDecorateNewPage{0.5}" #START HERE
CHAPTER_VSPACE[77] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[78] = "\\psalmEnd"
CHAPTER_VSPACE[79] = "\\psalmEnd"
CHAPTER_VSPACE[80] = "\\psalmEndNewPage"
CHAPTER_VSPACE[81] = "\\psalmEnd"
CHAPTER_VSPACE[82] = "\\psalmEnd"
CHAPTER_VSPACE[83] = "\\psalmEndDecorateNewPage{1.5}"
CHAPTER_VSPACE[84] = "\\psalmEnd"
CHAPTER_VSPACE[85] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[86] = "\\psalmEndNewPage"
CHAPTER_VSPACE[87] = "\\psalmEndDecorateNewPage{1.0}"
CHAPTER_VSPACE[88] = "\\psalmEnd"
CHAPTER_VSPACE[89] = "\\psalmEnd"
CHAPTER_VSPACE[90] = "\\psalmEndNewPage"
CHAPTER_VSPACE[91] = "\\psalmEnd"
CHAPTER_VSPACE[92] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[93] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[94] = "\\psalmEndDecorateNewPage{0.5}"
CHAPTER_VSPACE[95] = "\\psalmEnd"
CHAPTER_VSPACE[96] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[97] = "\\psalmEndDecorateNewPage{1.0}"
CHAPTER_VSPACE[98] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[99] = "\\psalmEndNewPage"
CHAPTER_VSPACE[100] = "\\psalmEnd"
CHAPTER_VSPACE[101] = "\\psalmEnd"
CHAPTER_VSPACE[102] = "\\psalmEndDecorateNewPage{1.0}"
CHAPTER_VSPACE[103] = "\\psalmEnd"
CHAPTER_VSPACE[104] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[105] = "\\psalmEnd"
CHAPTER_VSPACE[106] = "\\psalmEnd"
CHAPTER_VSPACE[107] = "\\psalmEndNewPage"
CHAPTER_VSPACE[108] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[109] = "\\psalmEndDecorateNewPage{1.0}"
CHAPTER_VSPACE[110] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[111] = "\\psalmEnd"
CHAPTER_VSPACE[112] = "\\psalmEnd"
CHAPTER_VSPACE[113] = "\\psalmEnd"
CHAPTER_VSPACE[114] = "\\psalmEndNewPage"
CHAPTER_VSPACE[115] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[116] = "\\psalmEnd"
CHAPTER_VSPACE[117] = "\\psalmEndDecorateNewPage{2.0}"
CHAPTER_VSPACE[118] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[119] = "\\psalmEndNewPage"
CHAPTER_VSPACE[120] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[121] = "\\psalmEndDecorateNewPage{1.5}"
CHAPTER_VSPACE[122] = "\\psalmEnd"
CHAPTER_VSPACE[123] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[124] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[125] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[126] = "\\psalmEndNewPage"
CHAPTER_VSPACE[127] = "\\psalmEnd"
CHAPTER_VSPACE[128] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[129] = "\\psalmEnd"
CHAPTER_VSPACE[130] = "\\psalmEnd"
CHAPTER_VSPACE[131] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[132] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[133] = "\\psalmEndNewPage"
CHAPTER_VSPACE[134] = "\\psalmEndDecorateNewPage{1.0}"
CHAPTER_VSPACE[135] = "\\psalmEnd"
CHAPTER_VSPACE[136] = "\\psalmEnd"
CHAPTER_VSPACE[137] = "\\psalmEnd"
CHAPTER_VSPACE[138] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[139] = "\\psalmEnd"
CHAPTER_VSPACE[140] = "\\psalmEnd"
CHAPTER_VSPACE[141] = "\\psalmEnd"
CHAPTER_VSPACE[142] = "\\psalmEndNewPage"
CHAPTER_VSPACE[143] = "\\psalmEndDecorateNewPage{1.5}"
CHAPTER_VSPACE[144] = "\\psalmEndNewPage"
CHAPTER_VSPACE[145] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[146] = "\\psalmEnd"
CHAPTER_VSPACE[147] = "\\psalmEnd"
CHAPTER_VSPACE[148] = "\\psalmEndDecorate{0.5}"
CHAPTER_VSPACE[149] = "\\psalmEnd"
CHAPTER_VSPACE[150] = "\\psalmEndNewPage"

KEY_PRINTER_LINEBREAK = "$PRX"
TEX_LINEBREAK = "\\linebreak"

def print_chapter(_chapter, _inscript, _body):
  if _inscript:
    text = "\\psalmInscription{" + _inscript + "} " + _body
  else:
    text = _body

  text = text.replace("¿", "¿~")
  text = text.replace("?", "~?")
  text = text.replace(";", "~;")
  text = text.replace("«", "«~")
  text = text.replace("»", "~»")
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


