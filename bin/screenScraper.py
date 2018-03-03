#!/usr/bin/python

import os
import sys
import logging
from lxml import html
from xml.etree import ElementTree
import requests
import gdata.docs.service

page = requests.get('http://www.google.com')
tree = html.fromstring(page.content)

print "Hello World"

