from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=LHPjYtm_LtI"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

# To print title
print("Title :", yt.title)
# To get number of views
print("Views :", yt.views)
# To get the length of video
print("Duration :", yt.length)
# To get description
print("Description :", yt.description)
# To get ratings
print("Ratings :", yt.rating)

youtube_stream= yt.streams.get_highest_resolution()
youtube_stream.download()