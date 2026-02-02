# -*- coding: utf-8 -*-
import json
import numpy as np
from tqdm import tqdm
import multiprocessing as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os
import matplotlib.font_manager as fm

'''plt.rcParams["font.sans-serif"] = ["PMingLiU","Mingliu"]  # font family: '細明體MingLiU'
plt.rcParams["axes.unicode_minus"] = False'''
font_path = r"D:\NTUT\AI\Font-Project\01-1_generate_paper-main\2_generate_manuscript\NotoSansTC-ExtraLight.ttf"  # 請根據你的系統修改字型路徑
fm.fontManager.addfont(font_path)
plt.rcParams["font.sans-serif"] = fm.FontProperties(fname=font_path).get_name()

# 讀取 info.json 稿紙字元數 及 頁數
with open('info.json','r', encoding='utf-8') as f:
    info = json.load(f)
total_characters = info["TOTAL_CHARACTERS"]
total_pages = info["TOTAL_PAGES"]
title = info["TITLE"]

def decimal_to_binary(number, digits):
    index = digits - 1
    binaries = [0] * digits
    while number > 0:
        binaries[index] = number % 2  # True / False
        index -= 1
        number >>= 1
    return binaries  # list of booleans


def create_plot(page):
    # figure
    fig = plt.figure(
        num=page, figsize=(8.27, 11.69), dpi=72, facecolor="white"
    )  # figure size (inches)
    axes = plt.subplot(111)

    plt.text(125, 7, "生成式人工智慧導論", fontsize=12.5, color="black")
    student = info["ID"] + "_" + info["NAME"]
    plt.text(85, 7, student, fontsize=12.5, color="black")
    number = info["NUMBER"]
    plt.text(55, 7,"114年度第二學期")

    table_square(axes)

    # page number
    temp_page = page + 1

    plt.text(
        175,
        7,
        "第 {}/{} 頁".format(temp_page, total_pages),
        fontsize=12.5,
        color="black",
    )
    plt.text(
        10,
        8,
        "字順 {}-{}".format(100 * (temp_page - 1) + 1, 100 * temp_page),
        fontsize=17,
        color="black",
    )
    plt.text(88, 285, "頁碼", fontsize=11, color="black")
    rect = patches.Rectangle(
        (98, 279), 58, 9, linewidth=1, edgecolor="black", facecolor="black", fill=False
    )
    axes.add_patch(rect)
    plt.text(158, 285, str(temp_page), fontsize=11, color="black")

    # decimal to binary
    binaries = decimal_to_binary(temp_page, 8)

    # square
    for j, fill in enumerate(binaries):
        rect = patches.Rectangle(
            (100 + 7 * j, 281),
            5,
            5,
            linewidth=1,
            edgecolor="black",
            facecolor="black",
            fill=fill,
        )
        axes.add_patch(rect)

    plt.text(8, 285, "編號", fontsize=11, color="black")
    rect = patches.Rectangle(
        (18, 279), 58, 9, linewidth=1, edgecolor="black", facecolor="black", fill=False
    )
    axes.add_patch(rect)
    plt.text(78, 285, str(number), fontsize=11, color="black")

    # decimal to binary
    binaries = decimal_to_binary(number, 8)

    # number square
    for j, fill in enumerate(binaries):
        rect = patches.Rectangle(
            (20 + 7 * j, 281),
            5,
            5,
            linewidth=1,
            edgecolor="black",
            facecolor="black",
            fill=fill,
        )
        axes.add_patch(rect)

def read_json(file):
    with open(file) as f:
        try:
            p = json.load(f)
        except UnicodeDecodeError:
            # Handle the UnicodeDecodeError here (e.g., print a message, log it, or skip the file).
            print(f"Error reading JSON file: {file}")
            return []
        
        v = [""] * total_characters
        for i in range(total_characters):
            try:
                code = p["CP950"][i]["UNICODE"][2:6]
                v[i] = "\\u{}".format(code)
            except Exception as e:
                # Handle the exception here (e.g., print a message, log it, or skip the entry).
                print(f"Error processing entry {i}: {str(e)}")
                v[i] = ""  # You can decide what to do in case of an error.
        return v

