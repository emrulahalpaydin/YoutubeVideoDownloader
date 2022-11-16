from pytube import YouTube
import os
from pathlib import Path

path = str(Path.home() / "Downloads")
link = input("Lütfen indirmek istediğiniz youtube url'ini yapıştırın: \n")
try:
    yt = YouTube(link)
except:
    print("Bağlantı hatası oluştu.")
    exit()
try:
    file = yt.streams.get_highest_resolution()
except:
    print("Bir sorun oluştu.")
    exit()
try:
    print("Dosya indiriliyor...")
    file.download(path)
    print("Dosya indirildi.")
    os.startfile(path)
except:
    print("İndirme sırasında bir sorun oluştu.")
    exit()