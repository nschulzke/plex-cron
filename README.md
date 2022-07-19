# Getting started

1. Install Python 3

2. Install the dependencies:

```python
pip install -r requirements.txt
```

3. Create a new file called `secret.py` with the following content. Replace with the URL and port of your Plex server.

```python
# Replace with your own Plex URL, including port.
PLEX_URL = "http://0.0.0.0:0000"

# Replace with your Plex token. See link below on how to find it:
# https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
PLEX_TOKEN = "[YOUR_TOKEN_HERE]"
```

3. Edit cron.py to include the scheduled playlists and tracks you actually want to run. Modify the cast device and track/playlist name.

4. Save the cron tasks:

```sh
python cron.py
```
