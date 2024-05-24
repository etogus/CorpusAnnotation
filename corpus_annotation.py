import en_core_web_sm
import numpy as np
import pandas as pd
import re
from nltk.corpus import words
from collections import Counter
from scipy.stats import pearsonr


# Check if a token should be filtered
def check_to_filter(string):
    pattern_symbols = r"[><_\/\\*]"
    pattern_whitespace = r"\s"
    return len(string) == 0 or re.findall(pattern_symbols, string) or re.match(pattern_whitespace, string)


# Load English language model
en_sm_model = en_core_web_sm.load()

# Read input file: clockwork_orange.txt
user_input = input()
file = open(user_input, 'r')
file_data = file.read()
file.close()

# NLTK English vocabulary
nltk_words = set(words.words())

# Process the text
doc = en_sm_model(file_data)

# Initialize array with column names
data = np.array(['Token', 'Lemma', 'POS', 'Entity_type', 'IOB_tag'])

lemma_devotchka = 0
stem_milk = 0

# Process each token
for token in doc:
    if check_to_filter(token.text):
        continue
    else:
        data = np.vstack([data, [token.text, token.lemma_, token.pos_, token.ent_type_, token.ent_iob_]])
        if token.lemma_ == "devotchka":  # Count lemma 'devotchka'
            lemma_devotchka += 1
        if "milk" in token.text:  # Count tokens with the stem 'milk'
            stem_milk += 1

# Count multi-word named entities
multi_word_entities = sum(1 for ent in doc.ents if len(ent.text.split()) > 1)

# Create DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Find the ten most common non-English words
pos_tags = ['ADJ', 'ADV', 'NOUN', 'VERB']
filtered_words = [
    token.lemma_ for token in doc
    if len(token.lemma_) > 4 and token.lemma_ not in nltk_words and token.pos_ in pos_tags
]
common_non_english_words = dict(Counter(filtered_words).most_common(10))

print(f"Number of multi-word named entities: {multi_word_entities}")
print(f"Number of lemmas 'devotchka': {lemma_devotchka}")
print(f"Number of tokens with the stem 'milk': {stem_milk}")
temp_df = df[['Entity_type']].value_counts()[1:].reset_index().iloc[0]
print(f"Most frequent entity type: {temp_df['Entity_type']}")
mf_ent = df[df['Entity_type'] != '']
temp_df = mf_ent.value_counts().reset_index().iloc[0]
print(f"Most frequent named entity token: {(temp_df['Token'], temp_df['Entity_type'])}")
print(f"Ten most common non-English words: {common_non_english_words}")

# Calculate correlation between NOUN/PROPN POS tags and named entities
df['POS_binary'] = df['POS'].apply(lambda x: 1 if x in ['NOUN', 'PROPN'] else 0)
df['Entity_binary'] = df['Entity_type'].apply(lambda x: 1 if x else 0)
correlation = pearsonr(df['POS_binary'], df['Entity_binary'])[0]
print('Correlation between NOUN and PROPN and named entities: {0:.2f}'.format(correlation))
