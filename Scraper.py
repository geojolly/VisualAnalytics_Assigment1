import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/areas/nlp/corpora/names/")
c=r.content

