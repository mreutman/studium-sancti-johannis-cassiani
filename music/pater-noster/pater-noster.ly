\version "2.24.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef tenorvarC
  \melodyDefaults

  \normal g a b b \bar "'" a c b a \soft g4. \bar ","                 % 1
  \normal a4 g a b a( g) g( a) b a( b) \soft a4. \bar "|"             % 2
  \normal b4 c b b a b a \soft g4. \bar ","                           % 3
  \normal b4 b a b a a \soft g4. \bar ","                             % 4
  \normal a4 g a b a( g) g( a) b a( b) \soft a4. \bar "|"             % 5
  \normal g4 a b b \bar "'" b a b c b \bar "'"                        % 6
  b a b a g \soft g4. \bar "|"                                        % 7
  \normal a4 g a b c b b a b a \soft g4. \bar ","                     % 8
  \normal a4 g a b a b a a g a b a g a \soft a4. \bar "|"             % 9
  \normal e4 g a a b a a a g a a( g) \soft g4. \bar "|"               % 10
  \normal g4 a a a a b a^\markup \sans "ret."( g) \soft g4. \fine     % 11
}

text = \lyricmode {
  \markup { \concat { \fontsize #4 "P" \tied-lyric #"" "à-" } }

  ter nos- ter qui es in čae- līs,                                    % 1
  san- cti- fi- cé- tur no- men tu- um;                               % 2
  ad- vèn- i- at reg- num tu- um;                                     % 3
  fi- at vo- lùn- tas tu- a,                                          % 4
  si- cut in čae- lo et in tèr- ra.                                   % 5
  Pa- nem nos- trum quo- ti- di- á- num                               % 6
  da no- bīs hó- di- e;                                               % 7
  et di- mìt- te no- bīs dé- bi- ta nos- tra,                         % 8
  si- cut et nos di- mìt- ti- mus de- bi- tó- ri- bus nos- trīs,      % 9
  et ne nos in- dú- cas in temp- ta- çi- ó- nem,                      % 10
  sed lí- be- ra nos a Mà- lo.                                        % 11
}

\header {
  title = "PÀTER NOSTER"
  tagline = #f
}

\include "../template-post.ly"
