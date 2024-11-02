# ライブラリのインポート
from pypdf import PdfReader

# PDFファイルの読み込み
reader = PdfReader("sample.pdf")

# ページ数の取得
number_of_pages = len(reader.pages)

# ページの取得。この場合は、1ページ目を取得する。
page = reader.pages[0]

# テキストの抽出
text = page.extract_text()
print(text)