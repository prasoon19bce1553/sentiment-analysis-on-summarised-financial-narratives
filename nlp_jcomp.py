# -*- coding: utf-8 -*-
"""NLP_JComp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wwTpR1rrXlfDFuBhpqDcgyCEGjRXhO0c

# Abstractive Summarization
"""

!pip install SentencePiece

!pip install transformers

from transformers import PegasusTokenizer, PegasusForConditionalGeneration, TFPegasusForConditionalGeneration

model_name = "human-centered-summarization/financial-summarization-pegasus"
tokenizer=PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)

#open text file in read mode
text_file_A = open("fcurren_risk.txt", "r")
#read whole file to a string
dataA = text_file_A.read()
#close file
text_file_A.close()

#open text file in read mode
text_file_B = open("interest_rate_risk.txt", "r")
#read whole file to a string
dataB = text_file_B.read()
#close file
text_file_B.close()

#open text file in read mode
text_file_C = open("equity_risk.txt", "r")
#read whole file to a string
dataC = text_file_C.read()
#close file
text_file_C.close()

text_to_summarize_A = dataA
text_to_summarize_B = dataB
text_to_summarize_C = dataC
# Tokenize our text
# If you want to run the code in Tensorflow, please remember to return the particular tensors as simply as using return_tensors = 'tf'
input_ids_A = tokenizer(text_to_summarize_A, return_tensors="pt").input_ids
input_ids_B = tokenizer(text_to_summarize_B, return_tensors="pt").input_ids
input_ids_C = tokenizer(text_to_summarize_C, return_tensors="pt").input_ids

output_A = model.generate(
    input_ids_A, 
    max_length=50, 
    num_beams=5, 
    early_stopping=True
)
output_B = model.generate(
    input_ids_B, 
    max_length=50, 
    num_beams=5, 
    early_stopping=True
)
output_C = model.generate(
    input_ids_C, 
    max_length=50, 
    num_beams=5, 
    early_stopping=True
)

print("Foreign currency risks")
print(tokenizer.decode(output_A[0], skip_special_tokens=True))
print("Interest Rate risks")
print(tokenizer.decode(output_B[0], skip_special_tokens=True))
print("Equity Investment risks")
print(tokenizer.decode(output_C[0], skip_special_tokens=True))

"""# Text Summarization"""

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
nlp= spacy.load("en_core_web_sm")

"""Foreign currency risks"""

doc=nlp(dataA)
tokens=[token.text for token in doc]
punctuation=punctuation+'n'
word_freq={}
stop_words= list(STOP_WORDS)

for word in doc:
   if word.text.lower() not in stop_words:
     if word.text.lower() not in punctuation:
       if word.text not in word_freq.keys():
         word_freq[word.text]= 1
       else:
         word_freq[word.text]+= 1 
print(word_freq)

x=(word_freq.values())
a=list(x)
a.sort()
max_freq=a[-1]
max_freq

for word in word_freq.keys():
   word_freq[word]=word_freq[word]/max_freq 
print(word_freq)

sent_score={}
sent_tokens=[sent for sent in doc.sents]
print(sent_tokens)

for sent in sent_tokens:
   for word in sent:
     if word.text.lower() in word_freq.keys():
       if sent not in sent_score.keys():
         sent_score[sent]=word_freq[word.text.lower()]
       else:
         sent_score[sent]+= word_freq[word.text.lower()] 
print(sent_score)

from heapq import nlargest
len(sent_score) *0.3
summary=nlargest(n=13,iterable=sent_score,key=sent_score.get)
print(summary)

final_summary=[word.text for word in summary]
final_summary

summary=''.join(final_summary)
DataA=summary

"""Interest Rate risks"""

doc=nlp(dataB)
tokens=[token.text for token in doc]
punctuation=punctuation+'n'
word_freq={}
stop_words= list(STOP_WORDS)

