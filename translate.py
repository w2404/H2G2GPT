import config
import os
import sys
import glob
import requests
import json


def send(messages):
    headers = {"Authorization": "Bearer " + config.key, "Content-Type": "application/json"}
    proxies = {'http': config.proxy, 'https': config.proxy}
    u = 'https://api.openai.com/v1/chat/completions'
    data = {"model": "gpt-3.5-turbo", "messages": messages, "temperature": 0.0}
    r = requests.post(u, json.dumps(data), headers=headers, proxies=proxies)
    o = r.json()
    return o


l1 =[json.load(open('./entries/'+n)) for n in  os.listdir('./entries')]
l2 =[json.load(open('./entries_zh/'+n)) for n in  os.listdir('./entries_zh')]
m1={o['title']:o for o in l1}
m2={o['title']:o for o in l2}

for n in set(m1.keys())-set(m2.keys()):
    o0 =m1[n] # json.load(open('./entries/' + n))
    msg = """翻译以下科幻讽刺小说的段落\n"""
    msg += o0['content']
    print(msg)
    o = send([{'role': 'user', 'content': msg}])
    s = o['choices'][0]['message']['content']
    print(s)
    o0['content'] = s #o['result']
    p = './entries_zh/' + o0['title'].replace(' ','_').replace('/','-').replace('\\','-')+'.json'
    f = open(p, 'w')
    json.dump(o0, f, ensure_ascii=False)
