import requests
import os

TOKEN = os.environ["Au/1SVffTM/zzIqPGo0JpTLiNQ4ceQtC+zMcQx/dW1VyzFeUsHmvELUfMPmC1lvVPokZ8BNkek/bF0m5qhjaJBPdaJD8YWW9eJVB8aPnS7+4aoscrCV07EEFVFZYuM4J5pa9CdXuWiWDvo6GBqBApgdB04t89/1O/w1cDnyilFU="]
GROUP_ID = os.environ["C0dc7443ed017d2175c3640e35da88eb9"]

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "to": GROUP_ID,
    "messages": [
        {
            "type": "text",
            "text": "📢 Nhắc nhân viên cập nhật công việc."
        }
    ]
}

r = requests.post(
    "https://api.line.me/v2/bot/message/push",
    headers=headers,
    json=payload
)

print(r.status_code)
print(r.text)