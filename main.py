import os,sys,downloadmodule,downloadwithcd,searcher,autodownload,downloadwithdl
os.system('pip install --upgrade pytube')
try:
    import youtubesearchpython,pytube
except:
    os.system('pip install youtube-search-python pytube')
    os.system('pip install --upgrade youtube-search-python pytube')
    import youtubesearchpython,pytube

def main():
    try:
        raw_link=''
        try:a=str(input('노래 제목,링크 또는 exit을 입력해주세요: '))
        except KeyboardInterrupt:exit()
        if a.lower()=='exit':sys.exit()
        if 'youtu.be' in a or 'youtube.com' in a:yt=pytube.YouTube(a);raw_link=a
        else:
            results=youtubesearchpython.VideosSearch(a,limit=5).result()
            result,links=searcher.beautifulresult(results)
            for x in range(len(result)):print(f'{x+1}: {result[x]}')
            yt=pytube.YouTube(links[int(input('다운로드 할 영상 번호를 입력해주세요.--> '))-1])
            raw_link=yt.watch_url
        print(f'author: {yt.author}\ntitle: {yt.title}\nrate: {yt.rating}\nviews: {yt.views}')
        os.system('pause')
        if downloadmodule.downloadmodule(yt,raw_link):return
        elif downloadwithcd.downloadwithcd(raw_link):return
        elif downloadwithdl.downloadwithdl(raw_link):return
        else:print('Cannot be downloaded -> no remaining options left.')
    except Exception as e:print(f'Cannot be downloaded -> {e}');return
autodownload.downloader()
print('''
  ____/ /___ _      ______  / /___  ____ _____/ /__  _____
 / __  / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/
/ /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /
\__,_/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/''')
while(1):main()