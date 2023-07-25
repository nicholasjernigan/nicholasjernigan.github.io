# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 19:34:27 2023

Definitions and lists used to webscrape needed details from companies websites.

@author: nicho
"""
import re
#The browser will grab anything that contains these words
relevant_terms = ['platform',
                  'revenue',
                  'service',
                  'COVID',
                  'audit',
                  'finance',
                  'legacy',
                  'software',
                  'solution',
                  'fraud',
                  'anagement',
                  'code',
                  'low',
                  'no',
                  'reservation',
                  'spend',
                  'model',
                  'b2b',
                  'SaaS',
                  'saas',
                  'olution',
                  'tool',
                  'API',
                  'product',
                  'blue',
                  'eneration',
                  'field',
                  'leader']

#These terms that are particularly likely to show up in links.
link_terms = ['olutions',
              'olution',
              'latform',
              'works',
              'Why',
              'why',
              'nsight',
              'eople',
              'mpact',
              'Home',
              'home']

#Only text with at least one of these words will be saved
most_relevant_terms = ['platform',
                  'revenue',
                  'service',
                  'COVID',
                  'audit',
                  'finance',
                  'legacy',
                  'software',
                  'solution',
                  'fraud',
                  'anagement',
                  'code',
                  'low',
                  'no',
                  'reservation',
                  'spend',
                  'model',
                  'b2b',
                  'SaaS',
                  'saas',
                  'olution',
                  'tool',
                  'API',
                  'product',
                  'blue',
                  'eneration',
                  'field',
                  'leader']

def get_relevant_elements_soup(terms,link_specific,soup):
    
    #print('* GRE: Beginning.')
    
    relements = set()
    
    for term in terms:
        pattern = re.compile(f'{term}')
        for element in soup(text=pattern):
            relements.add(element.parent.parent)
    
    #print('* GRE: On to links.')
    
    for link in soup.find_all('a'):
        link_text = link.get_text()
        for term in link_specific:
            if term in link_text:
                relements.add(link)
                break
    relements_list = list(relements)
    
    #print('* GRE: Ready to return.')
    
    return relements_list

def get_relevant_image_links_soup(terms,soup):
    
    #print('~ GRIL: Beginning.')
    
    relevant_links = set()
    image_elements = soup.find_all('img')
    for image_element in image_elements:
        image_parent = image_element.parent
        if image_parent.name != 'a': #################################################
            continue
        alt_text = image_element.get('alt')
        if alt_text is None:
            alt_text = image_element.get('title')
        if alt_text is None:
            continue
        img_relevant = False
        for term in terms:
            if term in alt_text:
                img_relevant = True
        if img_relevant == True:
            url = image_parent.get('href')
        else:
            continue
        if url is None:
            continue
        if 'mailto' in url or '.pdf' in url or 'javascript' in url or 'archive.org' in url:
            continue
        relevant_links.add(url)
        
    #print('~ GRIL: Ready to return.')
    
    return list(relevant_links)
