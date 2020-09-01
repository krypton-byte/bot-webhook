list_menu={
    'member':'''
↦↦↦↦↦❝Menu❞↦↦↦↦↦
↦#delete
↦#???
↦#cari
↦#qrreader
↦#?
↦#url2png
↦#tiktok {NO WM}
↦#wiki
↦#qrmaker
↦#intro
↦#help
↦#gambar
↦#joke
↦#kitsune
↦#neko
↦#dog
↦#adminlist
↦#bct #nyinyinyi
↦#kpt <syntak> # jangan di gunakan untuk pemerosessan yg keras
↦#doujin <nuklir> #dosa tanggung sendiri
↦#yt2mp3 <link youtube>
↦#owner
↦# [chatBot]
↦#quote
↦#film
↦#nime 
↦#ts {TRANSLATE}
↦#quotemaker
↦#linkgroup
↦#stiker
↦#donasi
↦↦↦↦↦↦↦↦↦↦↦↦''',
    'admin':'''
       ❝Menu❞
↦#admin
↦#unadmin
↦#kick
↦#revoke
↦#add +62xxxx
'''
}
def menu(args):
    try:
        return list_menu[args]
    except:
        return list_menu['member']