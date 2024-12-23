import json

from backend.llm.Client import LLM
from backend.llm.prompts import SearXng_System_Prompts
from backend.tools.toolsDef import searxngTool
from backend.utils.llmUtils import generateMessage
from backend.tools.toolsCenter import make_function_call
# create a client
llm = LLM()
def transform_tool_calls(tool_calls):
    transformed = []
    for call in tool_calls:
        transformed.append({
            "id": call.id,
            "type": call.type,
            "function": {
                "arguments": call.function.arguments,
                "name": call.function.name,
            }
        })
    return transformed
def recursive_llm_web_search(Message):
    completion = llm.getCompletion(systemPrompt=SearXng_System_Prompts(), messages=Message, tools=[searxngTool],
                                   stream=False)
    if completion.choices[0].message.tool_calls:
        Message.append({
            'role': "assistant",
            'tool_calls':transform_tool_calls(completion.choices[0].message.tool_calls)
        })
        for call in completion.choices[0].message.tool_calls:
            func = call.function
            result = make_function_call(func)
            Message.append({'role': 'tool', 'content':json.dumps(result), 'tool_call_id':call.id})
        recursive_llm_web_search(Message)
    else:
        print(completion.choices[0].message.content)
# get completion
# mock userMessage
userMessage = generateMessage('user','''Sanofi's financial status in the second half of 2024.''')
recursive_llm_web_search([userMessage])





