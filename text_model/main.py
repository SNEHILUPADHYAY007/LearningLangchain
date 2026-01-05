import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

# https://aistudio.google.com/
load_dotenv(override=True)

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    print("Google API Key not found")
else:
    print("Google API key found")

# Creating an instance of GoogleGenerativeAI 
llm = GoogleGenerativeAI(model="gemini-2.5-flash-lite")
# print(llm.invoke("Here is a fun fact about pluto:"))

result = llm.generate(["Here is a fun fact about pluto:", "Here is a fun fact about mars:"])
print(result)

print("*" * 50)
for i in result.generations:
    print(i[0].text)
 
