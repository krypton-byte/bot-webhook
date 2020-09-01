import requests, json, random
import sys
from bs4 import BeautifulSoup
from io import StringIO
import contextlib
import convertapi
def url2png(url):
	convertapi.api_secret = 'Z7Z4HpVF3n7e9I8H'
	x=convertapi.convert('png', {
	'Url': url
	}, from_format = 'web')
	return x.response['Files'][0]['Url']

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old
def doujin(nuklir,driver,chat_id):
    dujin = json.loads(requests.get('https://terkejoed.herokuapp.com/doujinshi/%s'%(nuklir), timeout=10000).text)
    if dujin['status']:
        open('cache/cover.jpg','wb').write(requests.get('https://terkejoed.herokuapp.com%s'%dujin['cover']).content)
        driver.send_media('cache/cover.jpg',chat_id,'title : %s \n%s\nLink Download : https://terkejoed.herokuapp.com%s'%(dujin['title'], dujin['tags'], dujin['content']))
    else:
        Msg.reply_message('kode Nuklir Salah')
def yt2mp3(urlyt):
    hasilYt=json.loads(requests.get('https://krypton-api.herokuapp.com/', params={'url':urlyt}, timeout=10000).text)
    if hasilYt['status']:
        return hasilYt #'Title : %s\nSize : %s\n Link Download : %s'%(hasilYt['title'], hasilYt['file_size'], 'https://krypton-api.herokuapp.com'+hasilYt['file'])
    else:
        return " Url Yg Anda Berikan Tidak Valid"
def simisimi():
    hasilparser=requests.post('https://wsapi.simsimi.com/190410/talk', headers={'Content-Type':'application/json','x-api-key':'WPLC5qW13w7creemIHAhoQNg~P..lSTJBsaKpMCZ'}, data={'utext':'duar','lang':'id'}).text
    return hasilparser
def bacot(chat):
    pesan=[]
    for i in chat:
        if i.lower() in ['a','u','e','o']:
            if i.isupper():
                pesan.append('I')
            elif i.islower():
                pesan.append('i')
            else:
                pesan.append(i)
        else:
            pesan.append(i)
    return ''.join (pesan)
def waifu():
    f=BeautifulSoup(requests.get('http://randomwaifu.altervista.org/').text,'html.parser')
    return {
        'title':f.p.text,
        'image':'http://randomwaifu.altervista.org/%s'%(f.img['src'])
    }
def bot(chat):
    auth=open('auth.txt').read()
    head=head={"Content-Type":"application/json; charset=utf-8","Authorization":auth}
    data="{\"queryInput\":{\"text\":{\"text\":\"%s\",\"languageCode\":\"id\"}},\"queryParams\":{\"timeZone\":\"Asia/Bangkok\"}}"%(chat)
    o=requests.post('https://dialogflow.clients6.google.com/v2/projects/quickstart-1591326938143/agent/sessions/479584e4-1542-c091-59f5-823889299723:detectIntent',data=data, headers=head).text
    print(o)
    return json.loads(o)