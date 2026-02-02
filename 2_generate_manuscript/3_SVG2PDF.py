from tqdm import tqdm
from os import listdir
import multiprocessing as mp
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import os
import json

with open('info.json', 'r', encoding='utf-8') as f:
    info = json.load(f)
title = info["TITLE"]

def svg2pdf(file):
    drawing = svg2rlg(f"./{title}-Merge/{file}")
    renderPDF.drawToFile(drawing, f"./{title}-PDF/{file}.pdf")


if __name__ == "__main__":
    cpus = mp.cpu_count()  # count of CPU cores
    result_path = f'{title}-PDF' # 存放資料夾
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    print(f"Using {cpus = }")
    pool = mp.Pool(cpus)
    files = listdir(f"./{title}-Merge")
    for _ in tqdm(pool.imap_unordered(svg2pdf, files), total=info["TOTAL_PAGES"]):
        ...
    pool.close()
    pool.join()
