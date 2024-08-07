import httpx
import json

client_id = "[应用API Key]"
client_secret = "[应用Secret Key]"


class WenxinHttpClient:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    async def get_access_token(self):
        """
        使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
        """
        # todo 可以写成缓存方案

        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={self.client_id}&client_secret={self.client_secret}"

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers)
            return response.json().get("access_token")

    async def llm_chat(self):
        # 平时access_token基本不会失效
        # access_token = await self.get_access_token()
        access_token = "access_token"
        url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token={access_token}"

        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": "介绍一下北京"
                }
            ]
        }
        headers = {
            'Content-Type': 'application/json'
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload)

        print(response.text)

    async def llm_chat_stream(self):
        access_token = await self.get_access_token()
        url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token={access_token}"

        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": "给我推荐一些自驾游路线"
                }
            ],
            "stream": True
        }
        headers = {
            'Content-Type': 'application/json'
        }

        async with httpx.AsyncClient() as client:
            async with client.stream("POST", url, headers=headers, json=payload) as response:
                async for line in response.aiter_lines():
                    if line:
                        print(line)
                        yield line
