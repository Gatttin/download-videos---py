from pytube import Youtube

link = input("Digite a URL de seu video: ")
url = Youtube(link)

stream = url.streams.get_highest_resolution()
stream.download()