for word in doc:
   if word.text.lower() not in stop_words:
     if word.text.lower() not in punctuation:
       if word.text not in word_freq.keys():
         word_freq[word.text]= 1
       else:
         word_freq[word.text]+= 1 
print(word_freq)

x=(word_freq.values())
a=list(x)
a.sort()
max_freq=a[-1]
max_freq

for word in word_freq.keys():
   word_freq[word]=word_freq[word]/max_freq 
print(word_freq)

sent_score={}
sent_tokens=[sent for sent in doc.sents]
print(sent_tokens)

for sent in sent_tokens:
   for word in sent:
     if word.text.lower() in word_freq.keys():
       if sent not in sent_score.keys():
         sent_score[sent]=word_freq[word.text.lower()]
       else:
         sent_score[sent]+= word_freq[word.text.lower()] 
print(sent_score)

from heapq import nlargest
len(sent_score) *0.3
summary=nlargest(n=13,iterable=sent_score,key=sent_score.get)
print(summary)

final_summary=[word.text for word in summary]

summary=''.join(final_summary)
DataB = summary

"""Equity Investment risks"""

doc=nlp(dataC)
tokens=[token.text for token in doc]
punctuation=punctuation+'n'
word_freq={}
stop_words= list(STOP_WORDS)

for word in doc:
   if word.text.lower() not in stop_words:
     if word.text.lower() not in punctuation:
       if word.text not in word_freq.keys():
         word_freq[word.text]= 1
       else:
         word_freq[word.text]+= 1 
print(word_freq)

x=(word_freq.values())
a=list(x)
a.sort()
max_freq=a[-1]
max_freq

for word in word_freq.keys():
   word_freq[word]=word_freq[word]/max_freq 
print(word_freq)

sent_score={}
sent_tokens=[sent for sent in doc.sents]
print(sent_tokens)

for sent in sent_tokens:
   for word in sent:
     if word.text.lower() in word_freq.keys():
       if sent not in sent_score.keys():
         sent_score[sent]=word_freq[word.text.lower()]
       else:
         sent_score[sent]+= word_freq[word.text.lower()] 
print(sent_score)

from heapq import nlargest
len(sent_score) *0.3
summary=nlargest(n=13,iterable=sent_score,key=sent_score.get)
print(summary)

final_summary=[word.text for word in summary]

summary=''.join(final_summary)
DataC=summary

"""# Summarization Using Sumy"""

!pip install sumy

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenize
file = 'fcurren_risk.txt' 
parser = PlaintextParser.from_file(file, Tokenize('english'))

from sumy.summarizers.lsa import LsaSummarizer
summarizer_2 = LsaSummarizer()
summary_2 =summarizer_2(parser.document,2)
for sentence in summary_2:
 print(sentence)

"""# Sentiment Analysis"""

!pip install spacytextblob

!pip install -U pip setuptools wheel
!pip install -U spacy

!pip install language-tool-python

!pip install spacytextblob
!python -m textblob.download_corpora
!python -m spacy download en_core_web_sm

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

def senti(text):
  doc = nlp(text)
  """
  print(doc._.blob.polarity)                            
  print(doc._.blob.subjectivity)"""
  if (doc._.blob.polarity>-1 and doc._.blob.polarity <-0.5):
    print("Very Negative")
  elif (doc._.blob.polarity>-0.5 and doc._.blob.polarity <0):
    print("Negative")
  elif (doc._.blob.polarity>0 and doc._.blob.polarity <0.5):
    print("Neutral")
  elif (doc._.blob.polarity>0.5 and doc._.blob.polarity <-0.5):
    print("Positive")
  elif (doc._.blob.polarity>-1 and doc._.blob.polarity <-0.5):
    print("Very Positive")  
  if (doc._.blob.subjectivity>0 and doc._.blob.subjectivity <0.5):
    print("Opinionated")
  elif (doc._.blob.subjectivity>0.5 and doc._.blob.subjectivity <1):
    print("General")

senti(DataA)
senti(DataB)
senti(DataC)