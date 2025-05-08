from src.webhook import send_message

def main():
    content = "Hello, Discord!"
    send_message(content)
    
if __name__ == "__main__":
    main()