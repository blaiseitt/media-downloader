from pytube import YouTube

def main():
    link = str(input("Enter Your Link: "))
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution() #get_audio_only()
    stream.download()
    print("Downloaded.")
    #https://youtu.be/Bu8bH2P37kY

if __name__ == "__main__":
    main()
