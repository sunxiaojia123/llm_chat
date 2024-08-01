from openai import OpenAI

api_key = "在这里设置key或者写到ENV"
client = OpenAI(api_key=api_key)


def llm_chat():
    # 非流式回复
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ]
    )

    print(completion.choices[0].message)


def llm_chat_stream():
    # 流式回复
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ],
        stream=True
    )

    for chunk in completion:
        print(chunk.choices[0].delta)
