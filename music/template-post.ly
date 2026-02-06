\markup \vspace #1

\score {
  <<
    \new Voice = "one" { 
      \autoBeamOff
      %\slurUp
      %\stemUp
      \melody
    }
    \new Lyrics \lyricsto "one" \text
  >>
  \layout { 
    indent = 0\mm
    \context {
      \Score
      \override TextScript.font-shape = #'caps
      \override LyricText.font-shape = #'caps
    }
  }
  \midi { }
}
