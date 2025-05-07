## 감정 기반 음악 추천 챗봇

사용자 감정을 분석하고 해당 감정에 맞는 음악을 추천하는 챗봇입니다.

---

### 📁 프로젝트 구조

- 'chatbot.py': 사용자와 대화를 주고받는 챗봇 인터페이스
- 'recommendation.py': 감정 키워드 기반 Spotify 음악 추천 로직
- 'emotion.py': 사용자의 대화에서 감정 분석을 수행하는 로직 (API가 아닌 실제로 모델을 구현)
- 'main.py': 이 모든 파일이 합쳐진 완성본

---

### ⚙️ 환경 설정

1. '.env.example'을 복사하여 '.env' 파일을 생성하고 다음 정보를 입력합니다:

SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080/callback

이 정보들은 각자 본인의 Spotify 개발자 계정에서 발급한 값으로 .env 내용을 채워야합니다.

2. 필요한 패키지 설치

pip install -r requirements.txt

