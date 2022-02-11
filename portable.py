import os,sys,time,json
os.system('pip install --upgrade pytube')
try:
    import youtubesearchpython,pytube,moviepy.editor,requests,wget,zipfile,hashlib,youtube_dl,gdown
    from selenium import webdriver
except:
    os.system('pip install youtube-search-python pytube moviepy requests wget zipfile hashlib selenium youtube_dl gdown')
    os.system('pip install --upgrade youtube-search-python pytube moviepy requests wget zipfile hashlib selenium youtube_dl gdown')
    import youtubesearchpython,pytube,moviepy.editor,requests,wget,zipfile,hashlib,youtube_dl,gdown
    from selenium import webdriver
def beautifulresult(results:dict):
    major=results['result'];compressed=[];links=[]
    for x in major:compressed.append(x['accessibility']['title']);links.append(x['link'])
    return compressed,links
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
def downloadwithcd(url):
    try:
        def autodownload():
            url='https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
            response=requests.get(url)
            version_number=response.text
            download_url=f'https://chromedriver.storage.googleapis.com/{version_number}/chromedriver_win32.zip'
            latest_driver_zip=wget.download(download_url,'chromedriver.zip')
            with zipfile.ZipFile(latest_driver_zip,'r') as zip_ref:zip_ref.extractall()
            os.remove(latest_driver_zip)
        def getChromeDriver():
            option=webdriver.ChromeOptions()
            option.add_argument('headless')
            option.add_argument("window-size=1920x1080")
            option.add_argument("disable-gpu")
            option.add_argument("disable-infobars")
            option.add_argument("--disable-extensions")
            prefs={'profile.default_content_setting_values':{'cookies':2,'images':2,'plugins':2,'popups':2,'geolocation':2,'notifications':2,'auto_select_certificate':2,'fullscreen':2,'mouselock':2,'mixed_script':2,'media_stream':2,'media_stream_mic':2,'media_stream_camera':2,'protocol_handlers':2,'ppapi_broker':2,'automatic_downloads':2,'midi_sysex':2,'push_messaging':2,'ssl_cert_decisions':2,'metro_switch_to_desktop':2,'protected_media_identifier':2,'app_banner':2,'site_engagement':2,'durable_storage':2}}
            option.add_experimental_option('prefs',prefs)
            return webdriver.Chrome('./chromedriver.exe',options=option)
        def jsonparser(driver:webdriver.Chrome,url:str):
            driver.get(url)
            isfind=-1
            data=''
            while isfind==-1:
                data=driver.find_element_by_xpath('//*').get_attribute('innerHTML')
                isfind=data.find('ytInitialPlayerResponse')
                data=data[isfind:]
                time.sleep(0.5)
            f=open('eee.txt','w',encoding='utf-8')
            f.write(data)
            f.close()
            data=data[data.find('\"url\"'):]
            data=data[:data.find('\"',10)]
            return json.loads('{'+data+'\"}')
        def makefilename():
            md5=hashlib.new('md5')
            md5.update(os.urandom(16))
            return md5.hexdigest()
        def downloadfile(url):
            res=requests.get(url)
            filename=makefilename()+'.webm'
            tempvideo=open(filename,'wb')
            tempvideo.write(res.content)
            tempvideo.close()
            return filename
        def converter(old,new):
            clip=moviepy.editor.VideoFileClip(old)
            clip.audio.write_audiofile(f'{new}.mp3')
        autodownload()
        yt=pytube.YouTube(url)
        ti=yt.title
        lstriplist=['~','#','$','%','^','*','\\','|',';',"'",':','"',',','.','/','?']
        for i in range(0,len(lstriplist)):ti=ti.replace(str(lstriplist[int(i)]),'')
        mp4filename=ti
        driver=getChromeDriver()
        data=jsonparser(driver,url)
        driver.close()
        data_url=data['url'].replace('mime=video/mp4','mime=audio/webm')
        webmfilename=downloadfile(data_url)
        converter(webmfilename,mp4filename)
    except:return False
def downloadwithdl(link:str=None):
    try:
        ti=pytube.YouTube(link).title
        lstriplist=['~','#','$','%','^','*','\\','|',';',"'",':','"',',','.','/','?']
        for i in range(0,len(lstriplist)):ti=ti.replace(str(lstriplist[int(i)]),'')
        ydl_opts={'format':'bestaudio/best','postprocessors': [{'key':'FFmpegExtractAudio','preferredcodec':'mp3','preferredquality':'320',}],'outtmpl':ti,}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:ydl.download((link,))
    except Exception as e:
        if f'{ti}' in os.listdir():
            os.rename(ti,f'{ti}.mp3')
            print('Download may be incomplete, check out.')
            return False
        return False
    return True
def downloader():
    dirlist=os.listdir()
    if 'ffmpeg.exe' not in dirlist:gdown.download('https://drive.google.com/uc?id=1JclQh6vM4MNOyJACCWTB7MlGxTmfpybX','ffmpeg.exe',quiet=True)
    if 'ffplay.exe' not in dirlist:gdown.download('https://drive.google.com/uc?id=1PSvusXF6c2Mo7hjpoit9XgdL9vh1vYh-','ffplay.exe',quiet=True)
    if 'ffprobe.exe' not in dirlist:gdown.download('https://drive.google.com/uc?id=1T1AvUmYLxPzvIwvy6HdJxLBuxgTc-iXQ','ffprobe.exe',quiet=True)
    killer()
    return
def killer():
    for x in os.listdir():
        if str(x).startswith('ffmpeg') and str(x).endswith('tmp'):
            os.system(f'del /q {x}')
        elif str(x).startswith('ffplay') and str(x).endswith('tmp'):
            os.system(f'del /q {x}')
        elif str(x).startswith('ffprobe') and str(x).endswith('tmp'):
            os.system(f'del /q {x}')
    return
def main():
    try:
        raw_link=''
        try:a=str(input('노래 제목,링크 또는 exit을 입력해주세요: '))
        except KeyboardInterrupt:exit()
        if a.lower()=='exit':sys.exit()
        if 'youtu.be' in a or 'youtube.com' in a:yt=pytube.YouTube(a);raw_link=a
        else:
            results=youtubesearchpython.VideosSearch(a,limit=5).result()
            result,links=beautifulresult(results)
            for x in range(len(result)):print(f'{x+1}: {result[x]}')
            yt=pytube.YouTube(links[int(input('다운로드 할 영상 번호를 입력해주세요.--> '))-1])
            raw_link=yt.watch_url
        print(f'author: {yt.author}\ntitle: {yt.title}\nrate: {yt.rating}\nviews: {yt.views}')
        os.system('pause')
        if downloadmodule(yt,raw_link):return
        elif downloadwithcd(raw_link):return
        elif downloadwithdl(raw_link):return
        else:print('Cannot be downloaded -> no remaining options left.')
    except Exception as e:print(f'Cannot be downloaded -> {e}');return
downloader()
print('''
  ____/ /___ _      ______  / /___  ____ _____/ /__  _____
 / __  / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/
/ /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /
\__,_/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/''')
while(1):main()