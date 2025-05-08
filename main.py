from src.webhook import send_message
from src.finviz import scrap_finviz

def main():
    data = scrap_finviz()
    for link, title in data:
        content = f"[{title}]({link})\n".strip()
        send_message(content)

if __name__ == "__main__":
    main()