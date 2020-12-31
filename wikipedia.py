#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 00:30:34 2020

@author: jamesdoucette
"""
import requests
from bs4 import BeautifulSoup

def get_page(topic):
    return 'https://en.wikipedia.org/wiki/'+topic

def get_backlinks_page(topic):
    return 'https://en.wikipedia.org/wiki/Special:WhatLinksHere/'+topic

def get_links(topic):
    page = get)page(topics)
    
    response=requests.get(page)
    if response.status_code!=200:
        raise Exception(f'Access error: {response.status_code}')
        
    parsed_response= BeautifulSoup(response.content,'lxml')

def get_backlinks(tipic):
    response=requests.get(page)
    if response.status_code!=200:
        raise Exception(f'Access error: {response.status_code}')
        
    parsed_response= BeautifulSoup(response.content,'lxml')