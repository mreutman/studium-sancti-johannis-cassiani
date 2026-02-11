\version "2.24.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "blackmensural-c4"
  \melodyDefaults

  % 1
  a8[ a( g)] a[ b( c) b] a[( g) f] g[ a a] \bar "'"
  % 2
  b[( a g) f] d[ e f d] d[ c( d) d] \bar "'"
  % 3
  f[ g( a) a] b[ c( b)] a4 \bar "'"
  % 4
  f8[( g a b) a] f[( e)] d4( f g f8[ g a] b4 a\>) r\! \bar "|"
  % 5
  a8[ g f e] g f[ e d] c[( e)] e4 \bar "'"
  % 6
  f8 g[( a) e] e[ e f d] d[ d( c) d( e f)] d4\> r\! \bar "|"
  % 7
  a'8[ c( d) d] c[( b) a( g f)] g a[( b) b] a4 \bar "'"
  % 8
  e8 g[( a) b( a) b] g[( a)] a4 \bar "'"
  % 9
  f8[( e d)] d4( f g f8[ g a] b4 a\>) r\! \bar "|"
  % 10
  a8[ f] e[( f)] d e[ c] d[( e) e] e4 \bar "'"
  % 11
  f8[( a) a( g) e( d)] f[ g a( b)] b4 a( g8[ f e] d4) \bar "'"
  % 12
  f8[( g) f( e d)] f[( g)] d4 \bar "'"
  % 13
  a'8[ f( e d)] c[( e)] d4 r8 \bar "|"
  % 14
  a'[ c( d) d( c a b c] a4) \bar "'"
  % 15
  g8 a[ b] c a4 \bar "'"
  % 16
  f8[ g a] b a f[ e d] e[( f)] d4\> r\! \bar "|"
  % 17
  b8([ c] f4 d8[ f] g4 f8[ g a] b4 a8[ f e d c] e4) d \fine
}

text = \lyricmode {
  % 1
  \markup { \concat { \fontsize #4 "L" \tied-lyric #"" "u-" } }
  men _ hì- la- _ re, sanc- _ tae gló-  ri- ae
  % 2
  Pà- _ _ tris im- mor- tá- lis, čae- lès- _ tis
  % 3
  sanc- _ _ ti, be- á- _ ti,
  % 4
  Je- _ _ _ _ su Chris- _ te. _ _ _ _ _ _
  % 5
  Ac- če- dèn- tes ad oc- cá- sum so- _ lis,
  % 6
  et lu- _ če ves- per- tí- na ac- čèn- _ sa. _ _ _
  % 7
  Čan- tá- _ mus Pà- _ trem, _ _ et Fí- _ li- um, 
  % 8
  et Spí- _ ri- _ tum San- _ ctum,
  % 9
  De- _ _ um. _ _ _ _ _ _ _
  % 10
  Dìg- nus es _ in òm- ni tèm- _ po- re 
  % 11
  can- _ tá- _ ri _ vó- či- bus _ pu- rīs, _ _ _ _
  % 12
  Fí- _ li _ _ De- _ i,
  % 13
  vi- tae _ _ Dà- _ tor.
  % 14
  Ì- de- _ o _ _ _ _ _
  % 15
  e to- to or- be
  % 16
  a- sčèn- dit ad te gló- ri- a lau- _ dis.
  % 17
  A- _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ men.
}

\header {
  title = "LUMEN HÌLARE"
  opus = \markup { \sans \smallCaps "melódia oriǧináli" }
  tagline = #f
}

\include "../template-post.ly"
