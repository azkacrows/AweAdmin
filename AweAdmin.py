#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import httplib
import os
import time
import sys
import getopt
import signal
import socket

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'


def t():
    current_time = time.localtime()
    ctime = time.strftime('%H:%M:%S', current_time)
    return "["+ ctime + "]"
def shutdown():
	print ""
	print bcolors.BGRED + bcolors.WHITE + t() + "[info] Mematikan AweAdmin" + bcolors.ENDC +"\n\n"
	sys.exit()
def usage():
    print bcolors.RED + bcolors.BOLD
    print """
	    ___                ___       __          _     	
	   /   |_      _____  /   | ____/ /___ ___  (_)___ 	
	  / /| | | /| / / _ \/ /| |/ __  / __ `__ \/ / __ \	
	 / ___ | |/ |/ /  __/ ___ / /_/ / / / / / / / / / /	
	/_/  |_|__/|__/\___/_/  |_\__,_/_/ /_/ /_/_/_/ /_/ 	
                                                   
    """
    print bcolors.ENDC
    print """
        Perintah:
         -t  --target   - Target web server "contoh.com"
         -v  --verbose  - Mengaktifkan mode verbose
         -h  --help     - Memunculkan pertolongan

        CONTOH:
          python AweAdmin.py -t targetsite.com -v
    """
    sys.exit()

def check(host, path):
        try:
            conn = httplib.HTTPConnection(host)
            conn.request("HEAD", path)
            return conn.getresponse().status
        except StandardError:
            return "unknown"


def final_result():
    print t() + "[info] scan selesai"
    if len(result_array)==0:
        print bcolors.RED + bcolors.BOLD + t() + "[critical] Maaf! AweAdmin tidak dapat menemukan direktori yang memungkinkan" + bcolors.ENDC
    else:
        print bcolors.GREEN + bcolors.BOLD
        print t() + "[info] Ketemu " + str(len(result_array)) + " Kemungkinan direktorinya"
        for count in result_array:
            print count
        print bcolors.ENDC
    shutdown()

def sigint_handler(signum, frame):
    print '\n Interupsi pengguna ! Mematikan'
    shutdown()

signal.signal(signal.SIGINT, sigint_handler)

v=0
f=0

opts, args = getopt.getopt(sys.argv[1:], 't:hv', ['target=','help''verbose'])


for opt, arg in opts:
    if opt in ('-h','--help'):
        usage()
    elif opt in ('-t', '--target'):
        host = arg
    elif opt in ('-v', '--verbose'):
        v=1
    else:
        usage()
if 'host' not in locals():
    usage()

print bcolors.RED + bcolors.BOLD
print """
	    ___                ___       __          _     	
	   /   |_      _____  /   | ____/ /___ ___  (_)___ 	
	  / /| | | /| / / _ \/ /| |/ __  / __ `__ \/ / __ \	
	 / ___ | |/ |/ /  __/ ___ / /_/ / / / / / / / / / /	
	/_/  |_|__/|__/\___/_/  |_\__,_/_/ /_/ /_/_/_/ /_/ 	
                                                   
"""
print bcolors.ENDC

print t() + "[info] Memeriksa koneksi ke server target"


ccode = check(host,"/")

if (ccode < 400):
	print bcolors.BOLD + t() + "[info] Server target sudah aktif dan berjalan" + bcolors.ENDC
else:
	print bcolors.RED + bcolors.BOLD + t() + "[warning] Server target terlihat akan down. check koneksi internet atau settingan proxy mu. lihat option yang salah ketik jika ada " + bcolors.ENDC
	shutdown()

print t() + "[info] Mulai scan daftar direktori scanner"

f = open( "dir", "r" )
directory = []
for line in f:
    directory.append(line)

print t() + "[info] menjalankan direktori scanning ke server target."
maxlen=len(directory)
if (v==0):
    print t() + "[info] "+ str(maxlen) + " Direktori dimuat, Ini mungkin butuh beberapa saat, harap tunggu.. pakai option -v untuk mode verbose"
else:
    print t() + "[info] "+ str(maxlen) + " Direktori dimuat, Ini mungkin butuh beberapa saat, harap tunggu.."
i=0
result_array = []
for i in range (maxlen):
    c_dir=directory[i].rstrip('\n')
    rcode=check(host,c_dir)
    code=str(rcode)

    if (v==True and rcode >= 400):
        print t() + "[response]" + bcolors.YELLOW + "["+code+"]" + bcolors.ENDC +" =>  "+ host + c_dir

    if (rcode <400 ):
        print bcolors.GREEN + bcolors.BOLD + t() + "[response]" + "["+code+"]" +" =>  "+ host + c_dir + bcolors.ENDC
        num=0
        result="[response]" + "["+code+"]" +" =>  "+ host + c_dir
        result_array.insert(num,result)
        num = num+1
        reply = str(raw_input(bcolors.BOLD +' Apakah Anda ingin melanjutkan scanning untuk hasil yang lebih pasti? (y/n): ')).lower().strip()
        print bcolors.ENDC
        if (reply == 'n'):
            final_result()
final_result()
