from pustaka.brainly import *
from flask import *
from pustaka.dewabatch import cari as dewabatch
from pustaka.sdmovie import fun
from pustaka.api import *
from pustaka.brainly import *
from urllib.parse import quote, unquote
import json, requests
from googletrans import Translator
import os, random, wikipedia
wikipedia.set_lang('id')
tra=Translator()
app = Flask(__name__)
menu='''
↦↦↦↦↦❝Menu❞↦↦↦↦↦
↦#cari
↦#? [bug]
↦#wiki
↦#intro
↦#help
↦#joke
↦#bct #nyinyinyi
↦#kpt <syntak> # jangan di gunakan untuk pemerosessan yg keras
↦#doujin <nuklir> #dosa tanggung sendiri
↦#yt2mp3 <link youtube>
↦#owner
↦#quote
↦#nime
↦#film
↦#ts {TRANSLATE}
↦↦↦↦↦↦↦↦↦↦↦↦'''
@app.route('/',methods=['GET','POST'])
def index():
    poStman=json.loads(request.data.decode())
    chat=poStman['query']['message']
    sender=poStman['query']['sender']
    message=[]
    hasil=reply(chat, sender)
    if hasil:
        for i in hasil:
            print(i)
            message.append({'message':i})
        return {
            'replies':message
        }
    else:
        return 'tested'

def reply(chat, sender):
    outPut=[]
    command=chat.lower().split()[0]
    print('co : '+command)
    args=chat.split()[1:]
    if command in ['#help','#menu']:
        return [menu]
    elif command == '#bct':
        outPut.append(bct(chat[5:]))
        return outPut
    elif command == '#doujin':
        if args:
            outPut.append(doujin(args[0], driver, chat_id))
        else:
            outPut.append('Masukan Kode Nuklir')
        return outPut
    elif command == '#quote':
        try:
            if args:
                hasil=json.loads(requests.get('https://api.quotable.io/random',params={'tags':args[0]}).text)
            else:
                hasil=json.loads(requests.get('https://api.quotable.io/random').text)
            tags=''
            for i in hasil['tags']:
                tags+=' ↦%s\n'%(i)
                pesan='''author : %s
Tags :
%s[EN] : %s
[ID] : %s'''%(hasil['author'], tags, hasil['content'],tra.translate(text=hasil['content'], dest='id').text)
            outPut.append(pesan)
        except:
            outPut.append('Tags Tidak Ada')
        return outPut
    elif command == '#yt2mp3':
        if args:
            hasilYt=yt2mp3(args[0])
            outPut.append('Title : %s\nSize : %s\nLink Download : https://krypton-api.herokuapp.com%s'%(hasilYt['title'], hasilYt['file_size'],hasilYt['file']))
        else:
            outPut.append('Masukan Parameternya Bro')
        return outPut
    elif command == '#?':
        if args:
            answers=''
            isi='''Soal    : %s
Mapel   : %s
Sekolah : %s
Tanggal : %s
'''
            if args[-1].isnumeric():
                jum=int(args[-1])
                soal=chat[3:-len(args[-1])]
            else:
                jum=1
                soal=chat[3:]
            print(jum)
            print(soal)
            cari=gsearch('"%s" site:brainly.co.id'%soal)
            print(cari)
            temp=[]
            for i in cari:
                if 'google.com' not in i and 'tugas' in i:
                    temp.append(i)
            print(temp)
            if temp:
                for i in temp[:jum]:
                    try:
                        print(i)
                        br=brainly(i)
                        print(br)
                        pesan=isi%(br['soal'][1:-1], br['mapel'][1:-1], br['angkatan'][1:-1], br['tanggal'])
                        for jb in br['jawaban']:
                            answers+='---------------------------%s'%(jb)
                        pesan+=answers
                        outPut.append(pesan)
                    except Exception as e:
                        print(e)
                        outPut.append('Gagal Mengambil Jawaban')
            else:
                outPut.append('Mencari Jawaban ? *%s* Tidak Ada'%(soal))
        else:
            outPut.append('Masukan Soal Nya Bro')
        return outPut
    elif command == '#cari':
        print('cmd : cari')
        try:
            hasil = wikipedia.search(chat[6:])
            pesan='hasil pencarian : \n'
            print(hasil)
            for i in hasil:
                pesan+='↦ %s\n'%(i)
            outPut.append(pesan)
        except Exception as e:
            print(e)
            outPut.append('Masukan Parameternya Bro')
        return outPut
    elif command == '#wiki':
        try:
            hasil=wikipedia.page(chat[6:])
            outPut.append('title :%s\nsource: %s\n%s'%(hasil.title, hasil.url, hasil.content))
        except:
            outPut.append('Yg Anda Cari Tidak Ada')
        return outPut
    elif command == '#cc':
        cc=json.loads(open('ISO-639-1-language.json').read())
        pesan=''
        for i in cc:
            pesan+='%s : %s\n'%(i['code'], i['name'])
        outPut.append(pesan)
        return outPut
    elif command == '#ts':
        try:
            con=tra.translate(text=chat[7:], dest=chat[4:6]).text
            outPut.append(con)
        except:
            outPut.append('#ts [Target] [Text]\nContoh :\n #ts id good morning \nketik #cc untuk melihat kode negara')
        return outPut
    elif command == '#kpt':
        outPut.append('Hasil Eksekusi :\n%s'%(requests.get('https://twilio-apis.herokuapp.com/',params={'cmd':chat[5:]}).text))
        return outPut
    elif command == '#nime':
        hasil=gsearch('"%s" site:dewabatch.com'%chat[5:])
        result=[]
        for i in hasil:
            if ('dewabatch' in i and 'google' not in i):
                try:
                    if args[0].lower() in i.lower():
                        print(i)
                        x=dewabatch(i)
                        outPut.append('%s\n%s'%(x['a'],x['result']))
                except:
                    outPut.append('Anime "%s" Tidak Ditemukan'%(chat[5:]))
        return outPut
    elif command == '#film':
        hasil=gsearch('"%s" site:sdmovie.fun'%chat[5:])
        print(hasil)
        for i in hasil:
            if ('sdmovie' in i and 'google' not in i):
                print(i)
                Link=''
                hafun=fun(i)
                print(hafun)
                for o in hafun['video']:
                    print(o)
                    Link+=f"{o['url']} | {o['lewat']} | {o['sub']} | {o['res']} \n "
                    print(Link)
                pesan='judul : %s\nrating: %s\nsinopsis : %s\n VIDEO :\n %s'%(hafun['title'],hafun['rating'],hafun['sinopsis'],Link)
                print(pesan)
                outPut.append(hasfun['title']+'\n'+pesan)
        return outPut
    elif command == '#donasi':
        return ['https://saweria.co/donate/KryptonByte\nYuk Donasi Biar Bot Nya Aktif Terus Dan Mimin Nya Rajin Update & Fix Bug']
    else:
        for i in ['assalamu\'alaikum','asalamu\'alaikum','assalamualaikum','asalamualaikum']:
            if i in chat.lower():
                outPut.append('وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ')
        for i in ['nyimak','minyak']:
            if i in chat.lower():
                outPut.append('Nyimak aja Terooos sampe Kiamat :v')
        outPut.append('wkwkwk')
        return outPut
app.run()
