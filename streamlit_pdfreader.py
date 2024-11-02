import streamlit as st
import os
from PIL import Image
import pyocr
import pyocr.builders

# Tesseractのパスを通す（必要に応じて変更）
path_tesseract = "C:\\Program Files\\Tesseract-OCR"
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract

# OCRエンジンの取得
tools = pyocr.get_available_tools()
if len(tools) == 0:
    st.error("OCRツールが見つかりません。Tesseractがインストールされているか確認してください。")
    st.stop()
tool = tools[0]

st.title("画像OCRリーダー")

# 画像ファイルのアップロード
uploaded_file = st.file_uploader("画像ファイルをアップロードしてください", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # アップロードされた画像をPILで開く
    img_org = Image.open(uploaded_file)
    st.image(img_org, caption="アップロードされた画像", use_column_width=True)

    # OCR実行
    builder = pyocr.builders.TextBuilder()
    result = tool.image_to_string(img_org, lang="jpn", builder=builder)

    # 結果表示
    st.write("抽出されたテキスト:")
    st.write(result)