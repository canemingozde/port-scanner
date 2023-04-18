import threading as t
from queue import Queue
import socket as s
import time


q = Queue()

ip = s.gethostbyname(input("ip giriniz: "))

print()
print(f"Girilen ip: {ip} taranıyor...")
print()

basla = int(input("Başlangıç port değeri: "))
bitis = int(input("Bitiş port değeri: "))
print()

for i in range(4):
    print("Lütfen bekleyin...")
    time.sleep(0.5)

print()
for port in range(basla,bitis+1):
    q.put(port)


def tara(port):
    server = s.socket(s.AF_INET,s.SOCK_STREAM)
    baglanti = server.connect_ex((ip,port))
    if baglanti == 0:
        print("-"*40)
        print(f"Bu port: {port} açıktır.")
        print("-"*40)
    server.close()        


def kuyruk():
    while not q.empty():
        port = q.get()
        tara(port)


def thereadd(isci):
    isciler = []
    for i in range(isci):
        calistir = t.Thread(target=kuyruk)
        isciler.append(calistir)

    for i in isciler:
        i.start()
   

thereadd(20)


