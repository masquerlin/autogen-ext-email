`autogen-ext-email` is a Python package that provides an agent capable of generating images, attaching files, drafting reports, and sendind emails to multiple recipients or specific users based on their queries. This feature is highly beneficial for customer management and email marketing, enhancing automation and improving efficiency.

## Installation

[](https://github.com/masquerlin/autogen-ext-email/blob/main/README.md#installation)

To install the package from the GitHub repository, use the following command:

```shell
pip install autogen-ext-email
```

## Example

```
from autogen_ext_email import EmailAgent,EmailConfig
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import TextMentionTermination
import asyncio
model_client = OpenAIChatCompletionClient(
        api_key=api_key,
        parallel_tool_calls=False,
    )
# img_base_url and img_api_key is from https://www.aliyun.com/product/bailian, or you can change your image generating method by yourself.
e_agent = EmailAgent(name='email_agent', 
                     model_client=model_client,
                     email_config=EmailConfig(
                         email='masquerlin@gmail.com', 
                         password='xxxxxxxxxxxx', server='smtp.gmail.com', 
                         port=587),
                     img_base_url=img_base_url,
                     img_api_key=img_api_key)

async def main():
    text_termination = TextMentionTermination("TERMINATE")
    team = RoundRobinGroupChat([e_agent], termination_condition=text_termination)
    async for message in team.run_stream(task="generate an report about autogen and send it to 'masquerlin@gmail.com'"): 
        if isinstance(message, TaskResult):
            print("Stop Reason:", message.stop_reason)
        elif 'PASS_TOUSER' in message.content:
            print(message)
asyncio.run(main())
```

## Usage

[](https://github.com/masquerlin/autogen-ext-email/blob/main/README.md#usage)

See example.py for a simple example of how to use this agent. Note, this example requires the OpenAI client, so please install the relevant extension.

## License

[](https://github.com/masquerlin/autogen-ext-email/blob/main/README.md#license)

This project is licensed under the MIT License.
