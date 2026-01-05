#! /usr/bin/env python3

import argparse

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

if __name__=='__main__':
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
    print(psalms.GetChapterLaTeX(int(chapter)))
  else:
    print("Insufficient arguments")

