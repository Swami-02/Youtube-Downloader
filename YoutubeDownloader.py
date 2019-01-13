from pytube import YouTube
import os

os.chdir('e:\\PythonPrograms')
f=open('input.txt', 'r')
s=f.read()
f.close()
list=s.split('\n')

#videocount=0

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)    

for vurl in list:
    downloadYouTube(vurl, 'c:\\Users\\Swami\\Downloads')
