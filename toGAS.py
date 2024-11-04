import requests
col1 = "2列目へのテスト送信"
col2 = "3列目へのテスト送信"
def gas_call():
    url =f"https://script.google.com/macros/s/AKfycbynwb1Lsie3v0zWSMb839lKxZjPjpLHj90MTRqiW4fFKk0eF4amWGorN7rP0XO5vnTbIA/exec?data_col1={col1}&data_col2={col2}"
    requests.get(url)
if __name__ == '__main__':
    gas_call()
