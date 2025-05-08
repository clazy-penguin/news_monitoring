def main():
    import requests
    import os
    from dotenv import load_dotenv
    load_dotenv()
    url = os.getenv("DISCORD_WEBHOOK_URL")
    content = "Hello, Discord!"
    requests.post(url, json={"content": content})
    
if __name__ == "__main__":
    main()