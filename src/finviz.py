def scrap_finviz() -> list:
    from bs4 import BeautifulSoup
    finviz_url = 'https://finviz.com/news.ashx'
    finviz_html = get_html_from_url(finviz_url)
    finviz_soup = BeautifulSoup(finviz_html, 'lxml')
    table_selector = 'table.styled-table-new'
    table = finviz_soup.select_one(table_selector)
    rows = table.select('a')
    result = []
    for row in rows:
        result.append((
            row['href'],
            row.get_text(strip=True),           
        ))
    return result

def get_html_from_url(url : str) -> str:
    import requests
    # response = requests.get(url) # 403
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    response.raise_for_status()
    return response.text