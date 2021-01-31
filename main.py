from __future__ import unicode_literals
from selenium import webdriver
from os import path
import sys
from webdriver_manager.chrome import ChromeDriverManager
import youtube_dl

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


while True:
    try:
        fin = ''
        inp = input("\nSong name: ")
        for i in inp.split():
            if i == inp.split()[0]:
                fin += i
            else:
                fin += f"+{i}"

        url = f"https://www.youtube.com/results?search_query={fin}"
            
        driver.get(url)

        source1 = driver.find_element_by_xpath('//*[@id="video-title"]')
        title = source1.get_attribute('title')
        href = source1.get_attribute('href')

        print(f"\n{title}")

        r = input("(y/n): ")

        if r.lower() == 'n':
            print("Please enter the song name with the artist's name for better results.")

        else:
            source_url = f"{href}"

            
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }],
            }

            print("\nDownloading...")
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([source_url])

            print("\nDownloaded succesfully")

    except KeyboardInterrupt:
        driver.quit()
        sys.exit(0)


            

