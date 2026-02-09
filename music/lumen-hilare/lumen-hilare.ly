\version "2.24.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "blackmensural-c4"
  \melodyDefaults

  a8[ a( g)] a[ b( c) b] a[( g) f] g[ a a] \bar "'"

  b[( a g) f] d[ e f d] d[ c( d) d] \bar "'"

  f[ g( a) a] b[ c( b)] a4 \bar "'"
  
  f8[( g a b) a] f[( e)] d4( f g f8[ g a] b4 a) r \bar "|"
  
  a8[ g f e] g f[ e d] c[( e)] e4 \bar "'"
  
  f8 g[( a) e] e[ e f d] d[ d( c) d( e f)] d4 r \bar "|"
  
  a'8[ c( d) d] c[( b) a( g f)] g a[( b) b] a4 \bar "'"
  
  e8 g[( a) b( a) b] g[( a)] a4 \bar "'"
  
  f8[( e d)] d4( f g f8[ g a] b4 a) r \bar "|"

  a8[ f] e[( f)] d e[ c] d[( e) e] e4 \bar "'"
  
  f8[( a) a( g) e( d)] f[ g a( b)] b4 a( g8[ f e] d4) \bar "'"

  f8[( g) f( e d)] f[( g)] d4 \bar "'"

  a'8[ f( e d)] c[( e)] d4 r8 \bar "|"

  a'[ c( d) d( c a b c] a4) \bar "'"

  g8 a[ b] c a4 \bar "'"

  f8[ g a] b a f[ e d] e[( f)] d4 r \bar "|"

  b8([ c] f4 d8[ f] g4 f8[ g a] b4 a8[ f e d c] e4) d \fine
}

text = \lyricmode {
  \markup { \concat { \fontsize #4 "L" \tied-lyric #"" "u-" } }

  men _ hì- la- _ re, sanc- _ tae gló-  ri- ae

  Pà- _ _ tris im- mor- tá- lis, čae- lès- _ tis
  
  sanc- _ _ ti, be- á- _ ti,
  
  Je- _ _ _ _ su Chris- _ te. _ _ _ _ _ _

  Ac- če- dèn- tes ad oc- cá- sum so- _ lis,

  et lu- _ če ves- per- tí- na ac- čèn- _ sa. _ _ _

  Čan- tá- _ mus Pà- _ trem, _ _ et Fí- _ li- um, 
  
  et Spí- _ ri- _ tum San- _ ctum,
  
  De- _ _ um. _ _ _ _ _ _ _

  Dìg- nus es _ in òm- ni tèm- _ po- re 
  
  can- _ tá- _ ri _ vó- či- bus _ pu- rīs, _ _ _ _

  Fí- _ li _ _ De- _ i,
  
  vi- tae _ _ Dà- _ tor.

  Ì- de- _ o _ _ _ _ _

  e to- to or- be

  a- sčèn- dit ad te gló- ri- a lau- _ dis.

  A- _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ men.
}

\header {
  title = "LUMEN HÌLARE"
  opus = \markup { \sans \smallCaps "melódia oriǧináli" }
  tagline = #f
}

\include "../template-post.ly"
