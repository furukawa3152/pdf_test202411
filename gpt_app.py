import streamlit as st
import base64
import requests
import json
# OpenAI API Keyの入力
api_key = st.text_input("OpenAI API Keyを入力してください", type="password")


# 画像のエンコード関数
def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')


st.title("名刺解析アプリ")

# 画像ファイルのアップロード
uploaded_file = st.file_uploader("画像をアップロードしてください", type=["jpg", "jpeg", "png"])

if uploaded_file is not None and api_key:
    # 画像をエンコード
    base64_image = encode_image(uploaded_file)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "画像を与えます。内容を読み取り、文字情報をすべて返して下さい。"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    # APIリクエストの送信
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # 結果の表示
    if response.status_code == 200:
        result = response.json()
        st.json(result)  # JSONとして結果を表示
    else:
        st.error(f"APIエラー: {response.status_code}")
        st.write(response.json())
else:
    st.info("APIキーと画像ファイルの両方を入力してください")