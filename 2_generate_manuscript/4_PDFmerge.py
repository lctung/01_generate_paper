from tqdm import tqdm
from pikepdf import Pdf
import json
import os

with open('info.json', 'r', encoding='utf-8') as f:
    info = json.load(f)
title = info["TITLE"]
stu_id = info['ID']
stu_name = info['NAME']

pdfs = [
    Pdf.open(f"{title}/{title}-PDF/{i:03d}.svg.pdf") for i in tqdm(range(1, info["TOTAL_PAGES"] + 1))
]
output = Pdf.new()

for each in tqdm(pdfs):
    output.pages.extend(each.pages)

result_path = 'manuscripts-final'
if not os.path.exists(result_path):
    os.makedirs(result_path)

output.save(f"{result_path}/{stu_id}_{stu_name}_{title}.pdf")