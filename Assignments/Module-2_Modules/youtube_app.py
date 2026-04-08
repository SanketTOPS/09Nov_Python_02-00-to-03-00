from pytubefix import YouTube

url="https://www.youtube.com/watch?v=T5Ge4viok-o"

YouTube(url).streams.first().download()