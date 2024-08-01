from openai import AsyncOpenAI
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse

app = FastAPI()

api_key = "在这里设置key或者写到ENV"
client = AsyncOpenAI(api_key=api_key)


@app.post("/chatgpt/non-stream")
async def llm_chat():
    # 非流式回复
    completion = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ]
    )
    return completion.choices[0].message


@app.post("/chatgpt/stream")
async def llm_chat_stream():
    # 流式回复
    async def generate():
        completion = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ],
            stream=True
        )

        async for chunk in completion:
            yield await chunk.choices[0]

    return StreamingResponse(generate())


# WebSocket 端点
@app.websocket("/ws/chatgpt")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()

            completion = await client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Hello!"}
                ],
                stream=True
            )
            async for chunk in completion:
                await websocket.send_json(chunk.choices[0])

    except WebSocketDisconnect:
        print("Client disconnected")
