# This is loosely based on https://superuser.com/questions/81044/playback-random-section-from-multiple-videos-changing-every-5-minutes

import random
import time
import subprocess
from requests import get
from requests.auth import HTTPBasicAuth
import argparse

host = "localhost:8080"
user = ""
password = "supersecret"

duration_in_seconds = 30
skip_start_seconds = 0

vlc_args = []

NEXT = "?command=pl_next"
SEEK = "?command=seek&val={}"
FULL_SCREEN = "?command=fullscreen"


def vlc(cmd = ""):
    response = get(f"http://{host}/requests/status.json{cmd}", auth=HTTPBasicAuth(user, password))    
    return response

def open_vlc(vlc_args):
    cmd = "vlc --extraint http --http-password {password} {args}".format(password=password, args=" ".join(vlc_args))
    vlc_process = subprocess.Popen(cmd.split())
    time.sleep(5) # Wait for VLC to start

def parse_args():
    parser = argparse.ArgumentParser(
        # description='Play random sections of videos in VLC.', 
        epilog="  Unknown arguments are passed to VLC \n\nExample usage:\n  python3 %(prog)s --duration 30 --skip-start 0 /path/to/videos", 
        usage='%(prog)s [options] [vlc options]', 
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-d", "--duration", help="Duration of each video in seconds", default=duration_in_seconds, type=int)
    parser.add_argument("-s", "--skip-start", help="Skip the first seconds of videos", default=skip_start_seconds, type=int)
    args, unknownargs = parser.parse_known_args()
    return args.duration, args.skip_start, unknownargs


# Run VLC with http interface
duration_in_seconds, skip_start_seconds, vlc_args = parse_args()
open_vlc(vlc_args)

## Loop forever
while True:
    vlc(NEXT)

    try:
        ## Choose random start time
        total_length = vlc().json()["length"]
        start_time = random.randint(skip_start_seconds, total_length - duration_in_seconds)
        vlc(SEEK.format(start_time))

        ## Enable fullscreen
        #vlc(FULL_SCREEN) # Seems like a toggle?

        ## Output
        print("Playing: ", vlc().json()["information"]["category"]["meta"]["filename"])
        print("playing at time: ", vlc().json()["time"])
        print("Expeced: ", start_time)

        ## Sleep for the specified interval
        time.sleep(duration_in_seconds)   

    except ValueError:
        print("Something went wrong. Trying next video")
        time.sleep(1)   