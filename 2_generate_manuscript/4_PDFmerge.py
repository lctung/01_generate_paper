from tqdm import tqdm
from pikepdf import Pdf
import json

with open('info.json', 'r', encoding='utf-8') as f:
    info = json.load(f)
title = info["TITLE"]

pdfs = [
    Pdf.open(f"./{title}-PDF/{i:03d}.svg.pdf") for i in tqdm(range(1, info["TOTAL_PAGES"] + 1))
]
output = Pdf.new()

for each in tqdm(pdfs):
    output.pages.extend(each.pages)

output.save(f"{info['ID']}_{info['NAME']}.pdf")