def print_font(count, page, fnip):
    index = 0
    X = np.arange(7.5, 192.5, 20)
    Y = np.arange(21, 281, 26)
    for j in range(10):
        for i in range(10):
            if count >= total_characters:
                plt.text(X[i], Y[j] - 2, "", fontsize=15, color="black", alpha=0.7)
                # plt.text(12.5+16.25*j, 23+17*i, '', fontsize=32, color='black')
            else:
                if unicode[count] == "123" or count >= total_characters:
                    plt.text(X[i], Y[j] - 2, "", fontsize=15, color="black", alpha=0.7)
                    fnip[page][index] = ""  # 第(page+1)頁 第(index+1)個字
                    # plt.text(7+16.25*j, 26.7+17*i, '\\u25A0'.encode('ascii').decode('unicode-escape'), fontsize=64, color='black')
                else:
                    plt.text(
                        X[i] + 1,
                        Y[j] - 3,
                        unicode[count].encode("ascii").decode("unicode-escape"),
                        fontsize=14,
                        color="black",
                        alpha=0.7,
                    )
                    plt.text(
                        X[i] + 8.5,
                        Y[j] - 3,
                        unicode[count][2:6],
                        fontsize=8,
                        color="black",
                        alpha=0.7,
                    )
                    fnip[page][index] = unicode[count][2:6]
                index += 1
            count += 1

            
def table_square(axes):
    X = np.arange(7.5, 192.5, 20)
    Y = np.arange(21, 281, 26)
    for j in range(10):
        for i in range(10):
            rect = patches.Rectangle(
                (X[i], Y[j]),
                15,
                15,
                linewidth=1,
                #edgecolor="#9ACD32",
                edgecolor="#000000",
                alpha=1,
                #facecolor="black",
                facecolor="#3C3C3C",
                fill=False,
            )
            axes.add_patch(rect)

            # 書寫輔助虛線
            # axes.plot([X[i]+7.5, X[i]+7.5], [Y[j], Y[j]+15], linewidth=0.4, color='#9ACD32', alpha=0.6, linestyle='--', dashes=(8, 8))
            # axes.plot([X[i], X[i]+15], [Y[j]+7.5, Y[j]+7.5], linewidth=0.4, color='#9ACD32', alpha=0.6, linestyle='--', dashes=(8, 8))
            # axes.plot([X[i], X[i]+15], [Y[j]+12, Y[j]+12], linewidth=0.4, color='#9ACD32', alpha=0.6, linestyle='--', dashes=(8, 8))

            axes.plot(
                [X[i] + 0.5, X[i] + 2],
                [Y[j] - 7.5, Y[j] - 7.5],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )  ## v
            axes.plot(
                [X[i] + 5, X[i] + 6.5],
                [Y[j] - 7.5, Y[j] - 7.5],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )
            axes.plot(
                [X[i] + 0.5, X[i] + 2],
                [Y[j] - 1.5, Y[j] - 1.5],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )
            axes.plot(
                [X[i] + 5, X[i] + 6.5],
                [Y[j] - 1.5, Y[j] - 1.5],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )
            axes.plot(
                [X[i] + 0.5, X[i] + 0.5],
                [Y[j] - 7.5, Y[j] - 6],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )  ## h
            axes.plot(
                [X[i] + 0.5, X[i] + 0.5],
                [Y[j] - 3, Y[j] - 1.5],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )
            axes.plot(
                [X[i] + 6.5, X[i] + 6.5],
                [Y[j] - 7.5, Y[j] - 6],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )
            axes.plot(
                [X[i] + 6.5, X[i] + 6.5],
                [Y[j] - 3, Y[j] - 1.5],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )

        axes.plot(
            [5, 205],
            [Y[j] + 16.5, Y[j] + 16.5],
            linewidth=0.3,
            color="black",
            alpha=0.4,
        )  ## vvvv


def output_svg(filename):
    plt.axis("off")  # 刪除座標軸
    plt.xlim(0, 210)
    plt.ylim(297, 0)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)  # 刪除白邊
    plt.margins(0, 0)
    plt.savefig(f"./{title}-Table/{filename}.svg")

def pipeline(args):
    (page, count) = args
    try:
        create_plot(page)
        print_font(count, page, fnip)
        output_svg("{:03d}".format(page + 1))
    finally:
        plt.close('all')


fnip = [[""] * 100 for _ in range(total_pages)]  # Font Number in Page (Unicode)
unicode = read_json("./CP950.json")

if __name__ == "__main__":
    cpus = mp.cpu_count()  # count of CPU cores
    result_path = f'Table' # 存放資料夾
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    print(f"Using {cpus = }")
    pool = mp.Pool(cpus)
    args = zip(range(0, total_pages), range(0, total_pages * 100 + 1, 100))
    for _ in tqdm(pool.imap_unordered(pipeline, args), total=total_pages):
        ...
    pool.close()
    pool.join()