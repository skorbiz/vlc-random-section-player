# vlc-random-section-player
A python script to play random section of videos using vlc.

Its uses the vlcs http interface to control video playback and as such should be compatible with both windows, mac, and linux.

##  Usage
Download and run the script as: 
```
python3 vlc-controller-http.py --duration 30 --skip-start 10 /path/to/videos
```

## Auto expand folders
To make vlc automatically open subfolders, edit the vlc setting:
```
Click 
--> Settings (select show "All" at the bottom") 
--> Playlist 
--> Subdirectory behavior
```

## To start VLC with http infterface manually
The script should launch vlc with the http interface automatically.

However, to launch vlc with http manually, etiher:
- Start using`'vlc --extraint http --http-password 123 <optional_content_path>`
- By configuring it in settings
  - See vlc documentation [here](https://wiki.videolan.org/VSG:Interface:HTTP/)
  - Set the password by going to a browser [http://localhost:8080]( http://localhost:8080) and follow instructions.


## Documentation on vlc's https interface
Link to vlcs documentation of its rest interface [vlc documentation](https://wiki.videolan.org/VLC_HTTP_requests/)

