# A2MP3
**A2MP3** is a command line tool to download any song with just *keywords* or *song title*.

## Install
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ***youtube-dl*** and ***selenium***.

    pip install youtube-dl
    pip install selenium

You will need to install ffmpeg, for linux based machines, you will just need to use your console.  
Example Ubuntu:

    sudo apt update
    sudo apt install ffmpeg
    
On windows ones instead, you will need to download the [last build](https://ffmpeg.org/download.html#build-windows)  
At this point copy the 3 files you can find on bin folder, and paste them in the main Python's scripts folder.

![enter image description here](https://camo.githubusercontent.com/8029dedf1ed27d2a12e30879e662ceca4d91b4d1898322ec08da2a09a220641a/68747470733a2f2f692e6962622e636f2f676d4a5a317a432f6161616161612e706e67)

Then you will need to install Google Chrome, for linux based machines, you will just need to use your console.  
Example ***Ubuntu***:
  * Download the latest Google Chrome `.deb` package with [wget](https://linuxize.com/post/wget-command-examples/):
  
    `wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`
* Install the Google Chrome `.deb` package by typing: 
 
    `sudo apt install ./google-chrome-stable_current_amd64.deb`
    
On ***Windows***:
* [Download the installation file.](https://www.google.com/chrome/browser/desktop/index.html)
* If prompted, click **Run** or **Save**.
* If you chose **Save**, double-click the download to start installing.
    
## Info
* selenium will be used to find the most relevant song for the appropiate keyword or title.
* youtube-dl will be used to download the audio from youtube.  
* ffmpeg will convert them to mp3.

## Usage
* Run **main.py**.

![Screenshot 1](https://i.ibb.co/pXcBZQJ/Screenshot-from-2021-01-31-16-01-53.png)

* Insert ***song title*** or ***keyword***. 
* We'll download '*1x1*' by '*Bring Me The Horizon ft. Nova Twins*' for this tutorial.

![Screenshot 2](https://i.ibb.co/nbHd197/Screenshot-from-2021-01-31-16-02-16.png)

* Enter '***y***' if its the song you wanted. If not, enter '***n***' and insert a more relevant *title* or *keyword*.
* The song will be downloaded in the current directory where the *main.py* file is running.

![enter image description here](https://i.ibb.co/M7Y0vYQ/Screenshot-from-2021-01-31-16-02-54.png)
## For frequent usage (*linux*)
You can create a custum command for linux terminal in order to use frequently.
* Open ***.bashrc*** file with nano

    `user@ubuntu:~$ nano ~/.bashrc`

* Find `# some mode ls aliases` and add

    `alias A2MP3 = "python3 path/to/the/main.py"`
    
    ![enter image description here](https://i.ibb.co/tz1vf3Z/Screenshot-from-2021-01-31-17-09-50.png)

* Press **Ctrl + O** to write out and press **RETURN**. Then exit the editor by pressing **Ctrl + X**
* Restart the terminal

Now you can use the command ***A2MP3*** in your terminal to run the *main.py* file.

![enter image description here](https://i.ibb.co/26xFWBT/Screenshot-from-2021-01-31-17-13-38.png)

Use **Ctrl+C** to make *main.py* exit with an error code 0.

## Liscence
***A2MP3*** is liscenced under the terms of [GNU General Public License](https://www.gnu.org/licenses/licenses.en.html#GPL)

*FAQs contact me* - ***gamerscrew2017.4bullets@gmail.com***
