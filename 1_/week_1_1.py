import openai
from dotenv import load_dotenv
import os

load_dotenv(override=True)

openai_key = os.getenv("OPENAI_API_KEY")


















if __name__ == "__main__":
    print(openai_key)