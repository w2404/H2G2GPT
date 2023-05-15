import glob
import json
l=[]
for p in glob.glob('./entries/*.json'):
    o=json.load(open(p))
    l.append((o['title'],o['content']))

f_out=open('./README.md','w')
for t,c in sorted(l):
    f_out.write(f'# {t}\n')
    f_out.write(f'{c}\n')
