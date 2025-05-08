def send_message(content: str) -> None:
    import requests
    import os
    from dotenv import load_dotenv
    load_dotenv()
    url = os.getenv("DISCORD_WEBHOOK_URL")
    # content = "Hello, Discord!"
    response = requests.post(url, json={"content": content})
    if response.status_code == 204:
        print("메시지 전송 성공")
    else:
        # 일정 이상 대기가 필요해 보임
        print("메시지 전송 실패")