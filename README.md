# Generate Paper
## 環境建置
### 1. 下載專案
點擊右上角綠色 `CODE` --> `DOWNLOAD ZIP`
### 2. 安裝 Conda
點擊 [Anaconda](https://www.anaconda.com/download) 註冊帳號，並安裝 miniconda
### 3. 建立虛擬環境
```
conda create --name gen_paper python=3.8
```
### 4. 開啟虛擬環境
```
conda activate gen_paper
```
### 5. 切換目錄至 `0_env_gen_paper`
```
# 請根據你的目錄位置更改路徑
cd C:\Users\ntut\01-1_generate_paper-main\0_env_gen_paper
```
### 6. 安裝套件
```
pip install -r requirements.txt
```
### 7. 檢查套件
```
conda list
```
- 是否符合 `requirements.txt` 內的套件與版本

-----

## 設定稿紙

### 選擇稿紙內容
- 將該次[作業](https://tjhsieh.github.io/c/ai/ai2026s/hw/index.html)的指定稿紙內容貼至 `manuscript_paper.txt`
- 貼上時，請略過所有來源連結
- 有 **空行**、**空格**、**標點符號** 沒關係

### 切換目錄至 `1_generate_CP950`
```
cd .. 
cd 1_generate_CP950
```

### 刪除稿紙中的不必要字元
```
python 1_preprocess_characters.py
```

### 產生 `CP950.json`
```
python 2_generate_CP950.py
```
- 檢查 `CP950.json` 是否出現指定稿紙內容
----
## 製作包含 CP950 所有字元稿紙

### 切換目錄至 `2_generate_manuscript`
```
cd ..
cd 2_generate_manuscript
```

### 修改 `info.json` 程式碼
```json
"TITLE": "千字文", # check the title
"TOTAL_CHARACTERS": 1000, # check the number of characters
"TOTAL_PAGES": 10, # check the pages
"ID": "你的學號", # enter your ID here
"NAME": "你的名字", # enter your name here
"NUMBER": 0 # enter your number here
```

### 執行程式碼
#### 1. 生成 svg 稿紙
```
python 1_SVGtable.py
```
#### 2. 在 svg 稿紙加上 QRcode
```
python 2_QR_add.py
```
#### 3. svg 轉成 pdf
```
python 3_SVG2PDF.py
```
#### 4. 多個 pdf 檔案合併成一個 pdf 檔案
```
python 4_PDFmerge.py
```
![GITHUB](https://github.com/Circle472/script_ntut/raw/main/scripts_pku_intro.jpg)
