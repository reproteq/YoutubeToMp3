import yt_dlp
import os

def download_youtube_audio(url, output_path='.'):
    # Ruta a la carpeta 'bin' dentro de FFmpeg
    ffmpeg_local_path = r"D:\MUSICA\mp3\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg_local_path,  # Usa FFmpeg desde la carpeta especificada
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Introduce la URL del video de YouTube: ")
    
    script_directory = os.path.dirname(os.path.realpath(__file__))
    output_folder = input(f"Introduce la ruta donde deseas guardar el audio (por defecto: {script_directory}): ") or script_directory

    download_youtube_audio(video_url, output_folder)
