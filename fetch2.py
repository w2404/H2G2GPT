
import config
import sys
import glob
import requests
import json


def send(messages):
    print(messages)
    headers = {"Authorization": "Bearer " + config.key, "Content-Type": "application/json"}
    proxies = {'http': config.proxy, 'https': config.proxy}
    u = 'https://api.openai.com/v1/chat/completions'
    m="text-davinci-003"
    u = 'https://api.openai.com/v1/completions'
    data = {"model": m, "prompt": config.msg, "temperature": 0.0,"max_tokens":4000}
    r = requests.post(u, json.dumps(data), headers=headers, proxies=proxies)
    o = r.json()
    return o


msg = config.msg

entries = ''
for i, p in enumerate(glob.glob('./entries/*.json')):
    o = json.load(open(p))
    entries += f'{i+1}. "{o["title"]}"\n'
#msg = msg % entries

#o = send(config.pre) # + [{'role': 'user', 'content': msg}])
o = send( [{'role': 'user', 'content': msg}])
print(o)
s = o['choices'][0]['message']['content']
print(s)
o = {}
if False:
    o['title'], o['content'] = s.split(':', maxsplit=1)
else:
    o['title'], o['content'] ='1',s # s.split(':', maxsplit=1)

n = o['title'].replace('/', '-').replace(' ', '_')
p = f'./entries/{n}.json'
f = open(p, 'w')
json.dump(o, f)
