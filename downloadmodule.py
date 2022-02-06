import pytube,moviepy.editor
def downloadmodule(yt:pytube.YouTube=None,link:str=None):
    try:
        if yt:
            v=yt.streams.get_highest_resolution()
            v.download()
            ti=yt.title
            lstriplist=['~','#','$','%','^','*','\\','|',';',"'",':','"',',','.','/','?']
            for i in range(0,len(lstriplist)):ti=ti.replace(str(lstriplist[int(i)]),'')
            video=moviepy.editor.VideoFileClip(f"{ti}.mp4")
            video.audio.write_audiofile(f"{ti}.mp3")
        elif link:
            yt=pytube.YouTube(link)
            v=yt.streams.get_highest_resolution()
            v.download()
            ti=yt.title
            lstriplist=['~','#','$','%','^','*','\\','|',';',"'",':','"',',','.','/','?']
            for i in range(0,len(lstriplist)):ti=ti.replace(str(lstriplist[int(i)]),'')
            video=moviepy.editor.VideoFileClip(f"{ti}.mp4")
            video.audio.write_audiofile(f"{ti}.mp3")
    except:return False
    return True