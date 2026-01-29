import os
import json
import math
with open("manuscript_paper.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 依據空白字元分割
clean_text = "".join(text.lstrip('\ufeff').split())

# 建立一個txt檔案並將字元寫入其中
output_file = "chinese_character.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for char in clean_text:
        file.write(char)

# 計算稿紙字元的數量
count = len(clean_text)
pages = math.ceil(count/100)

# 將 總字元數 + 稿紙頁數 寫入 info.json 方便稿紙生成調用
paper_info_path = "D:\\NTUT\\AI\\Font-Project\\01-1_generate_paper-main\\2_generate_manuscript\\info.json"
os.makedirs(os.path.dirname(paper_info_path), exist_ok=True)

with open(paper_info_path, 'r', encoding='utf-8') as f:
    info = json.load(f)

info["TOTAL_CHARATERS"] = count
info["TOTAL_PAGES"] = pages

with open(paper_info_path, 'w', encoding="utf-8") as f:
    json.dump(info, f, indent=4, ensure_ascii=False)

print("字元的數量:", count)
print(f"已保存到 {output_file}")
print("info.json 更新完畢")


