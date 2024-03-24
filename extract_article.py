#!/usr/bin/env python
# coding: utf-8

import json, os, re

from bs4 import BeautifulSoup
import numpy as np
import requests
from requests.models import MissingSchema
import trafilatura
import spacy


# Define web page url
url = 'https://www.theguardian.com/uk-news/2023/sep/08/what-a-year-of-king-charles-has-shown-us-about-how-he-wants-to-reign'


# Define Beautifulsoup fallback function for cases when Trafilatura is unable to extract text
def extract_text_fallback(response_content):
    
    # Create the beautifulsoup object
    soup = BeautifulSoup(response_content, 'html.parser')
    
    # Find the text:
    text = soup.find_all(text=True)
    
    # Remove unwanted tag elements
    cleaned_text = ''
    unwanted_tags = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script',
        'style',]

    # Extract text, ignoring unwanted tags
    for item in text:
        if item.parent.name not in unwanted_tags:
            cleaned_text += '{} '.format(item)
            
    # Remove any tab separation and strip the text
    cleaned_text = cleaned_text.replace('\t', '')
    return cleaned_text.strip()
    
# Define extract function, Trafilatura with callback function
def extract_text(url):
    
    downloaded_url = trafilatura.fetch_url(url)
    try:
        extracted_content = trafilatura.extract(downloaded_url, output_format='json', with_metadata=True, include_comments = False,
                            date_extraction_params={'extensive_search': True, 'original_date': True})
    except AttributeError:
        extracted_content = trafilatura.extract(downloaded_url, output_format='json', with_metadata=True,
                            date_extraction_params={'extensive_search': True, 'original_date': True})
    if extracted_content:
        json_output = json.loads(extracted_content)
        return json_output['text']
    else:
        try:
            # Obtain the response
            resp = requests.get(url)
            # Check if the response status is 200 - Status OK, collect HTML Content
            if resp.status_code == 200:
                return extract_text_fallback(resp.content)
            else:
                # If both Trafilature and BeautifulSoup functions fail
                return np.nan
        # Handle any URLs that don't have the correct protocol
        except MissingSchema:
            return np.nan



# Extract parsed text
final_article_text = extract_text(url)

# print(final_article_text)


# Convert text into spacy tokens doc
nlp = spacy.load("en_core_web_sm")
doc=nlp(final_article_text)
# print(doc)


# Check the word count per text document
print(f"The estimated word count for this document is: {len(doc)}.\n")
# Check the number of sentences
print(f"The estimated number of sentences in the document is: {len(list(doc.sents))}.")


# Extract article's title from the first sentence
for sent_i in enumerate(doc.sents):
  sent_i
first_sentence = str(f"{list(doc.sents)[0]}")
first_sentence = first_sentence.replace(' ','_')
first_sentence = re.sub('\n.*','',first_sentence)
article_first_sentence = re.sub('[?!\\/:*|\"\'<>]','',first_sentence).split(',')[0]
print(f"The article's first sentence is: {article_first_sentence}")


# Extract article's title from tag

## Obtain the response
resp = requests.get(url)
## Get Content
soup = BeautifulSoup(resp.content, 'html.parser')
## Get title
title = soup.find('title').string.split('|')[0]
article_title = title.replace(' ','_')
print(f"The article's title is: {article_title}")


# Check working directory
os.getcwd()


# Save scraped article to file

## Name with title
file = open(f"{article_title}.txt",'w', encoding="utf-8")
file.write(final_article_text)
file.close()

# ## Name with the first sentence
# file = open(f"{article_first_sentence}.txt",'w')
# file.write(final_article_text)
# file.close()