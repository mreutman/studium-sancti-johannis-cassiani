#! /usr/bin/env python3

import argparse

kathisma = {}
stasis = {}

kathisma[0] = 1
kathisma[1] = 1
kathisma[2] = 1
kathisma[3] = 1
kathisma[4] = 1
kathisma[5] = 1
kathisma[6] = 1
kathisma[7] = 1
kathisma[8] = 1
kathisma[9] = 2
kathisma[10] = 2
kathisma[11] = 2
kathisma[12] = 2
kathisma[13] = 2
kathisma[14] = 2
kathisma[15] = 2
kathisma[16] = 2
kathisma[17] = 3
kathisma[18] = 3
kathisma[19] = 3
kathisma[20] = 3
kathisma[21] = 3
kathisma[22] = 3
kathisma[23] = 3
kathisma[24] = 4
kathisma[25] = 4
kathisma[26] = 4
kathisma[27] = 4
kathisma[28] = 4
kathisma[29] = 4
kathisma[30] = 4
kathisma[31] = 4
kathisma[32] = 5
kathisma[33] = 5
kathisma[34] = 5
kathisma[35] = 5
kathisma[36] = 5
kathisma[37] = 6
kathisma[38] = 6
kathisma[39] = 6
kathisma[40] = 6
kathisma[41] = 6
kathisma[42] = 6
kathisma[43] = 6
kathisma[44] = 6
kathisma[45] = 6
kathisma[46] = 7
kathisma[47] = 7
kathisma[48] = 7
kathisma[49] = 7
kathisma[50] = 7
kathisma[51] = 7
kathisma[52] = 7
kathisma[53] = 7
kathisma[54] = 7
kathisma[55] = 8
kathisma[56] = 8
kathisma[57] = 8
kathisma[58] = 8
kathisma[59] = 8
kathisma[60] = 8
kathisma[61] = 8
kathisma[62] = 8
kathisma[63] = 8
kathisma[64] = 9
kathisma[65] = 9
kathisma[66] = 9
kathisma[67] = 9
kathisma[68] = 9
kathisma[69] = 9
kathisma[70] = 10
kathisma[71] = 10
kathisma[72] = 10
kathisma[73] = 10
kathisma[74] = 10
kathisma[75] = 10
kathisma[76] = 10
kathisma[77] = 11
kathisma[78] = 11
kathisma[79] = 11
kathisma[80] = 11
kathisma[81] = 11
kathisma[82] = 11
kathisma[83] = 11
kathisma[84] = 11
kathisma[85] = 12
kathisma[86] = 12
kathisma[87] = 12
kathisma[88] = 12
kathisma[89] = 12
kathisma[90] = 12
kathisma[91] = 13
kathisma[92] = 13
kathisma[93] = 13
kathisma[94] = 13
kathisma[95] = 13
kathisma[96] = 13
kathisma[97] = 13
kathisma[98] = 13
kathisma[99] = 13
kathisma[100] = 13
kathisma[101] = 14
kathisma[102] = 14
kathisma[103] = 14
kathisma[104] = 14
kathisma[105] = 15
kathisma[106] = 15
kathisma[107] = 15
kathisma[108] = 15
kathisma[109] = 16
kathisma[110] = 16
kathisma[111] = 16
kathisma[112] = 16
kathisma[113] = 16
kathisma[114] = 16
kathisma[115] = 16
kathisma[116] = 16
kathisma[117] = 16
kathisma[118] = 17
kathisma[119] = 18
kathisma[120] = 18
kathisma[121] = 18
kathisma[122] = 18
kathisma[123] = 18
kathisma[124] = 18
kathisma[125] = 18
kathisma[126] = 18
kathisma[127] = 18
kathisma[128] = 18
kathisma[129] = 18
kathisma[130] = 18
kathisma[131] = 18
kathisma[132] = 18
kathisma[133] = 18
kathisma[134] = 19
kathisma[135] = 19
kathisma[136] = 19
kathisma[137] = 19
kathisma[138] = 19
kathisma[139] = 19
kathisma[140] = 19
kathisma[141] = 19
kathisma[142] = 19
kathisma[143] = 20
kathisma[144] = 20
kathisma[145] = 20
kathisma[146] = 20
kathisma[147] = 20
kathisma[148] = 20
kathisma[149] = 20
kathisma[150] = 20

