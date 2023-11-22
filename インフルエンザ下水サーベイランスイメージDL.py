import requests
from bs4 import BeautifulSoup
import re
import json

# サーベイランスの結果ページのURL
url = "https://www.city.sapporo.jp/gesui/surveillance.html"

# ページの内容を取得
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

image_tag = soup.find('img', src=re.compile(r'graph\d+\-i.jpg$'))
src = image_tag['src']
image_url = "https://www.city.sapporo.jp" + image_tag['src']
image_date = re.search(r'graph(\d+)\-i.jpg$', src).group(1)


# Channel (技術管理/通知)
uri = "https://jsdazure.webhook.office.com/webhookb2/5e899d5d-9748-40ad-bbd1-72b37bda771f@f432b760-3333-434b-801a-26e24f55c413/IncomingWebhook/27edbb3dfddc4f3aa4f6a2be11da1158/0f569ab7-e490-441d-b11d-4776ab6a5bee"

message = "札幌市のインフルエンザ下水サーベイランスの結果です。"
message_with_imageurl = f"{message}({image_date})\n![サーベイランス結果]({image_url})"

# ペイロードの作成
payload = {
    "text": message_with_imageurl
}

# ヘッダー
headers = {
    "Content-Type": "application/json"
}

# POSTリクエストを送信
response = requests.post(uri, data=json.dumps(payload), headers=headers)




