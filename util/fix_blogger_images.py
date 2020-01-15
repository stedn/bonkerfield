from bs4 import BeautifulSoup
import glob
import fileinput
import sys
import re


files = glob.glob('*.html')
for f in files:
    img_src = None
    with open(f) as page:
        soup = BeautifulSoup(page, "html.parser")
        img = soup.find('img')
        if not img:
            break
        img_src = img['src']
        if 'blogspot' in img['src']:
            src_parts = img['src'].split('/')
            img_src = '/'.join(src_parts[:-2]+[src_parts[-1]])
    if img_src:
        for line in fileinput.input([f], inplace=True):
            if line.strip().startswith('image: '):
                line = 'image: '+img_src + '\n'
            sys.stdout.write(line)





files = glob.glob('*.html')
for f in files:
    with open(f) as page:
        soup = BeautifulSoup(page, "html.parser")
        soup.find('div', {"dir": "ltr", "trbidi":"on"}).replaceWithChildren()
        [d.decompose() for d in soup.findAll('div', style=re.compile("display:none;"))] 
        for div in soup.findAll('div', {"class": "separator"}):
            img = div.a.img
            if img:
                img['title'] = div.text +' '+ div.a.text
                
                div.replaceWith(img)
        with open("2014-12-16-daves-grill-2.html", "wb") as f_output:
            f_output.write(soup.prettify("utf-8")) 