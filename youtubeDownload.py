from pytube import YouTube

link = input("Cole seu link do youtube para Download: ")
video = input("Coloque a resolução ex: 144p,240p,360p,720p...: ")
try:
    yt = YouTube(link)
    video = yt.get()
except:
    pass
try:
    yt.streams.filter(res=video).first().download()
except:
    print("erro Download")
print("Download completo")