from fastapi import FastAPI
import json
import os

app = FastAPI()

# 데이터 로드
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []

@app.get("/")
def read_root():
    return {"status": "AI Webtoon MCP Server Running", "data_count": len(load_data())}

@app.get("/search/{title}")
def search(title: str):
    data = load_data()
    for item in data:
        if title.lower() in item['title'].lower():
            return item
    return {"error": "Not Found"}
