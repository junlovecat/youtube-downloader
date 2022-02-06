import os,time,json
from selenium import webdriver
from selenium.webdriver.remote.command import Command
try:import hashlib,requests,moviepy.editor,pytube
except:
    os.system('pip install hashlib requests moviepy pytube')
    import hashlib,requests,moviepy.editor,pytube
def downloadwithcd(url):
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
        print(url)
        print('this is an error code(3-1)')
        driver.get(url)
        isfind=-1
        data=''
        print('this is an error code(4)')
        while isfind==-1:
            data=driver.find_element_by_xpath('//*').get_attribute('innerHTML')
            isfind=data.find('ytInitialPlayerResponse')
            data=data[isfind:]
            time.sleep(0.5)
        print('this is an error code(5)')
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
        print('this is an error code(8)')
        filename=makefilename()+'.webm'
        print('this is an error code(9)')
        tempvideo=open(filename,'wb')
        tempvideo.write(res.content)
        tempvideo.close()
        print('this is an error code(10)')
        return filename
    def converter(old,new):
        clip=moviepy.editor.VideoFileClip(old)
        clip.audio.write_audiofile(f'{new}.mp3')
        print('this is an error code(12)')
    yt=pytube.YouTube(url)
    ti=yt.title
    print('this is an error code(1)')
    lstriplist=['~','#','$','%','^','*','\\','|',';',"'",':','"',',','.','/','?']
    for i in range(0,len(lstriplist)):ti=ti.replace(str(lstriplist[int(i)]),'')
    mp4filename=ti
    print('this is an error code(2)')
    driver=getChromeDriver()
    print('this is an error code(3)')
    data=jsonparser(driver,url)
    print('this is an error code(6)')
    driver.close()
    data_url=data['url'].replace('mime=video/mp4','mime=audio/webm')
    print('this is an error code(7)')
    webmfilename=downloadfile(data_url)
    print('this is an error code(11)')
    converter(webmfilename,mp4filename)