from dotenv import load_dotenv
import os
import requests
from google import genai


load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
news_api_key=os.getenv("newsapi")
print('what would like to do')
print('1.Talk to GEMINI\n2.Get Top Tech Headlines')
choice=int(input("Enter choice:"))
if (choice==1):
    client=genai.Client(api_key=api_key)
    while(True):
        prompt=input("Enter Your Prompt:")
        if prompt.lower()=="exit":
            break
        response=client.models.generate_content(model="gemini-2.5-flash",contents=prompt)
        print(response.text)
        
elif (choice==2):    
    response=requests.get("https://newsapi.org/v2/top-headlines",params={"category":"technology","apiKey":news_api_key,"pageSize":5})

    data = response.json()
    for article in data["articles"]:
        print(article["title"])
