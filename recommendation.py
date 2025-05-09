import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import random

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    redirect_uri = REDIRECT_URI,
    scope = 'user-read-private'
))

emotion_to_query = {
    '기쁨': '기분 좋아지는 노래',
    '슬픔': '슬픈 노래 모음',
    '분노': '화날 때 듣는 노래',
    '힐링': '마음이 편안해지는 노래'
}

def recommend_music_by_emotion(emotion: str):
    """
    감정 키워드에 따라 Spotify에서 음악을 추천하는 함수

    Parameters:
        emotion (str): 사용자의 감정 ('기쁨', '슬픔', '분노', '힐링' 등)

    Returns:
        dict | None: 추천된 플레이리스트 및 곡 정보를 담은 dict
                     (플레이리스트 이름, 링크, 곡 리스트), 추천 실패 시 None
    """
    query = emotion_to_query.get(emotion, emotion)
    results = sp.search(q=query, type='playlist', limit=20)
    playlists = results['playlists']['items']

    filtered = [
        p for p in playlists
        if p is not None and '찬양' not in (p.get('name', '') + p.get('description', ''))
    ]

    if not filtered:
        return None

    playlist = random.choice(filtered)
    playlist_id = playlist['id']
    playlist_name = playlist['name']
    playlist_url = playlist['external_urls']['spotify']

    tracks_data = sp.playlist_tracks(playlist_id, limit=3, market="KR")
    songs = []

    for t in tracks_data['items']:
        track = t['track']
        name = track['name']
        artist = track['artists'][0]['name']
        url = track['external_urls']['spotify']
        songs.append({
            'name': name,
            'artist': artist,
            'url': url
        })

    return {
        'emotion': emotion,
        'playlist_name': playlist_name,
        'playlist_url': playlist_url,
        'songs': songs
    }
    
# 이건 main.py에 붙여넣기 해야함.    
# from recommendation import recommend_music_by_emotion

result = recommend_music_by_emotion('기쁨')

if result:
    print(f"🎧 감정: {result['emotion']}")
    print(f"📚 추천 플레이리스트: {result['playlist_name']}")
    print(f"🔗 링크: {result['playlist_url']}\n")

    for song in result['songs']:
        print(f"🎵 {song['name']} - {song['artist']}\n   🔗 {song['url']}\n")
else:
    print("❌ 감정에 맞는 플레이리스트를 찾지 못했습니다.")