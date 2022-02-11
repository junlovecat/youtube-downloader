import os,time,json
from selenium import webdriver
try:import hashlib,requests,moviepy.editor,pytube,wget,zipfile
except:
    os.system('pip install hashlib requests moviepy pytube wget zipfile')
    import hashlib,requests,moviepy.editor,pytube,wget,zipfile
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
        def converter(old,new):moviepy.editor.VideoFileClip(old).audio.write_audiofile(f'{new}.mp3')
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
        os.system(f'del /f {webmfilename}')
    except:return False
    return True
downloadwithcd('https://www.youtube.com/watch?v=TxhiMXVe3fc')