from bs4 import BeautifulSoup
import glob
import fileinput
import sys


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
