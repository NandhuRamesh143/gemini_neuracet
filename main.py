import os

import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel


def get_news(query):
    response = requests.get(
        "https://newsapi.org/v2/everything",
        params={
            "q": query,
            "apiKey": news_api_key,
            "pageSize": 5,
            "sortBy": "publishedAt",
        },
    )
    data = response.json()
    headlines = []
    for article in data["articles"]:
        headlines.append(article["title"])
    return "\n".join(headlines)


console = Console()
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
news_api_key = os.getenv("newsapi")
news_tool = {
    "function_declarations": [
        {
            "name": "get_news",
            "description": "Get latest news headlines ",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "query": {
                        "type": "STRING",
                        "description": "Topic to search news for",
                    }
                },
                "required": ["query"],
            },
        }
    ]
}
console.print(
    Panel(
        "NeuraCET\nTalk to Gemini",
        title="NeuraCET",
        border_style="blue",
    )
)
client = genai.Client(api_key=api_key)
try:
    while True:
        prompt = console.input("[#FFA500]You>>[/#FFA500]")
        if prompt.lower() == "exit":
            break
        try:
            with console.status("[green]Gemini is thinking..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        tools=[news_tool],
                        system_instruction="""
                        Be concise.
                        Use bullet points when appropriate.
                        Avoid Long explainations.
                        Give direct answers first
                        """,
                    ),
                )
                part = response.candidates[0].content.parts[0]
                if getattr(part, "function_call", None):
                    func_name = part.function_call.name
                    if func_name == "get_news":
                        query = part.function_call.args["query"]
                        news = get_news(query)
                        response = client.models.generate_content(
                            model="gemini-2.5-flash",
                            contents=f"""
                            User asked:
                            {prompt}
                            Latest news:
                            {news}
                            Answer the user's question using ONLY the news provided below.
                            Do not invent headlines.
                            List the headlines as bullet points.
                            """,
                        )

        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
            continue
        console.print(
            Panel(
                Markdown(response.text),
                title="[bold green]Gemini[/bold green]",
                border_style="green",
            )
        )

except KeyboardInterrupt:
    console.print("\nBye;)")
