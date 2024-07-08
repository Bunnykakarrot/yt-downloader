#YouTube downloader for single video
from pytube import YouTube
#saving path
Save_path = "C:\\Users\\KOUSHIK\\Downloads"
#video link to download
link = "https://youtube.com/shorts/zf27nH8WOKM?si=ZC-xQdWeCJ2Q5iuh"
#gaurding the statements
try :
    yt = YouTube(link)# object instantiation
except:
    print("check your internet connection ")# to handle exception
#streams and filter for the mp4 files
mp4_streams =yt.streams.filter(file_extension="mp4").all()
#downloading video with higest resoultion
down_video = mp4_streams[-1]
try:
    down_video.download(output_path =Save_path)
    print("downloaded successfully")
except:
    print("error occured try again")
