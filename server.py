from fastmcp import FastMCP
import json
import os

# 1. MCP 서버 생성
mcp = FastMCP("WebtoonAnimeExplorer")

# 2. 데이터 로드 함수 (수집한 data.json 읽기)
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# 3. AI가 사용할 도구(Tool) 등록
@mcp.tool()
def search_anime_webtoon(title: str):
    """작품 제목으로 웹툰/애니메이션 정보를 검색합니다."""
    data = load_data()
    for item in data:
        if title.lower() in item['title'].lower():
            return f"제목: {item['title']}\n장르: {', '.join(item['genres'])}\n평점: {item['score']}\n줄거리: {item['synopsis'][:100]}..."
    return "데이터에 해당 작품이 없습니다."

if __name__ == "__main__":
    mcp.run()

