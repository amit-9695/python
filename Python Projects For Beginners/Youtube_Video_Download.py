# First install pytube

from pytube import YouTube

# Specify the URL of the YouTube video
Url = input("Enter Your Youtube Video URL :- ")

#Create a YouTube object
video=YouTube(Url)

# Select the highest resolution stream
stream = video.streams.get_highest_resolution()

# Define the output path for the downloaded video
path = "E:\Download"

# Download the video
stream.download(path)
