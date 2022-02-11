from __future__ import unicode_literals
import os,converter
try:import youtube_dl,pytube
except:
    os.system('pip install youtube_dl pytube moviepy')
    import youtube_dl,pytube
def downloadwithdl(link:str=None):
    try:
        ti=pytube.YouTube(link).title
        lstriplist=['~','#','$','%','^','*','\\','|',';',"'",':','"',',','.','/','?']
        for i in range(0,len(lstriplist)):ti=ti.replace(str(lstriplist[int(i)]),'')
        ydl_opts={'format':'bestaudio/best','postprocessors': [{'key':'FFmpegExtractAudio','preferredcodec':'mp3','preferredquality':'320',}],'outtmpl':ti,}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:ydl.download((link,))
        converter.changer(f'{ti}.mp3')
    except Exception as e:
        if f'{ti}' in os.listdir():
            os.rename(ti,f'{ti}.mp3')
            converter.changer(f'{ti}.mp3')
            print('Download may be incomplete, check out.')
            return False
        return False
    return True