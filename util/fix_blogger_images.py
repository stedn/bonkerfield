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
    soup = None
    with open(f) as page:
        soup = BeautifulSoup(page, "html.parser")
        global_div = soup.find('div', {"dir": "ltr", "trbidi":"on"})
        if global_div:
            global_div.replaceWithChildren()
        [d.decompose() for d in soup.findAll('div', style=re.compile("display:none"))] 
        for div in soup.findAll('div', {"class": "separator"}):
            a = div.a
            if a:
                img = a.img
                if img:
                    img['title'] = div.text +' '+ div.a.text
                    if 'blogspot' in img['src']:
                        src_parts = img['src'].split('/')
                        img_src = '/'.join(src_parts[:-2]+[src_parts[-1]])
                        img['src'] = img_src
                    div.replaceWith(img)
    if soup:
        with open(f, "w") as f_output:
            f_output.write(str(soup)) 