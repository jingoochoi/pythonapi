import requests,re
r=requests.get('https://wttr.in/seoul?format=%t+%h+%p')
r1=re.sub(r'[^\w\s:,+°%/.-]', '', r.text)
print(r1.strip())