stasis[1] =  1
stasis[2] =  1
stasis[3] =  1
stasis[4] =  2
stasis[5] =  2
stasis[6] =  2
stasis[7] =  3
stasis[8] =  3
stasis[9] =  1
stasis[10] =  1
stasis[11] =  2
stasis[12] =  2
stasis[13] =  2
stasis[14] =  3
stasis[15] =  3
stasis[16] =  3
stasis[17] =  1
stasis[18] =  2
stasis[19] =  2
stasis[20] =  2
stasis[21] =  3
stasis[22] =  3
stasis[23] =  3
stasis[24] =  1
stasis[25] =  1
stasis[26] =  1
stasis[27] =  2
stasis[28] =  2
stasis[29] =  2
stasis[30] =  3
stasis[31] =  3
stasis[32] =  1
stasis[33] =  1
stasis[34] =  2
stasis[35] =  2
stasis[36] =  3
stasis[37] =  1
stasis[38] =  1
stasis[39] =  1
stasis[40] =  2
stasis[41] =  2
stasis[42] =  2
stasis[43] =  3
stasis[44] =  3
stasis[45] =  3
stasis[46] =  1
stasis[47] =  1
stasis[48] =  1
stasis[49] =  2
stasis[50] =  2
stasis[51] =  3
stasis[52] =  3
stasis[53] =  3
stasis[54] =  3
stasis[55] =  1
stasis[56] =  1
stasis[57] =  1
stasis[58] =  2
stasis[59] =  2
stasis[60] =  2
stasis[61] =  3
stasis[62] =  3
stasis[63] =  3
stasis[64] =  1
stasis[65] =  1
stasis[66] =  1
stasis[67] =  2
stasis[68] =  3
stasis[69] =  3
stasis[70] =  1
stasis[71] =  1
stasis[72] =  2
stasis[73] =  2
stasis[74] =  3
stasis[75] =  3
stasis[76] =  3
stasis[77] =  1
stasis[78] =  2
stasis[79] =  2
stasis[80] =  2
stasis[81] =  3
stasis[82] =  3
stasis[83] =  3
stasis[84] =  3
stasis[85] =  1
stasis[86] =  1
stasis[87] =  1
stasis[88] =  2
stasis[89] =  3
stasis[90] =  3
stasis[91] =  1
stasis[92] =  1
stasis[93] =  1
stasis[94] =  2
stasis[95] =  2
stasis[96] =  2
stasis[97] =  3
stasis[98] =  3
stasis[99] =  3
stasis[100] =  3
stasis[101] =  1
stasis[102] =  1
stasis[103] =  2
stasis[104] =  3
stasis[105] =  1
stasis[106] =  2
stasis[107] =  3
stasis[108] =  3
stasis[109] =  1
stasis[110] =  1
stasis[111] =  1
stasis[112] =  2
stasis[113] =  2
stasis[114] =  2
stasis[115] =  3
stasis[116] =  3
stasis[117] =  3
stasis[118] =  1
stasis[119] =  1
stasis[120] =  1
stasis[121] =  1
stasis[122] =  1
stasis[123] =  1
stasis[124] =  2
stasis[125] =  2
stasis[126] =  2
stasis[127] =  2
stasis[128] =  2
stasis[129] =  3
stasis[130] =  3
stasis[131] =  3
stasis[132] =  3
stasis[133] =  3
stasis[134] =  1
stasis[135] =  1
stasis[136] =  1
stasis[137] =  2
stasis[138] =  2
stasis[139] =  2
stasis[140] =  3
stasis[141] =  3
stasis[142] =  3
stasis[143] =  1
stasis[144] =  1
stasis[145] =  2
stasis[146] =  2
stasis[147] =  2
stasis[148] =  3
stasis[149] =  3
stasis[150] =  3

