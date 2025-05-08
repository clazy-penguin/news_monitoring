from src.webhook import send_message
from src.finviz import scrap_finviz
from src.db import insert_data
from collections import deque
from time import sleep

def main():
    data = scrap_finviz()
    dq = deque()
    for link, title in data:
        try:
            insert_data('news', {'news_url': link})
            dq.appendleft((link, title)) # push 처리
        except:
            print('중복 뉴스 감지')
            break
    for link, title in dq:
        content = f"[{title}]({link})\n".strip()
        sleep(1)
        send_message(content)

if __name__ == "__main__":
    main()