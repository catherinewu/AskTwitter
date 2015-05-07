from nltk.corpus import wordnet as wn

#dog = wordnet.synset('dog')
#print dog.lemma_names

#dictionary
for i,j in enumerate(wn.synsets('dog')):
  print "Meaning",i, "NLTK ID:", j.name
  print "Definition:",j.definition

#thesaurus
for i,j in enumerate(wn.synsets('dog')):
  print "Meaning",i, "NLTK ID:", j.name
  print "Definition:",j.definition
  print "Synonyms:", ", ".join(j.lemma_names)
  print

#ontology
for i,j in enumerate(wn.synsets('dog')):
  print "Meaning",i, "NLTK ID:", j.name
  print "Hypernyms:", ", ".join(list(chain(*[l.lemma_names for l in j.hypernyms()])))
  print "Hyponyms:", ", ".join(list(chain(*[l.lemma_names for l in j.hyponyms()])))
  print