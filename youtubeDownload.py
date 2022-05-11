from pytube import YouTube

link =input("cole seu link do youtube para Download: ")
try:
    yt = YouTube(link)
except:
    print("erro de conexao")


try:
    yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution().download()
    #yt.streams.filter(progressive=True, file_extension="mp4").first().download() biblioteca pytube
except:
    print("erro Download")
print("donload completo")