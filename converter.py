import os
try:import moviepy.editor
except:
    os.system('pip install moviepy')
    import moviepy.editor
def changer(filename):
    audio=moviepy.editor.AudioFileClip(filename)
    audio.write_audiofile(filename)