from mira_sdk import MiraClient, Flow
import os
from dotenv import load_dotenv

# Load API key from environment variables
def give_response(prompt):
    load_dotenv()
    YOUR_API_KEY = os.getenv("OPENROUTER_API_KEY")
    # Initialize the client
    client = MiraClient(config={"API_KEY": YOUR_API_KEY})

    version = "1.0.0"
    input_data = {
            "prompt": prompt
        }


    # If no version is provided, latest version is used by default
    if version:
        flow_name = f"@sparsh-r/coding-assistant/{version}"
    else:
        flow_name = "@sparsh-r/coding-assistant"

    result = client.flow.execute(flow_name, input_data)
    return result["result"]
def give_tags(prompt):
    from mira_sdk import MiraClient, Flow
    load_dotenv()
    YOUR_API_KEY = os.getenv("OPENROUTER_API_KEY")
    # Initialize the client
    client = MiraClient(config={"API_KEY": YOUR_API_KEY})

    version = "1.0.0"
    input_data = {
            "prompt": prompt
        }

    # If no version is provided, latest version is used by default
    if version:
        flow_name = f"@sparsh-r/tag-generator/{version}"
    else:
        flow_name = "@sparsh-r/tag-generator"

    result = client.flow.execute(flow_name, input_data)
    return result["result"].replace("'","`")
#print(give_response("recommend leetcode questions"))