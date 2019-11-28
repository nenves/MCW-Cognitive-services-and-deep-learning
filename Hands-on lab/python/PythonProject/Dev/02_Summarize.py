# # Summarizing Text

# In this notebook, you will get to experiment with performing extraction based summarization of text. This technique of summarization attempts to identify key sentences in a provided text and returns a summary that is the result of returning just those key sentences.
# The process we will follow to summarize text is a subset of the text analytics pipeline that includes these steps:
# - Normalize the text: in this case, simply to clean the text of line break characters. This followed by some simple sentence tokenization, which breaks the paragraph into sentences and removes any extra trailing spaces. Finally the cleaned up text is returned as string.
# - Apply the analytic method: in this case, we use the summarize method provided by the gensim library to generate the summarized result.

# **Please confirm that you have run notebook `01_Initialization` before proceeding**

# ## Task 1 - Import modules
# First, we need to import the modules used by our logic.
# In[6]:


import nltk
import re
import unicodedata
import numpy as np
from gensim.summarization import summarize

# ## Task 2 - Normalize text
# In the following, we define a method that will remove line break characters, tokenize the paragraph of text into an array of string sentences and then strip any extra spaces surrounding a sentence. This is an example of a simple, but typical, text normalization step.

# In[1]:

def clean_and_parse_document(document):
    document = re.sub('\n', ' ', document)
    document = document.strip()
    sentences = nltk.sent_tokenize(document)
    sentences = [sentence.strip() for sentence in sentences]
    return sentences


# ## Task 3 - Summarize text
# In the following, we define a method that uses the summarize method from the gensim module. We take the pre-processed output from our clean_and_parse_document routine and convert the array of string sentences to a single text item by concatenating the sentences. When performing text analytics, some analytic methods might require tokenized input and others may require string input, so this is a common process. In this, the summarize method requires a text string as input.

# In[2]:

def summarize_text(text, summary_ratio=None, word_count=30):
    sentences = clean_and_parse_document(text)
    cleaned_text = ' '.join(sentences)
    summary = summarize(cleaned_text, split=True, ratio=summary_ratio, word_count=word_count)
    return summary 


# ## Task 4 - Try it out
# Author an example string that represents a rather long claim description that Contoso Ltd. might encounter. An example is provided for you, but feel free to provide your own.

# In[3]:


example_document = """
I was driving down El Cäminö and stopped at a red light.
It was about 3pm in the afternoon.  
The sun was bright and shining just behind the stoplight.
This made it hard to see the lights.
There was a car on my left in the left turn lane.
A few moments later another car, a black sedan pulled up behind me. 
When the left turn light changed green, the black sedan hit me thinking 
that the light had changed for us, but I had not moved because the light 
was still red.
After hitting my car, the black sedan backed up and then sped past me.
I did manage to catch its license plate. 
The license plate of the black sedan was ABC123. 
"""


# Now, invoke your summarize_text function against the example document and observe the result.

# In[4]:

clean_and_parse_document_unicode(example_document)


# Observe that the summary is returned as an array of string. If multiple sentences were returned, there would be multiple array entries.

# ## Task 5 - Experiment
# - The summarize text function above defaults to providing a summary that is about 30 words long. What happens if you attempt to summarize the text to 60 words?
# - What happens when you submit a text to summarize that is shorter than the summary target length?

# In[5]:

summarize_text(example_document,5)



