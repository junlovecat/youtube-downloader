import urllib,os,sys
try:import re,pytube,moviepy.editor,pyfiglet,eyed3
except:os.system('pip install pytube moviepy pyfiglet eyed3');import re,pytube,moviepy.editor,pyfiglet,eyed3
def main():
    try:
        a=str(input('노래 제목,링크 또는 exit을 입력해주세요: '))
        if a.lower()=='exit':sys.exit()
        if 'youtu.be' in a or 'youtube.com' in a:yt=pytube.YouTube(a)
        else:
            search_results=re.findall(r"watch\?v=(\S{11})",urllib.request.urlopen('http://www.youtube.com/results?'+urllib.parse.urlencode({'search_query':a})).read().decode())[:5]
            link=[]
            for x in search_results:link.append('https://youtu.be/'+x)
            for x in range(len(link)):print(pytube.YouTube(link[x]).title)
            yt=pytube.YouTube(link[int(input())-1])
        print(f'author: {yt.author}\ntitle: {yt.title}\nrate: {yt.rating}\nviews: {yt.views}')
        input('press enter to download')
        vid=yt.streams.get_highest_resolution()
        vid.download()
        ti=str(yt.title)
        lstriplist=['~','#','$','%','^','*','\\','|',';',"'",':','"',',','.','/','?']
        for i in range(0,len(lstriplist)):ti=ti.replace(str(lstriplist[int(i)]),'')
        video=moviepy.editor.VideoFileClip(os.path.join(f"{ti}.mp4"))
        video.audio.write_audiofile(os.path.join(f"{ti}.mp3"))
        audiofile=eyed3.load(f'{ti}.mp3')
        audiofile.tag.artist=yt.author
        audiofile.tag.album=yt.title
        audiofile.tag.album_artist=yt.author
        audiofile.tag.title=yt.title
        audiofile.tag.save()
    except Exception as e:
        print(f'error occured - {e}')
        return
print(pyfiglet.Figlet(font='slant').renderText('downloader'))
while(1):main()
