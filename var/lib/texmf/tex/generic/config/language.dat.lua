-- $Id: language.us.lua 18737 2010-06-04 17:09:02Z karl $
--[[
language.us.dat (and the start of language.dat.lua), used by:
- a special luatex version of hyphen.cfg (derived from the babel system);
- a special luatex version of etex.src (from the e-TeX distributon).

See luatex-hyphen.pdf (currently part of the hyph-utf8 package) for details.

DO NOT EDIT THIS FILE (language.dat.lua)! It is generated by tlmgr.
See language.dat (or language.us) for more information.

Warning: formats using this file also use one of language.dat or
language.def. Update them accordingly. The interaction between these
files is documented in luatex-hyphen.pdf, but here is a summary:
- a language must be mentioned in language.dat or language.def to be
available; if, in addition, it is:
  - not mentioned in language.dat.lua, then it is dumped in the format;
  - mentioned in language.dat.lua with a key special="disabled:<reason>",
    then it is not available at all;
  - mentioned in language.dat.lua with a normal entry, then it will not
    be dumped in the format, but loaded at runtime when activated.
]]

return {
	["english"]={
		loader="hyphen.tex",
		special="language0", -- should be dumped in the format
		lefthyphenmin=2,
		righthyphenmin=3,
		synonyms={"usenglish","USenglish","american"},
	},
        -- dumylang and zerohyph are dumped in the format,
        -- since they contain either very few or no patterns at all
-- END of language.us.lua (missing '}' appended after all entries)
  ['gujarati'] = {
    loader = 'loadhyph-gu.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-gu.pat.txt',
    hyphenation = '',
  },
  ['marathi'] = {
    loader = 'loadhyph-mr.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-mr.pat.txt',
    hyphenation = '',
  },
  ['swedish'] = {
    loader = 'loadhyph-sv.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-sv.pat.txt',
    hyphenation = '',
  },
  ['lithuanian'] = {
    loader = 'loadhyph-lt.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-lt.pat.txt',
    hyphenation = '',
  },
  ['indonesian'] = {
    loader = 'loadhyph-id.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-id.pat.txt',
    hyphenation = 'hyph-id.hyp.txt',
  },
  ['panjabi'] = {
    loader = 'loadhyph-pa.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-pa.pat.txt',
    hyphenation = '',
  },
  ['greek'] = {
    loader = 'loadhyph-el-polyton.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = { 'polygreek' },
    patterns = 'hyph-el-polyton.pat.txt',
    hyphenation = '',
  },
  ['irish'] = {
    loader = 'loadhyph-ga.tex',
    lefthyphenmin = 2,
    righthyphenmin = 3,
    synonyms = {  },
    patterns = 'hyph-ga.pat.txt',
    hyphenation = 'hyph-ga.hyp.txt',
  },
  ['piedmontese'] = {
    loader = 'loadhyph-pms.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-pms.pat.txt',
    hyphenation = '',
  },
  ['serbianc'] = {
    loader = 'loadhyph-sr-cyrl.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-sh-latn.pat.txt,hyph-sh-cyrl.pat.txt',
    hyphenation = 'hyph-sh-latn.hyp.txt,hyph-sh-cyrl.hyp.txt',
  },
  ['tamil'] = {
    loader = 'loadhyph-ta.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-ta.pat.txt',
    hyphenation = '',
  },
  ['russian'] = {
    loader = 'loadhyph-ru.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-ru.pat.txt',
    hyphenation = 'hyph-ru.hyp.txt',
  },
  ['icelandic'] = {
    loader = 'loadhyph-is.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-is.pat.txt',
    hyphenation = '',
  },
  ['oriya'] = {
    loader = 'loadhyph-or.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-or.pat.txt',
    hyphenation = '',
  },
  ['kurmanji'] = {
    loader = 'loadhyph-kmr.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-kmr.pat.txt',
    hyphenation = '',
  },
  ['bengali'] = {
    loader = 'loadhyph-bn.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-bn.pat.txt',
    hyphenation = '',
  },
  ['estonian'] = {
    loader = 'loadhyph-et.tex',
    lefthyphenmin = 2,
    righthyphenmin = 3,
    synonyms = {  },
    patterns = 'hyph-et.pat.txt',
    hyphenation = '',
  },
  ['croatian'] = {
    loader = 'loadhyph-hr.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-hr.pat.txt',
    hyphenation = '',
  },
  ['usenglishmax'] = {
    loader = 'loadhyph-en-us.tex',
    lefthyphenmin = 2,
    righthyphenmin = 3,
    synonyms = {  },
    patterns = 'hyph-en-us.pat.txt',
    hyphenation = 'hyph-en-us.hyp.txt',
  },
  ['occitan'] = {
    loader = 'loadhyph-oc.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-oc.pat.txt',
    hyphenation = '',
  },
  ['mongolian'] = {
    loader = 'loadhyph-mn-cyrl.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-mn-cyrl.pat.txt',
    hyphenation = '',
  },
  ['nynorsk'] = {
    loader = 'loadhyph-nn.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-nn.pat.txt',
    hyphenation = 'hyph-nn.hyp.txt',
  },
  ['galician'] = {
    loader = 'loadhyph-gl.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-gl.pat.txt',
    hyphenation = '',
  },
  ['portuguese'] = {
    loader = 'loadhyph-pt.tex',
    lefthyphenmin = 2,
    righthyphenmin = 3,
    synonyms = { 'portuges' },
    patterns = 'hyph-pt.pat.txt',
    hyphenation = 'hyph-pt.hyp.txt',
  },
  ['liturgicallatin'] = {
    loader = 'loadhyph-la-x-liturgic.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-la-x-liturgic.pat.txt',
    hyphenation = '',
  },
  ['turkish'] = {
    loader = 'loadhyph-tr.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-tr.pat.txt',
    hyphenation = '',
  },
  ['turkmen'] = {
    loader = 'loadhyph-tk.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-tk.pat.txt',
    hyphenation = '',
  },
  ['kannada'] = {
    loader = 'loadhyph-kn.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-kn.pat.txt',
    hyphenation = '',
  },
  ['assamese'] = {
    loader = 'loadhyph-as.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-as.pat.txt',
    hyphenation = '',
  },
  ['swissgerman'] = {
    loader = 'loadhyph-de-ch-1901.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-de-ch-1901.pat.txt',
    hyphenation = '',
  },
  ['farsi'] = {
    loader = 'zerohyph.tex',
    lefthyphenmin = 2,
    righthyphenmin = 3,
    synonyms = { 'persian' },
    patterns = '',
  },
  ['dutch'] = {
    loader = 'loadhyph-nl.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-nl.pat.txt',
    hyphenation = 'hyph-nl.hyp.txt',
  },
  ['ukenglish'] = {
    loader = 'loadhyph-en-gb.tex',
    lefthyphenmin = 2,
    righthyphenmin = 3,
    synonyms = { 'british', 'UKenglish' },
    patterns = 'hyph-en-gb.pat.txt',
    hyphenation = 'hyph-en-gb.hyp.txt',
  },
  ['ngerman'] = {
    loader = 'loadhyph-de-1996.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-de-1996.pat.txt',
    hyphenation = '',
  },
  ['slovenian'] = {
    loader = 'loadhyph-sl.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = { 'slovene' },
    patterns = 'hyph-sl.pat.txt',
    hyphenation = '',
  },
  ['sanskrit'] = {
    loader = 'loadhyph-sa.tex',
    lefthyphenmin = 1,
    righthyphenmin = 3,
    synonyms = {  },
    patterns = 'hyph-sa.pat.txt',
    hyphenation = '',
  },
  ['danish'] = {
    loader = 'loadhyph-da.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-da.pat.txt',
    hyphenation = '',
  },
  ['churchslavonic'] = {
    loader = 'loadhyph-cu.tex',
    lefthyphenmin = 1,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-cu.pat.txt',
    hyphenation = 'hyph-cu.hyp.txt',
  },
  ['friulan'] = {
    loader = 'loadhyph-fur.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-fur.pat.txt',
    hyphenation = '',
  },
  ['arabic'] = {
    loader = 'zerohyph.tex',
    lefthyphenmin = 2,
    righthyphenmin = 3,
    synonyms = {  },
    patterns = '',
  },
  ['polish'] = {
    loader = 'loadhyph-pl.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-pl.pat.txt',
    hyphenation = 'hyph-pl.hyp.txt',
  },
  ['hungarian'] = {
    loader = 'loadhyph-hu.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-hu.pat.txt',
    hyphenation = '',
  },
  ['bulgarian'] = {
    loader = 'loadhyph-bg.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-bg.pat.txt',
    hyphenation = '',
  },
  ['finnish'] = {
    loader = 'loadhyph-fi.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-fi.pat.txt',
    hyphenation = '',
  },
  ['hindi'] = {
    loader = 'loadhyph-hi.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-hi.pat.txt',
    hyphenation = '',
  },
  ['monogreek'] = {
    loader = 'loadhyph-el-monoton.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-el-monoton.pat.txt',
    hyphenation = '',
  },
  ['malayalam'] = {
    loader = 'loadhyph-ml.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-ml.pat.txt',
    hyphenation = '',
  },
  ['german-x-2014-05-21'] = {
    loader = 'dehypht-x-2014-05-21.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = { 'german-x-latest' },
    patterns = 'hyph-de-1901.pat.txt',
    hyphenation = 'hyph-de-1901.hyp.txt',
  },
  ['georgian'] = {
    loader = 'loadhyph-ka.tex',
    lefthyphenmin = 1,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-ka.pat.txt',
    hyphenation = '',
  },
  ['slovak'] = {
    loader = 'loadhyph-sk.tex',
    lefthyphenmin = 2,
    righthyphenmin = 3,
    synonyms = {  },
    patterns = 'hyph-sk.pat.txt',
    hyphenation = 'hyph-sk.hyp.txt',
  },
  ['ukrainian'] = {
    loader = 'loadhyph-uk.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-uk.pat.txt',
    hyphenation = '',
  },
  ['mongolianlmc'] = {
    loader = 'loadhyph-mn-cyrl-x-lmc.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    special = 'disabled:only for 8bit montex with lmc encoding',
  },
  ['romanian'] = {
    loader = 'loadhyph-ro.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-ro.pat.txt',
    hyphenation = '',
  },
  ['coptic'] = {
    loader = 'loadhyph-cop.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-cop.pat.txt',
    hyphenation = '',
  },
  ['pinyin'] = {
    loader = 'loadhyph-zh-latn-pinyin.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-zh-latn-pinyin.pat.txt',
    hyphenation = '',
  },
  ['classiclatin'] = {
    loader = 'loadhyph-la-x-classic.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-la-x-classic.pat.txt',
    hyphenation = '',
  },
  ['czech'] = {
    loader = 'loadhyph-cs.tex',
    lefthyphenmin = 2,
    righthyphenmin = 3,
    synonyms = {  },
    patterns = 'hyph-cs.pat.txt',
    hyphenation = 'hyph-cs.hyp.txt',
  },
  ['ibycus'] = {
    loader = 'ibyhyph.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    special = 'disabled:8-bit only',
  },
  ['latvian'] = {
    loader = 'loadhyph-lv.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-lv.pat.txt',
    hyphenation = '',
  },
  ['german'] = {
    loader = 'loadhyph-de-1901.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-de-1901.pat.txt',
    hyphenation = '',
  },
  ['romansh'] = {
    loader = 'loadhyph-rm.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-rm.pat.txt',
    hyphenation = '',
  },
  ['welsh'] = {
    loader = 'loadhyph-cy.tex',
    lefthyphenmin = 2,
    righthyphenmin = 3,
    synonyms = {  },
    patterns = 'hyph-cy.pat.txt',
    hyphenation = '',
  },
  ['thai'] = {
    loader = 'loadhyph-th.tex',
    lefthyphenmin = 2,
    righthyphenmin = 3,
    synonyms = {  },
    patterns = 'hyph-th.pat.txt',
    hyphenation = '',
  },
  ['ngerman-x-2014-05-21'] = {
    loader = 'dehyphn-x-2014-05-21.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = { 'ngerman-x-latest' },
    patterns = 'hyph-de-1996.pat.txt',
    hyphenation = 'hyph-de-1996.hyp.txt',
  },
  ['italian'] = {
    loader = 'loadhyph-it.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-it.pat.txt',
    hyphenation = '',
  },
  ['ethiopic'] = {
    loader = 'loadhyph-mul-ethi.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = { 'amharic', 'geez' },
    patterns = 'hyph-mul-ethi.pat.txt',
    hyphenation = '',
  },
  ['latin'] = {
    loader = 'loadhyph-la.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-la.pat.txt',
    hyphenation = '',
  },
  ['esperanto'] = {
    loader = 'loadhyph-eo.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-eo.pat.txt',
    hyphenation = '',
  },
  ['uppersorbian'] = {
    loader = 'loadhyph-hsb.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-hsb.pat.txt',
    hyphenation = 'hyph-hsb.hyp.txt',
  },
  ['basque'] = {
    loader = 'loadhyph-eu.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-eu.pat.txt',
    hyphenation = '',
  },
  ['afrikaans'] = {
    loader = 'loadhyph-af.tex',
    lefthyphenmin = 1,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-af.pat.txt',
    hyphenation = 'hyph-af.hyp.txt',
  },
  ['serbian'] = {
    loader = 'loadhyph-sr-latn.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-sh-latn.pat.txt,hyph-sh-cyrl.pat.txt',
    hyphenation = 'hyph-sh-latn.hyp.txt,hyph-sh-cyrl.hyp.txt',
  },
  ['catalan'] = {
    loader = 'loadhyph-ca.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-ca.pat.txt',
    hyphenation = 'hyph-ca.hyp.txt',
  },
  ['spanish'] = {
    loader = 'loadhyph-es.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = { 'espanol' },
    patterns = 'hyph-es.pat.txt',
    hyphenation = '',
  },
  ['interlingua'] = {
    loader = 'loadhyph-ia.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-ia.pat.txt',
    hyphenation = 'hyph-ia.hyp.txt',
  },
  ['armenian'] = {
    loader = 'loadhyph-hy.tex',
    lefthyphenmin = 1,
    righthyphenmin = 2,
    synonyms = {  },
    patterns = 'hyph-hy.pat.txt',
    hyphenation = '',
  },
  ['telugu'] = {
    loader = 'loadhyph-te.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-te.pat.txt',
    hyphenation = '',
  },
  ['ancientgreek'] = {
    loader = 'loadhyph-grc.tex',
    lefthyphenmin = 1,
    righthyphenmin = 1,
    synonyms = {  },
    patterns = 'hyph-grc.pat.txt',
    hyphenation = '',
  },
  ['french'] = {
    loader = 'loadhyph-fr.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = { 'patois', 'francais' },
    patterns = 'hyph-fr.pat.txt',
    hyphenation = '',
  },
  ['bokmal'] = {
    loader = 'loadhyph-nb.tex',
    lefthyphenmin = 2,
    righthyphenmin = 2,
    synonyms = { 'norwegian', 'norsk' },
    patterns = 'hyph-nb.pat.txt',
    hyphenation = 'hyph-nb.hyp.txt',
  },
}