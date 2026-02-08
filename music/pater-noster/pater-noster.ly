\version "2.24.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "blackmensural-c4"
  \melodyDefaults

  g8[ a] b[ b] \bar "'"                                             % 1
  a c b a g4\> r8\! \bar "|"                                        % 2
  a[ g a b a( g)] g[( a) b] a[( b)] a4\> r8\! \bar "|"              % 3
  b[ c b b] a[ b] a g4\> r8\! \bar "|"                              % 4
  b[ b] a[ b a] a g4\> r8\! \bar "|"                                % 5
  a[ g] a b[ a( g)] g[( a)] b a[( b)] a4\> r\! \bar "|"             % 6
  g8[ a] b[ b] \bar "'"                                             % 7
  b[ a b c b] \bar "'"                                              % 8
  b a[ b] a[ g] g4\> r8\! \bar "|"                                  % 9
  a g[ a b] c[ b] b[ a b] a g4\> r8\! \bar "|"                      % 10
  a8[ g] a b a[ b a a] g[ a b a g] a a4\> r8\! \bar "|"             % 11
  e g a a[ b a] a a[ g a a( g)] g4\> r8\! \bar "|"                  % 12
  g a[ a a] a^\markup \sans "ret." b a\>[( g)] g4\! \fine           % 13
}

text = \lyricmode {
  \markup { \concat { \fontsize #4 "P" \tied-lyric #"" "à-" } }

  ter nos- ter                                                      % 1
  qui es in čae- līs,                                               % 2
  san- cti- fi- cé- tur _ no- _ men tu- _ um;                       % 3
  ad- vèn- i- at reg- num tu- um;                                   % 4
  fi- at vo- lùn- tas tu- a,                                        % 5
  si- cut in čae- lo _ et _ in tèr- _ ra.                           % 6
  Pa- nem nos- trum                                                 % 7
  quo- ti- di- á- num                                               % 8
  da no- bīs hó- di- e;                                             % 9
  et di- mìt- te no- bīs dé- bi- ta nos- tra,                       % 10
  si- cut et nos di- mìt- ti- mus de- bi- tó- ri- bus nos- trīs,    % 11
  et ne nos in- dú- cas in temp- ta- çi- ó- _ nem,                  % 12
  sed lí- be- ra nos a Mà- _ lo.                                    % 13
}

\header {
  title = "PÀTER NOSTER"
  opus = \markup { \sans \smallCaps "melódia oriǧináli" }
  tagline = #f
}

\include "../template-post.ly"
