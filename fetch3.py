import config
import glob
import json
from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
    "access_token": config.a_token ,
    "proxy":config.proxy,
})


entries = ''
for i, p in enumerate(glob.glob('./entries/*.json')):
    o = json.load(open(p))
    if len(o['title'])<1:continue
    #entries += f'{i+1}. "{o["title"]}"\n'
    entries += f'"{o["title"]}",'
msg=config.msg%entries
print(msg)

for data in chatbot.ask(msg):continue
chatbot.delete_conversation(data['conversation_id'])
s=data['message']
print(s)
import os
import json
import time
i=int(time.time()) #os.listdir('./entries')
p=f'./entries/{i}.json'
json.dump({'title':'','content':s},open(p,'w'))

