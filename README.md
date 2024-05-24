<p>Any serious NLP experiment requires data processing. In most cases, you use ready-made data, but sometimes you need to compile a corpus yourself. Depending on the task, you may also need certain information about your text: part-of-speech tags, named entities, statistical characteristics, and so on. In this project, raw text is converted into a corpus so it can be used for further analysis.</p>

Program has the the following functionality:<br/>
> Preprocess the corpus<br/>
> Print the number of multi-word named entities in the text;<br/>
> Print the number of lemmas devotchka;<br/>
> Print the number of tokens that have the stem milk inside;<br/>
> Print the most recurring named entity tag;<br/>
> Print the most recurring named entity (token);<br/>
> Print the ten most common words that fall into the criteria described above;<br/>
> Calculate the correlation between both NOUN and PROPN POS tags and named entities according to Pearson's formula and print the result.<br/><br/>

Example<br/>
> clockwork_orange.txt<br/>
> Number of multi-word named entities: 720<br/>
> Number of lemmas 'devotchka': 12<br/>
> Number of tokens with the stem 'milk': 5<br/>
> Most frequent entity type: LOC<br/>
> Most frequent named entity token: ('English', 'LANGUAGE')<br/>
> Most common non-English words: {'prestoopnick': 11, 'govoreeting': 10, 'tolchocking': 5, 'crystallography': 4, 'malchickiwick': 3}<br/>
> Correlation between NOUN and PROPN and named entities: 0.44
