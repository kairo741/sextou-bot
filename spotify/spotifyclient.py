import json
import os

import requests
import spotify.cover_image as cover_image

import spotify.track as track_class
import spotify.playlist as playlist_class


class SpotifyClient:
    """SpotifyClient performs operations using the Spotify API."""

    def __init__(self, authorization_token):
        """
        :param authorization_token (str): Spotify API token
        :param user_id (str): Spotify user id
        """
        self._authorization_token = authorization_token
        # self._user_id = user_id

    # def get_last_played_tracks(self, limit=10):
    #     """Get the last n tracks played by a user
    #
    #     :param limit (int): Number of tracks to get. Should be <= 50
    #     :return tracks (list of Track): List of last played tracks
    #     """
    #     url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
    #     response = self._place_get_api_request(url)
    #     response_json = response.json()
    #     tracks = [track_class.Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"])
    #               for
    #               track in response_json["items"]]
    #     return tracks

    def get_track_recommendations(self, genres, limit=50):
        url = f"https://api.spotify.com/v1/recommendations?seed_genres={genres}&limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        try:
            tracks = [track_class.Track(track["name"], track["id"], track["artists"][0]["name"]) for
                      track in response_json["tracks"]]
            return tracks
        except NameError:
            print(response_json)

    def create_playlist(self, name):
        data = json.dumps({
            "name": name,
            "description": "Sextouu AI AI AIAIAI 🔇 IAIAIAIAI (SEGUUU 🗡🗡💨 RA)",
            "public": True
        })
        url = f"https://api.spotify.com/v1/users/{os.environ['SPOTIFY_BOT_USER_ID']}/playlists"
        response = self._place_post_api_request(url, data)
        response_json = response.json()
        playlist_id = response_json["id"]
        # create playlist
        playlist = playlist_class.Playlist(name, playlist_id)

        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/images"
        self._place_put_api_request(url, cover_image.BASE_64)
        return playlist

    def populate_playlist(self, playlist, tracks):
        """Add tracks to a playlist.

        :param playlist (Playlist): Playlist to which to add tracks
        :param tracks (list of Track): Tracks to be added to playlist
        :return response: API response
        """
        track_uris = [track.create_spotify_uri() for track in tracks]
        data = json.dumps(track_uris)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response = self._place_post_api_request(url, data)
        response_json = response.json()
        return response_json

    def _place_get_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._authorization_token}"
            }
        )
        return response

    def _place_post_api_request(self, url, data):
        response = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._authorization_token}"
            }
        )
        return response

    def _place_put_api_request(self, url, data):
        response = requests.put(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._authorization_token}"
            }
        )
        return response
