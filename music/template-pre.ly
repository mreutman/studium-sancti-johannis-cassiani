#(ly:font-config-add-font "/home/anon/Git/studium-sancti-johannis-cassiani/text/books/fonts/dueblo/mod/Dueblo-SEMI-EXT-MED.otf")

#(ly:font-config-add-font "/home/anon/Git/studium-sancti-johannis-cassiani/text/books/fonts/dueblo/mod/Dueblo-SEMI-EXT-REG.otf")

\paper {
  #(define fonts
    (set-global-fonts
     #:roman "Dueblo SemiSerif Extended Medium"
     #:sans "Dueblo SemiSerif Extended Regular"
    ))

  #(set-paper-size "letter")
  top-margin = 0.5\in
  left-margin = 1.0\in
  right-margin = 1.0\in

  score-system-spacing.padding = #5

}

melodyDefaults = {
  \key c \major
  \time 4/4
  \cadenzaOn
  \dynamicUp
  \omit Staff.TimeSignature
  %\omit Stem
  %\override Stem.length = #5
  \override Stem.thickness = #1
  \override Lyrics.LyricSpace.minimum-distance = #1.0
  \set melismaBusyProperties = #'()
}
