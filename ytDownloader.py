# import libraries
import yt_dlp

# function to retrieve Urls
def collectUrls():

    # pull in the propper youtube urls from my list
    with open('desiredURLS.txt', 'r') as f:
        contents = f.read()

    urlList = []
    counter = 0
    currentUrl = ""
    for char in contents:
        if (char != "\n"):
            currentUrl += char
        elif (char == "\n"):
            urlList.append(currentUrl)
            counter += 1
            currentUrl = ""

    # print(urlList)

    return urlList

# the operation
def theOperation(urls):

    yt_opts = {
        'verbose': False,
        'download_sections': [{
            'section': {
                'start_time': 2,
                'end_time': 7
            }
        }],
        'extract_audio': True,  # Extract audio
        # 'format': 'mp3',  # Choose best audio quality
        'format': 'bestaudio/best',
        # 'audio-format': 'mp3', #very important to include this line, when changing the format.
        'outtmpl': '%(title)s.%(ext)s', #set the output file name
    }

    ydl = yt_dlp.YoutubeDL(yt_opts)

    for url in urls:
        try:
            ydl.download(url)
        except yt_dlp.DownloadError as e:
            print(f"Error downloading {url}: {e}") #handle download errors

################# MAIN #########################

# urls = collectUrls()

# theOperation(urls)

