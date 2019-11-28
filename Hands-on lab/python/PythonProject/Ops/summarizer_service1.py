import re
import nltk
import unicodedata
from gensim.summarization import summarize, keywords
import numpy as np
from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
import json

def clean_and_parse_document(document):
    if isinstance(document, str):
        document = document
    elif isinstance(document, unicode):
        return unicodedata.normalize('NFKD', document).encode('ascii', 'ignore')
    else:
        raise ValueError("Document is not string or unicode.")
    document = document.replace("\\n", "").strip()
    document_lines = document.splitlines()
    document = ''.join(document_lines)
    sentences = nltk.sent_tokenize(document)
    sentences = [sentence.strip() for sentence in sentences]
    return sentences

def summarize_text(text, summary_ratio=0.3, word_count=None):
    sentences = clean_and_parse_document(text)
    cleaned_text = ' '.join(sentences)
    summary = summarize(cleaned_text, split=True, ratio=summary_ratio, word_count=word_count)
    return summary 

def init():  
    nltk.download('all')
    return

def run(data):
    try:
        data = json.loads(data)
        text = str(data["text"])
        word_count = None if data["count"] == 'None' else int(data["count"])
        summary_ratio = None if data["ratio"] == 'None' else float(data["ratio"])
        return summarize_text(text=text, summary_ratio=summary_ratio, word_count=word_count)
    except Exception as e:
        return (str(e))
