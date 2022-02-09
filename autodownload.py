import gdown,os
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