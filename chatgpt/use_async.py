from openai import AsyncOpenAI

api_key = "在这里设置key或者写到ENV"
client = AsyncOpenAI(api_key=api_key)


async def llm_chat():
    # 非流式回复
    completion = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ]
    )

    print(completion.choices[0].message)


async def llm_chat_stream():
    # 流式回复
    completion = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ],
        stream=True
    )

    async for chunk in completion:
        print(chunk.choices[0].delta)
