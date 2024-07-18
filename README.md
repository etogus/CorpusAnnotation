# Corpus Annotation

<p>Any serious NLP experiment requires data processing. In most cases, you use ready-made data, but sometimes you need to compile a corpus yourself. Depending on the task, you may also need certain information about your text: part-of-speech tags, named entities, statistical characteristics, and so on. In this project, raw text is converted into a corpus so it can be used for further analysis.</p>

## Functionality
1. Preprocess the corpus.
2. Print the number of multi-word named entities in the text.
3. Print the number of lemmas of given word.
4. Print the number of tokens that have the given stem.
5. Print the most recurring named entity tag.
6. Print the most recurring named entity token.
7. Print the ten most common words that fall into the criteria described above.
8. Calculate the correlation between both NOUN and PROPN POS tags and named entities according to Pearson's formula and print the result.<br/>

## Example
```
> clockwork_orange.txt
> Number of multi-word named entities: 720
> Number of lemmas 'devotchka': 12
> Number of tokens with the stem 'milk': 5
> Most frequent entity type: LOC
> Most frequent named entity token: ('English', 'LANGUAGE')
> Most common non-English words: {'prestoopnick': 11, 'govoreeting': 10, 'tolchocking': 5, 'crystallography': 4, 'malchickiwick': 3}
> Correlation between NOUN and PROPN and named entities: 0.44
```
