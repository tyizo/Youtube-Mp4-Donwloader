from colored import fg
from pytube import YouTube


green = fg(46) # Colors
red = fg(160)
art = (red+""" 
=====================================================================================================
    __   __ _____     ______                        _                    _
    \ \ / /|_   _|    |  _  \                      | |                  | |
     \ V /   | |      | | | | ___ __      __ _ __  | |  ___    __ _   __| |  ___  _ __
      \ /    | |      | | | |/ _ \\ \ /\ / /| '_ \ | | / _ \  / _` | / _` | / _ \| '__|
      | |    | |      | |/ /| (_) |\ V  V / | | | || || (_) || (_| || (_| ||  __/| |
      \_/    \_/      |___/  \___/  \_/\_/  |_| |_||_| \___/  \__,_| \__,_| \___||_|
                                                                                       - By Tyizo , 
                                                                                       - Small Project.
=======================================================================================================\n""")
print(art)
try:
    link = input(green + '[+] Enter the link:')
    yt = YouTube(link)

    # Video Info , like title and views ... etc.

    print(green + '[+] Title : \n', yt.title)
    print(green + '[+] Views : \n', yt.views)
    print(green + '[+] Channel : \n', yt.author)
    print(green + '[+] Description : \n ', yt.description)
    print(green + '[+] Date : ', yt.publish_date)

    # Downloading and staff like that

    ys = yt.streams.get_highest_resolution()
    print(green + '[*] Downloading , just wait! ...')
    ys.download(link)
    input(green + '[*] Download completed!!')

except NameError:

    # Error Name
    error_color = fg(196)
    print(error_color + '[-] There is an error , try again later!')
    input(error_color + '[-] Press [enter] to exit.')
    exit()