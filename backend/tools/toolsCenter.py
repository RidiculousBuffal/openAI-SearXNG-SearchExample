import json

from backend.tools.searxngTool import searchWithSearxng
from openai.types.chat.chat_completion_message_tool_call import Function
def make_function_call (function:Function):
    if function.name in globals():
        try:
            function_to_call = globals()[function.name]
            result = function_to_call(**json.loads(function.arguments))
            return result
        except Exception as e:
            print(e)

    else:
        print(f'''Function {function.name} is not found''')