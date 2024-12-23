#write tools here
searxngTool = {
    "type":"function",
    "function":{
        "name":"searchWithSearxng",
        "description":"Call this function to get the latest online information.",
        "parameters":{
            "type":"object",
            "properties":{
                "q":{
                    "type":"string",
                    "description":"search string"
                },
                "categories":{
                    'type':'string',
                    "enum":["general","images","videos","news","science"]
                }
            },
            "required":['q'],
            "additionalProperties": False
        }
    }
}


exported_tools = [searxngTool]