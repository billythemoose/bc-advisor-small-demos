import requests
import csv
import random
import time
import socket
import http.client
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>', 'html.parser')
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)