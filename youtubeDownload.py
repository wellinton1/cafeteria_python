from pytube.cli import on_progress
from pytube import YouTube

link = input("Cole seu link do youtube para Download: ")
video = input("Coloque a resolução ex: 144p, 240p ,360p ,480p ,720p...: ")
try:
    yt = YouTube(link, on_progress_callback=on_progress)
    video = yt.get()
except:
    pass
try:
    yt.streams.filter(res=video).first().download()
except:
    print("donwload erro")
else:
    print("Download completo : ")
