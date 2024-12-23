import os

import dotenv
import requests

from backend.llm.Client import LLM
from backend.llm.prompts import Summarize_Markdown_Prompt
from backend.utils.llmUtils import generateMessage

dotenv.load_dotenv()


def readWebPageWithNoneStream(url, searchQuestion):
    llm = LLM()
    url = f'https://r.jina.ai/{url}'
    headers = {
        'Authorization': f'Bearer {os.getenv("JINA_READER_API_KEY")}',
        'X-Retain-Images': 'none'
    }
    response = requests.get(url, headers=headers)
    message = generateMessage('user', response.text)
    return llm.getCompletion(Summarize_Markdown_Prompt(searchQuestion), [message], tools=None, stream=False).choices[
        0].message.content
