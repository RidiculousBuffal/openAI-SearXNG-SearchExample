# OpenAI functionCall WebSearch Example
> In this case, we use **Searxng**,**Jira Reader**,**OpenAI** to build a single example using recursive function call


## Prerequisites
- Python 3.10
- OpenAI API Key
- Searxng Instance
    - You can reference this link [Open Web UI Reference](https://docs.openwebui.com/tutorials/integrations/web_search/#searxng-docker)
- Jina Reader API Key
    - Get Your API Key here : [API KEY](https://jina.ai/reader)
## Installation
- Install the required packages:
```Bash
pip install -r requirements.txt
```
- Configure environment variables:
Create a .env file in the project's root directory.
Add your API keys and base URLs to the .env file, following the format in the .env.example file.
```bash
SEARXNG_BASE_URL="your_searxng_base_url"
OPENAI_BASE_URL="your_openai_base_url"
OPENAI_API_KEY="your_openai_api_key"
JINA_READER_API_KEY="your_jina_reader_api_key"
```
# Usage
The main functionality is implemented in two test scripts:

`basicTest.py`: This script showcases how to use the LLM client, prompts, and tools to perform a single function call to searchWithSearxng.
`searchTest.py`: This script demonstrates the recursive web search functionality, where the LLM client repeatedly calls the searchWithSearxng function until it finds the best answer.
To run the scripts, simply execute them from the project's root directory:

```Bash

python ./backend/tests/basicTest.py
python ./backend/tests/searchTest.py
```
## Code Overview
- `backend/llm/Client.py`: This module provides a client class for interacting with the OpenAI API.
- `backend/llm/prompts.py`: This module defines the system prompts for the LLM, including instructions for using the search tool.
- `backend/tools/searxngTool.py`: This module implements the searchWithSearxng function, which uses the Searxng and Jina Reader APIs to perform web searches and summarize the results.
- `backend/tools/toolsCenter.py`: This module provides a function for making function calls based on the LLM's output.
- `backend/tools/toolsDef.py`: This module defines the tools available to the LLM, including the searchWithSearxng tool.
- `backend/utils/JinaReader.py`: This module provides a function for reading web pages using the Jina Reader API.
- `backend/utils/llmUtils.py`: This module provides utility functions for generating messages for the LLM.