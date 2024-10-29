import os
import yt_dlp
from datetime import datetime
import time

url = input("Cole aqui a sua URL: ")

download_dir = os.path.join(os.path.expanduser("~"), "Downloads")

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

today = datetime.today().strftime('%Y-%m-%d')

ydl_opts = {
    'format': 'best',
    'outtmpl': os.path.join(download_dir, f'%(title)s.%(ext)s'),
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    video_title = info_dict.get('title', None)
    video_ext = info_dict.get('ext', None)
    file_path = os.path.join(download_dir, f"{video_title}.{video_ext}")

    ydl.download([url])

try:
    current_time = time.time()
    os.utime(file_path, (current_time, current_time))
except Exception as e:
    print(f"O nome do arquivo contem caracteres desconhecidos nao permitindo a mudança de data")

print(f"Vídeo baixado para: {download_dir}")
