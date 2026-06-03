def generate_from_llm(prompt):
    return f"""
# GENERATED OUTPUT

{prompt}
"""














#from openai import OpenAI
#import os
#from dotenv import load_dotenv

# IMPORTANT: load .env FIRST
#load_dotenv()

#api_key = os.getenv("OPENAI_API_KEY")

#if not api_key:
 #   raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

#client = OpenAI(api_key=api_key)

#def generate_from_llm(prompt: str) -> str:
 #   response = client.chat.completions.create(
  #      model="gpt-5",
   #     messages=[{"role": "user", "content": prompt}],
    #    temperature=0.2,
    #)

    #return response.choices[0].message.content