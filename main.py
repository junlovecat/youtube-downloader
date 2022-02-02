import os,sys,time,json,hashlib,zipfile
os.system('pip uninstall -y pytube')
os.system('pip install pytube')
try:
    import youtubesearchpython,pyfiglet,pytube,moviepy.editor,requests,wget
    from selenium import webdriver
except:
    os.system('pip uninstall -y moviepy youtube-search-python pyfiglet pytube requests wget')
    os.system('pip install moviepy youtube-search-python pyfiglet pytube requests wget')
    import youtubesearchpython,pyfiglet,pytube,moviepy.editor,requests,wget
    from selenium import webdriver
def beautifulresult(results:dict):
    major=results['result'];compressed=[];links=[]
    for x in major:compressed.append(x['accessibility']['title']);links.append(x['link'])
    return compressed,links
def downloader(url):
    def getChromeDriver():
        option=webdriver.ChromeOptions()
        option.add_argument('headless');option.add_argument("window-size=1920x1080");option.add_argument("disable-gpu");option.add_argument("disable-infobars");option.add_argument("--disable-extensions")
        option.add_experimental_option('prefs',{'profile.default_content_setting_values':{'cookies':2,'images':2,'plugins':2,'popups':2,'geolocation':2,'notifications':2,'auto_select_certificate':2,'fullscreen':2,'mouselock':2,'mixed_script':2,'media_stream':2,'media_stream_mic':2,'media_stream_camera': 2, 'protocol_handlers':2,'ppapi_broker':2,'automatic_downloads':2,'midi_sysex':2,'push_messaging':2,'ssl_cert_decisions':2,'metro_switch_to_desktop':2,'protected_media_identifier':2,'app_banner':2,'site_engagement':2,'durable_storage':2}})
        return webdriver.Chrome('./chromedriver.exe',options=option)
    def jsonparser(driver,url):
        driver.get(url)
        isfind=False
        data=''
        while not isfind:
            data=driver.find_element_by_xpath('//*').get_attribute('innerHTML')
            isfind=data.find('ytInitialPlayerResponse')
            data=data[isfind:]
            time.sleep(0.5)
        data=data[data.find('\"url\"'):]
        data=data[:data.find('\"',10)]
        return json.loads('{'+data+'\"}')
    def makefilename():
        md5=hashlib.new('md5')
        md5.update(os.urandom(16))
        return md5.hexdigest()
    def downloadfile(url):
        res=requests.get(url)
        print('downloading webm file')
        filename=makefilename()+'.webm'
        tempvideo=open(filename,'wb')
        tempvideo.write(res.content)
        tempvideo.close()
        return filename
    def converter(old,new):clip=moviepy.editor.VideoFileClip(old);clip.audio.write_audiofile(f'{new}.mp3')
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
def main():
    try:
        raw_link=''
        a=str(input('노래 제목,링크 또는 exit을 입력해주세요: '))
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
        try:
            vid=yt.streams.get_highest_resolution()
            vid.download()
            ti=str(yt.title)
            lstriplist=['~','#','$','%','^','*','\\','|',';',"'",':','"',',','.','/','?']
            for i in range(0,len(lstriplist)):ti=ti.replace(str(lstriplist[int(i)]),'')
            video=moviepy.editor.VideoFileClip(f"{ti}.mp4")
            video.audio.write_audiofile(f"{ti}.mp3")
        except:
            print('Fast download unavailable.\nSlow downloading instead...')
            downloader(raw_link)
    except Exception as e:print(f'error occured - {e}');return
url='https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
response=requests.get(url)
version_number=response.text
download_url=f'https://chromedriver.storage.googleapis.com/{version_number}/chromedriver_win32.zip'
latest_driver_zip=wget.download(download_url,'chromedriver.zip')
with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:zip_ref.extractall()
os.remove(latest_driver_zip)
print(pyfiglet.Figlet(font='slant').renderText('downloader'))
while(1):main()
