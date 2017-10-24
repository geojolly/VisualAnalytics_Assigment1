#The project aim to get the data from web and supplement it with gender data
import pandas as pd

#read the dataset
f=pd.read_csv("/Users/geojolly/Downloads/IEEE VIS papers 1990-2016 - Main dataset.csv")

#keep only relevant entries
keep_col = ['Conference','Year','Author Names','Author Affiliation','Author Keywords']
new_f = f[keep_col]
new_f.to_csv("/Users/geojolly/Desktop/IT4BI_1/VisualAnalytics/Assignment1/result.csv", index=False)

#for scraping the link
from bs4 import BeautifulSoup
import requests

#extraction of the links
r  = requests.get("http://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/areas/nlp/corpora/names/")
data = r.text
soup = BeautifulSoup(data)
links=[]
for link in soup.find_all('a'):
    links.append(link.get('href'))

#saving the file locally
import csv
import itertools

def text2csv(name):

    with open(name+'.txt', 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line for line in stripped if line)
        grouped = zip(*[lines] * 1)
        with open(name+'.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('Name', 'Sex'))
            writer.writerows(grouped)

#save links locally as csv files
for link in links[7:8]:
    text2csv(link)

def append_sex(val):
    with open(val+'csv', 'r') as csvinput:
        with open('output'+val+'.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            all = []
            row = next(reader)
            all.append(row)

            for row in reader:
                row.append(val)
                all.append(row)

            writer.writerows(all)

for link in links[7:8]:
    append_sex(link)

#merging the csv file into one.
import csv
reader = csv.reader(open('output_male.csv', 'r'))
reader1 = csv.reader(open('output_female.csv', 'r'))
writer = csv.writer(open('appended_output.csv', 'w'))
for row in reader:
    writer.writerow(row)
for row1 in reader1:
    writer.writerow(row1)


#sorting the file
import pandas as pd
df = pd.read_csv('appended_output.csv')
df = df.sort('Name')
df.to_csv('Database_Gender.csv', index=False)

#genderguesser api test
#import gender_guesser.detector as gender
#d = gender.Detector()
