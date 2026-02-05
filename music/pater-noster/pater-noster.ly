\version "2.24.0"

% Function to wrap every lyric syllable in \smallCaps markup
smallCapsLyrics =
#(define-music-function (lyrics) (ly:music?)
   (music-map
     (lambda (m)
       (if (music-is-of-type? m 'lyric-event)
           (set! (ly:music-property m 'text)
                 #{ \markup \smallCaps #(ly:music-property m 'text) #}))
       m)
     lyrics))

melody = \relative c' {
  \clef tenorvarC
  \key c \major
  \time 4/4
  \omit Staff.TimeSignature
  \omit Stem
  \override Lyrics.LyricSpace.minimum-distance = #1.5
  %\override Staff.Clef.font-size = #-3.5
  \cadenzaOn
  g a b b \bar "'" a c b a g4. \bar "'"
  a4 g a b a( g) g( a) b a( b) a \bar ","
}

text = \smallCapsLyrics \lyricmode {
  Pà- ter nos- ter qui es in čae- līs,
  san- cti- fi- cé- tur no- men tu- um;

%\firstLetter{P}àter noster, qui es in ċaelīs, sanctificétur nomen tuum. Advèniat regnum tuum. Fiat volùntas tua, sicut in ċaelo et in tèrra. Panem nostrum quotidiánum da nobīs hódie, et dimìtte nobīs débita nostra, sicut et nos dimìttimus debitóribus nostrīs, et ne nos indúcas in temptaçiónem, sed líbera nos a Màlo.}

}

#(ly:font-config-add-font "/home/anon/Git/studium-sancti-johannis-cassiani/text/books/fonts/dueblo/mod/Dueblo-SEMI-EXT-MED.otf")

\paper {
  #(define fonts
    (set-global-fonts
     #:roman "Dueblo SemiSerif Extended Medium"
    ))
}

\score {
  <<
    \new Voice = "one" { 
      \autoBeamOff
      %\slurUp
      \stemUp
      \melody
    }
    \new Lyrics \lyricsto "one" \text
  >>
  \layout { }
  \midi { }
}
