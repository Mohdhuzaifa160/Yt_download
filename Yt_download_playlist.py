import yt_dlp

playlist_url = "paste your playlist link"

ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s', 
    'noplaylist': False,  
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
