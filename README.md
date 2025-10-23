# 🧠 My Own ChatGPT — Professional Prompt Maker

LangChain + Streamlit + LangSmith API를 활용하여 **전문적인 프롬프트 변환 및 테스트 환경**을 제공합니다.  
이 앱은 사용자가 입력한 질문과 Task를 기반으로, LangSmith Prompt Hub에서 불러온 프롬프트를 활용해 맞춤형 응답을 생성합니다.

---

## 🚀 Features

- 🧩 **LangSmith Prompt 연동**:  
  `hardkothari/prompt-maker` 등 등록된 프롬프트를 불러와 즉시 사용 가능.
- 💬 **ChatGPT 스타일 UI**:  
  Streamlit의 `st.chat_message` 기능으로 구현한 실시간 대화형 인터페이스.
- ⚙️ **Task 기반 프롬프트 변형**:  
  사이드바에서 `TASK`를 입력하면, 해당 태스크가 자동으로 프롬프트에 반영됩니다.
- 🔁 **대화 히스토리 관리 / 초기화 버튼 지원**
- 🧵 **Streaming Response**:  
  LLM의 응답을 실시간 토큰 스트리밍 방식으로 표시합니다.

---

## 🧰 Tech Stack

| 구성 요소 | 역할 |
|------------|------|
| **Streamlit** | 프론트엔드 UI 구성 및 실시간 채팅 인터페이스 |
| **LangChain** | 체인 구성 및 LLM 응답 파이프라인 관리 |
| **LangSmith** | 프롬프트 버전 관리 및 로드 |
| **OpenAI API** | GPT-4o-mini 모델을 사용하여 응답 생성 |
| **dotenv** | 환경변수(.env) 관리 |

---

## 📂 Project Structure

📦 my-own-chatgpt
├── app.py # Streamlit 메인 실행 파일
├── .env # API Keys (LangSmith, OpenAI 등)
├── requirements.txt # 필요한 라이브러리
└── README.md

---

## ⚙️ Installation

1. **저장소 클론**
   ```bash
   git clone https://github.com/Yangms30/prompt_maker.git
   cd prompt_maker
가상환경 생성 및 활성화

python3 -m venv venv
source venv/bin/activate   # (macOS/Linux)
필요 라이브러리 설치

bash
코드 복사
pip install -r requirements.txt
환경 변수 설정
프로젝트 루트에 .env 파일을 생성하고 다음을 입력하세요:


OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
LANGSMITH_API_KEY=ls-xxxxxxxxxxxxxxxx
▶️ Run

streamlit run app.py
브라우저에서 자동으로 열리지 않는 경우,
http://localhost:8501 로 접속하세요.

💡 Usage
사이드바의 TASK 입력란에 특정 프롬프트 작업을 입력합니다.
(예: 영문 마케팅 문장으로 변환, 이력서 문체로 바꾸기, 데이터 분석 보고서 스타일로 변환)

메인 화면 하단 입력창에 질문을 입력하고 Enter를 누릅니다.
→ LangSmith에서 지정한 프롬프트를 기반으로, 전문적인 응답이 실시간으로 생성됩니다.

“대화 초기화” 버튼으로 모든 대화 기록을 초기화할 수 있습니다.



🧩 Example Prompt (LangSmith)
현재 Client().pull_prompt("hardkothari/prompt-maker") 로 불러오는 프롬프트는
LangSmith Prompt Hub에 등록된 전문 프롬프트를 자동으로 가져옵니다.

👉 직접 커스터마이징하려면 LangSmith Prompt Hub에서
새로운 프롬프트를 만들어 "username/prompt-name" 형태로 바꿔주세요.


