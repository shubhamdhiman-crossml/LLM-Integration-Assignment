import os

from google import genai
from google.genai import types
from PIL import Image

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

prompt =  "Gie me the details of  object present inside the  room"

image = Image.open("image.png")

response1 = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = [prompt, image],

 config = types.GenerateContentConfig(
        temperature = 0.8,
        top_p = 0.9,
        top_k = 40
    )
)    
print(response1.text)
prompt2=  "This is my living room and there is a dining table inside that room can you suggest me what more I can do to enhance the ambience of the room"

response2 = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = [prompt2, image],

 config = types.GenerateContentConfig(
        temperature = 0.8,
        top_p = 0.9,
        top_k = 40
    ) 
)    
print(response2.text)

prompt3 = "There is a dining table in the room if someone wants to eat something healthy than what dishes can be served on the table"

response3 = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = [prompt3, image],

  config =  types.GenerateContentConfig(
         temperature = 0.8,
         top_p = 0.9,
         top_k = 50
    )  
)
print(response3.text)