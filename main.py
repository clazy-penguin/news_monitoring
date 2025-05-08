from collections import deque
from time import sleep

from src.webhook import send_message
from src.finviz import scrap_finviz
from src.db import insert_data
from src.llm import translate

def main():
    data = scrap_finviz()
    dq = deque()
    for link, title in data:
        try:
            insert_data('news', {'news_url': link})
            dq.appendleft((link, title)) # push 처리
        except Exception as e:
            print(e)
            print(f'중복 뉴스 감지 : {title}')
            break
    for link, title in dq:
        title_ko = translate(title)
        content = f"[{title_ko}]({link})\n"
        content += f"({title})"
        sleep(1)
        send_message(content)

if __name__ == "__main__":
    main()