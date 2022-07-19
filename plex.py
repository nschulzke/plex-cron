import argparse
import sys

from plexapi.server import PlexServer

import pychromecast
from pychromecast.controllers.plex import PlexController

import random
import secret

parser = argparse.ArgumentParser(description='Play a Plex playlist.')

parser.add_argument('device', type=str, help='The device on which to play')
parser.add_argument('playlist', type=str, help='The playlist to play')
parser.add_argument('--shuffle', dest='shuffle', default=False, action='store_true')
parser.add_argument('--volume', type=int, default=None)

args = parser.parse_args()

CAST_NAME = args.device
PLEX_URL = secret.PLEX_URL
PLEX_TOKEN = secret.PLEX_TOKEN

# Library of items to pick from for tests. Use "episode", "movie", or "track".
PLEX_LIBRARY = "track"

chromecasts, browser = pychromecast.get_listed_chromecasts(
    friendly_names=[CAST_NAME]
)
cast = next((cc for cc in chromecasts if cc.name == CAST_NAME), None)

if not cast:
    print(f"No chromecast with name '{CAST_NAME}' found.")
    foundCasts = ", ".join([cc.name for cc in pychromecast.get_chromecasts()[0]])
    print(f"Chromecasts found: {foundCasts}")
    sys.exit(1)

plex_server = PlexServer(PLEX_URL, PLEX_TOKEN)

media = plex_server.playlist(args.playlist).items()

if (args.shuffle):
    random.shuffle(media)

plex_c = PlexController()
cast.register_handler(plex_c)
cast.wait()

if (args.volume is not None):
    plex_c.set_volume(args.volume)

plex_c.block_until_playing(media)

browser.stop_discovery()
