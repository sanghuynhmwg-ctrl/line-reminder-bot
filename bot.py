import requests
import os

TOKEN = os.environ["LINE_TOKEN"]
GROUP_ID = os.environ["GROUP_ID"]

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
