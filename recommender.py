import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
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

# 감정 입력 (사용자 입력 기준)
emotion = '기쁨'

# 검색어 추출
query = emotion_to_query.get(emotion, emotion)

# 플레이리스트 검색
results = sp.search(q=query, type='playlist', limit=20)
playlists = results['playlists']['items']

# '찬양' 포함된 항목 제외
filtered = [
    p for p in playlists
    if p is not None and '찬양' not in (p.get('name', '') + p.get('description', ''))
]

# 랜덤 추천
if filtered:
    playlist = random.choice(filtered)  # 🎯 랜덤 선택
    playlist_id = playlist['id']
    playlist_name = playlist['name']
    print(f"🎧 감정: {emotion}")
    print(f"📚 추천 플레이리스트: {playlist_name}")
    print(f"🔗 링크: {playlist['external_urls']['spotify']}\n")

    # 곡 5개 출력
    tracks = sp.playlist_tracks(playlist_id, limit=5)
    for t in tracks['items']:
        track = t['track']
        name = track['name']
        artist = track['artists'][0]['name']
        url = track['external_urls']['spotify']
        print(f"🎵 {name} - {artist}\n   🔗 {url}\n")
else:
    print(f"❌ '{emotion}' 감정에 맞는 플레이리스트를 찾지 못했습니다.")