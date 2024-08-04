from openai import OpenAI
from openai import AsyncOpenAI

api_key = "在这里设置key或者写到ENV"


class ChatgptSyncClient:
    def __init__(self):
        self.client = OpenAI(api_key=api_key)

    def llm_chat(self):
        # 非流式回复
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ]
        )

        print(completion.choices[0].message)

    def llm_chat_stream(self):
        # 流式回复
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ],
            stream=True
        )

        for chunk in completion:
            print(chunk.choices[0].delta)


class ChatgptAsyncClient:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=api_key)

    async def llm_chat(self):
        # 非流式回复
        completion = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ]
        )

        print(completion.choices[0].message)

    async def llm_chat_stream(self):
        # 流式回复
        completion = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ],
            stream=True
        )

        async for chunk in completion:
            print(chunk.choices[0].delta)