class Psalms:
  __file_psalms = "psalms.csv"
  __dict2_psalms = {}
  __dict2_inscripts = {}

  def __init__(self):
    keys = []
    for n in range(0, 151):
      keys.append(n)

    self.__dict2_psalms = {key: {} for key in keys}
    self.__dict2_inscripts = {key: {} for key in keys}

    f = open(self.__file_psalms, 'r')

    line = f.readline()
    while line:
      if '#' == line[0]:
        line = f.readline()
        continue

      s = line.split('^')
      ch = int(s[0])
      vs = int(s[1])
      is_inscript = s[2][0] == 'i'
      txt = s[3].rstrip() # removes ending whitespace and '\n'

      if is_inscript:
        self.__dict2_inscripts[ch][vs] = txt
      else:
        self.__dict2_psalms[ch][vs] = txt
      line = f.readline()

    f.close()

  def GetChapterLaTeX(self, ch):
    chapter = "\\psalmChapter{" + str(ch) + "} "
    inscript = ""
    text = ""
    separator = " "

    inscript = separator.join(
      "\\verseNumber{" + str(k) + "} " + v
      for k,v in self.__dict2_inscripts[ch].items())

    text = separator.join(
      "\\verseNumber{" + str(k) + "} " + v
      for k,v in self.__dict2_psalms[ch].items())

    if inscript:
      return (
        chapter +
        "\\psalmInscription{" + inscript + "} " +
        "\\psalmText{" + text + "}")

    return chapter + "\\psalmText{" + text + "}"

def WriteDivisionBegin(f, k):
  f.write("\\PsalmDivisionBegin{" + str(k) + "}\n")

def WriteDivisionNext(f, k, s):
  f.write("\\PsalmDivisionNext{" + str(k) + "}{" + str(s) + "}\n")

if __name__=='__main__':
  zfill_len = 3
  range_char = ','

  parser = argparse.ArgumentParser(description="Vulgate Psalms")
  parser.add_argument(
    "--all",
    action='store_true',
    help="Print all Psalms")
  parser.add_argument(
    "--chapter",
    type=str,
    default="",
    help="Psalm Chapter(s), range is BEGIN,END")
  parser.add_argument(
    "--verse",
    type=str,
    default="",
    help="Psalm Verse(s), range is BEGIN,END")

  args = parser.parse_args()
  psalms = Psalms()

  if args.all:
    print("Make all Psalms")

    f = open("psalms.tex", "w")
    k = 0
    s = 0

    for n in range(1, 151):
      if 118 == n:
        # Psalm 118 is special, being the only Psalm with internal divisions
        k = kathisma[n]
        s = stasis[n]
        WriteDivisionBegin(f, k)
        text = psalms.GetChapterLaTeX(n)
        text1, sep, textx = text.partition("\\verseNumber{73}")
        f.write(text1 + "\n")

        s = s + 1
        WriteDivisionNext(f, k, s)
        text = sep + textx
        text2, sep, textx = text.partition("\\verseNumber{132}")
        f.write(text2 + "\n")

        s = s + 1
        WriteDivisionNext(f, k, s)
        text3 = sep + textx
        f.write(text3 + "\n")

        continue

      elif k != kathisma[n]:
        k = kathisma[n]
        s = stasis[n]
        WriteDivisionBegin(f, k)

      elif s != stasis[n]:
        s = stasis[n]
        WriteDivisionNext(f, k, s)

      text = psalms.GetChapterLaTeX(n)
      f.write(text + "\n")
    f.close()

  elif range_char in args.chapter:
    chapters = args.chapter.split(range_char)
    print("Make Psalm chapters " + chapters[0] + " through " + chapters[1])

  elif range_char in args.verse and args.chapter:
    verses = args.verse.split(range_char)
    chapter = args.chapter
    print("Make Psalm chapter " + chapter + ":" + verses[0] + "-" + verses[1])

  elif args.chapter:
    chapter = args.chapter
    print("Make Psalm chapter " + chapter)

    filename = chapter.zfill(zfill_len)
    text = psalms.GetChapterLaTeX(int(chapter))

    with open(filename + ".tex", "w") as f:
      f.write(text)

  else:
    print("Insufficient arguments")

