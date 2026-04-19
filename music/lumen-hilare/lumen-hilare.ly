\version "2.24.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "blackmensural-c4"
  \melodyDefaults

  % 1
  a4 a( g) a b( c) b a( g) f g a a4. \bar "'"
  % 2
  b4( a g) f d e f d d c( d) d4. \bar "'"
  % 3
  f4 g( a) a b c( b) a4. \bar "'"
  % 4
  f4( g a b) a f( e) d2( f g f4 g a b2 a) \bar "|"
  % 5
  a4 g f e g f e d c( e) e2 \bar "'"
  % 6
  f4 g( a) e e e f d d d( c) d( e f) d2 \bar "|"
  % 7
  a'4 c( d) d c( b) a( g f) g a( b) b a4. \bar "'"
  % 8
  e4 g( a) b( a) b g( a) a4. \bar "'"
  % 9
  f4( e d) d2( f g f4 g a b2 a) \bar "|"
  % 10
  a4 f e( f) d e c d( e) e e4. \bar "'"
  % 11
  f4( a) a( g) e( d) f g a( b) b2 a( g4 f e d2) \bar "'"
  % 12
  f4( g) f( e d) f( g) d4. \bar "'"
  % 13
  a'4 f( e d) c( e) d2 \bar "|"
  % 14
  a'4 c( d) d( c a b c a2) \bar "'"
  % 15
  g4 a b c a2 \bar "'"
  % 16
  f4 g a b a f e d e( f) d2 \bar "|"
  % 17
  c4( d f2 d4 f g2 f4 g a b a f e d c e2) d \fine
}

text = \lyricmode {
  % 1
  \markup { \concat { \fontsize #4 "L" \tied-lyric #"" "u" } }
  -- men __ _ hì -- la _ -- re, sanc _ -- tae gló -- ri -- ae
  % 2
  Pà _ _ -- tris im -- mor -- tá -- lis, čoe -- lès _ -- tis
  % 3
  sanc _ _ -- ti, be -- á _ -- ti,
  % 4
  Ïe _ _ _ -- su Chris _ -- te. __ _ _ _ _ _ _ _
  % 5
  Ac -- če -- dèn -- tes ad oc -- cá -- sum so _ -- lis,
  % 6
  et lu _ -- če ves -- per -- tí -- na ac -- čèn _ -- sa. __ _ _ _
  % 7
  Čan -- tá _ -- mus Pà _ -- trem, __ _ _ et Fí _ -- li -- um, 
  % 8
  et Spí _ -- ri _ -- tum Sanc _  -- tum,
  % 9
  De _ _ -- um. __ _ _ _ _ _ _ _
  % 10
  Dìg -- nus es _ in òm -- ni tèm _ -- po -- re 
  % 11
  čan _ -- tá _ -- ri __ _ vó -- či -- bus __ _ pu -- rīs, __ _ _ _ _
  % 12
  Fí _ -- li __ _ _ De _ -- i,
  % 13
  vi -- tae __ _ _ Dà _ -- tor.
  % 14
  Ì -- de _ -- o __ _ _ _ _ _
  % 15
  e to -- to or -- be
  % 16
  a sčèn -- dit ad te gló -- ri -- a lau _ -- dis.
  % 17
  A _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ -- men.
}

\header {
  title = "LUMEN HÌLARE"
  opus = \markup { \sans \smallCaps "melódia oriǧináli" }
  tagline = #f
}

\include "../template-post.ly"
