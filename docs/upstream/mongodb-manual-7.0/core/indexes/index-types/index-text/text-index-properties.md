<!-- Converted from core/indexes/index-types/index-text/text-index-properties.txt (reStructuredText). Includes are inlined. -->

# Text Index Properties on Self-Managed Deployments

This page describes the behavior of version 3 
text indexes. 

## Case Insensitivity

Text indexes are case insensitive. The text index does not distinguish between 
capitalized and lower-case characters, such as `e` and `E`. 

Text indexes support case foldings as specified in [Unicode 8.0 Character Database Case Folding](http://www.unicode.org/Public/8.0.0/ucd/CaseFolding.txt): 

- Common C
  
- Simple S

- Special T for Turkish languages

- Characters with diacritics, such as `é` and `É`

- Characters from non-Latin alphabets, such as `И` and `и` in the 
  Cyrillic alphabet.

Previous text index versions are only case 
insensitive for non-diacritic Latin characters `[A-z]`. Previous text index 
versions treat all other characters as distinct.

## Diacritic Insensitivity

Text indexes are diacritic insensitive. The text index does not distinguish 
between characters that contain diacritical marks and their non-marked 
counterparts, such as `é`, `ê`, and `e`. More specifically, the text index 
strips the markings categorized as diacritics in the [Unicode 8.0 Character Database Prop List](http://www.unicode.org/Public/8.0.0/ucd/PropList.txt).

Previous versions of the text index treat 
characters with diacritics as distinct.

## Tokenization Delimiters

For tokenization, text indexes use the delimiters categorized under `Dash`, 
`Hyphen`, `Pattern_Syntax`, `Quotation_Mark`, `Terminal_Punctuation`, 
and `White_Space` in the [Unicode 8.0 Character Database Prop List](http://www.unicode.org/Public/8.0.0/ucd/PropList.txt).

For example, in the string ``Il a dit qu'il «était le meilleur joueur du 
monde»`, the quotation marks (`«`, `»``) and spaces are delimiters.

Previous versions of the index treat `«` as part 
of the term `«était` and `»` as part of the term `monde»`.

## Index Entries

Text indexes tokenize and stem the terms in the indexed fields for the index 
entries. The index uses simple 
language-specific suffix stemming. For 
each document in the collection, the text index stores one index entry for each 
unique stemmed term in each indexed field. 

## Supported Languages and Stop Words

MongoDB supports text search for various languages. Text indexes use simple 
language-specific suffix stemming. Text indexes also drop language-specific stop 
words such as `the`, `an`, `a`, and `and` in English. For a list of the 
supported languages, see text-search-languages.

To specify a language for the text index, see
specify-text-index-language.

## Sparse Property

Text indexes are always sparse. When you create a 
text index, MongoDB ignores the `sparse` option. 

If an existing or newly inserted document lacks a text index 
field (or the field is null or an empty array), MongoDB does not add a text 
index entry for the document.

## Learn More

To learn about text index restrictions, see 
text-index-versions.
