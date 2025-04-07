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