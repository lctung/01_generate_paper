import os
import json
import math
with open("all_manuscript.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 依據空白字元分割
raw_clean_text = "".join(text.lstrip('\ufeff').split())
exclude_chars = "，。；「」：！？《》、"  # 填入指定刪除的字元

clean_text = "".join([char for char in raw_clean_text if char not in exclude_chars])

unique_characters = set(clean_text)

count = len(unique_characters)

# 建立一個txt檔案並將字元寫入其中
output_file = "characters_history.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for char in unique_characters:
        file.write(char)

print("字元的數量：", count)
print(f"已保存到 {output_file}")


