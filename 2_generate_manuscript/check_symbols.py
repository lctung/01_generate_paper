import os
from fontTools.ttLib import TTFont
import sys
from pathlib import Path

# 加入 root 路徑以讀取 config
sys.path.append(str(Path(__file__).resolve().parents[1]))
import config

def check_font_char_support(target_char):
    target_unicode = ord(target_char)
    print(f"正在檢查字元: {target_char} (U+{target_unicode:04X})\n" + "-"*50)
    
    font_dir = config.DIR_FONTS
    found_any = False
    
    for font_file in os.listdir(font_dir):
        if font_file.lower().endswith(('.ttf', '.otf', '.ttc')):
            path = os.path.join(font_dir, font_file)
            try:
                # 處理 TTC 字體集
                if font_file.lower().endswith('.ttc'):
                    # 檢查 TTC 內的所有字體
                    from fontTools.ttLib import TTCFont
                    ttc = TTCFont(path)
                    for i, font in enumerate(ttc.fonts):
                        cmap = font.getBestCmap()
                        if target_unicode in cmap:
                            print(f"✅ [TTC-{i}] {font_file}")
                            found_any = True
                else:
                    font = TTFont(path)
                    cmap = font.getBestCmap()
                    if target_unicode in cmap:
                        print(f"✅ {font_file}")
                        found_any = True
            except Exception as e:
                continue
                
    if not found_any:
        print("❌ 警告：目前 fonts 資料夾中沒有任何字體支援此字元！")

# 檢查 Triple Dagger (U+2E4B)
check_font_char_support("⹋")