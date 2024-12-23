from typing import Optional

from openai import OpenAI
import dotenv
import os
dotenv.load_dotenv()
class LLM:
    def __init__(self,model:Optional[str]=None):
        self.model = model if model else 'gpt-4o-mini-2024-07-18'
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),base_url=os.getenv("OPENAI_BASE_URL"))
    def getClient(self):
        return self.client
    def getCompletion (self,systemPrompt,messages,tools,stream):
        client = self.getClient()
        completion = client.chat.completions.create(
            model=self.model,
            stream=stream,
            messages = [{"role":"system","content":systemPrompt}]+messages,
            tools=tools,
        )
        return completion