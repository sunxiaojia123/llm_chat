import os
import qianfan

# 通过环境变量初始化认证信息
# 【推荐】使用安全认证AK/SK鉴权
# 替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
os.environ["QIANFAN_ACCESS_KEY"] = "your_iam_ak"
os.environ["QIANFAN_SECRET_KEY"] = "your_iam_sk"


class WenxinAsyncClient:
    def __init__(self):
        self.client = qianfan.ChatCompletion()

    async def llm_chat(self):
        resp = await self.client.ado(model="ERNIE-4.0-8K",
                                     system="你是我的小助手",
                                     messages=[
                                         {
                                             "role": "user",
                                             "content": "北京有哪些美食"
                                         },
                                     ])
        print(resp["body"])

    async def llm_chat_stream(self):
        resp = await self.client.ado(model="ERNIE-4.0-8K",
                                     system="你是我的小助手",
                                     messages=[{
                                         "role": "user",
                                         "content": "简单介绍下故宫"
                                     }],
                                     stream=True)

        async for r in resp:
            print(r["body"])
