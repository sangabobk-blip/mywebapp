import streamlit as st

import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="🔥 매운맛 MBTI 팩폭 여행지 추천",
    page_icon="✈️",
    layout="wide"
)

# 커스텀 스타일 적용 (자극적이고 세련된 디자인)
st.markdown("""
    <style>
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #FF4B4B;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.2rem;
        text-align: center;
        color: #555;
        margin-bottom: 2rem;
    }
    .mbti-card {
        background-color: #FFF0F0;
        border-left: 5px solid #FF4B4B;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 25px;
    }
    .dest-card {
        background-color: #F8F9FA;
        border: 1px solid #E9ECEF;
        border-radius: 12px;
        padding: 15px;
        height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .dest-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #1E1E1E;
        margin-top: 10px;
    }
    .dest-desc {
        font-size: 0.95rem;
        color: #444;
        line-height: 1.5;
        margin-top: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 16가지 MBTI 데이터 (자극적인 팩폭 + 고화질 이미지 + 최소 3개 여행지)
mbti_database = {
    "INTJ": {
        "tagline": "🧠 '인간 AI' 당신을 위한 완벽 통제 및 고독의 스케줄",
        "intro": "어설픈 여행지는 계획에 차질만 줄 뿐! 사람과의 감정 소비를 극도로 싫어하고 효율에 미친 당신을 위해 완벽한 통제와 안식을 제공합니다.",
        "destinations": [
            {
                "name": "🇨🇭 스위스 취리히 & 융프라우",
                "img": "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?w=800",
                "desc": "초단위로 딱딱 맞춰 구동되는 시스템. 대자연 속에서 유유자적으로 미개한(?) 인간들을 관조하기 최적의 장소입니다."
            },
            {
                "name": "🇮🇸 아이슬란드 레이캬비크",
                "img": "https://images.unsplash.com/photo-1504893524553-b855bce32c67?w=800",
                "desc": "지구가 멸망해도 이상하지 않을 황무지. 오로라를 보며 1인용 렌터카 안에서 혼자 우주의 원리를 정리하세요."
            },
            {
                "name": "🇸🇬 싱가포르",
                "img": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=800",
                "desc": "철저한 법과 질서로 완벽하게 통제된 인공 도시. 예측 불가능한 변수가 제로에 가까운 극강의 효율 여행지!"
            }
        ]
    },
    "INTP": {
        "tagline": "👽 방구석 지식인의 세상 건너뛰기 은둔 코스",
        "intro": "남들 다 가는 인스타 핫플은 사절. 오디오 비는 것도 상관없고 지적 호기심만 충족되면 장땡인 당신을 위한 마이웨이 여행지입니다.",
        "destinations": [
            {
                "name": "🇯🇵 도쿄 아키하바라",
                "img": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?w=800",
                "desc": "아무도 당신을 신경 쓰지 않는 미지의 지덕체 안식처. 하루 종일 혼자 매장을 헤매도 그 누구도 참견하지 않습니다."
            },
            {
                "name": "🇳🇴 노르웨이 스발바르",
                "img": "https://images.unsplash.com/photo-1517411032315-54ef2cb783bb?w=800",
                "desc": "북극곰이 사람보다 많은 지구 최북단. 세상과의 단절 속에서 방구석 철학관을 차리기에 최적인 곳입니다."
            },
            {
                "name": "🇨🇱 칠레 아타카마 사막",
                "img": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=800",
                "desc": "세계에서 별이 가장 잘 보이는 건조한 사막. 밤하늘을 보며 지평선 너머 양자역학을 고민해 보세요."
            }
        ]
    },
    "ENTJ": {
        "tagline": "👑 세계 정복을 꿈꾸는 야망가의 워커홀릭 피서지",
        "intro": "휴가지에서도 엑셀 켜고 자산관리 현황판을 볼 당신! 무의미하게 누워있는 시간은 죄악입니다. 야망을 자극하는 곳으로 가세요.",
        "destinations": [
            {
                "name": "🇺🇸 미국 뉴욕 맨해튼",
                "img": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=800",
                "desc": "치열하게 달리는 세계 자본주의의 중심지! 빌딩 숲 사이를 걸으며 '내가 저 건물들을 사버리겠다'는 도파민을 채우세요."
            },
            {
                "name": "🇬🇧 영국 런던 카나리 워프",
                "img": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800",
                "desc": "글로벌 금융가들의 속도감을 온몸으로 체감하며, 최고급 루프탑 바에서 비즈니스 구상을 하기 좋은 명소입니다."
            },
            {
                "name": "🇦🇪 아랍에미리트 두바이",
                "img": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800",
                "desc": "돈과 권력으로 만든 사막 위의 초고층 마천루! 최고 존엄 자본주의의 화려함을 오감으로 느껴볼 시간."
            }
        ]
    },
    "ENTP": {
        "tagline": "⚡️ 광기와 자극에 목마른 럭비공의 도파민 폭발지",
        "intro": "평범하고 지루한 패턴은 사절! 논쟁하고 상식을 깨부수는 것을 좋아하는 당신에게 매 순간 예측 불가능한 스릴을 선사합니다.",
        "destinations": [
            {
                "name": "🇹🇭 태국 방콕 카오산로드",
                "img": "https://images.unsplash.com/photo-1508009603885-50cf7c579365?w=800",
                "desc": "혼돈의 도가니 그 자체! 길거리 무작위 파티와 예측 불가능한 사람들과의 끝없는 티키타카가 펼쳐집니다."
            },
            {
                "name": "🇳🇱 네덜란드 암스테르담",
                "img": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?w=800",
                "desc": "자유와 파격의 끝판왕. 세상의 모든 편견과 규칙을 비웃듯 가장 기발하고 파격적인 예술과 문화를 만끽하세요."
            },
            {
                "name": "🇺🇸 미국 라스베이거스",
                "img": "https://images.unsplash.com/photo-1506146332389-18140dc7b2fb?w=800",
                "desc": "규칙 따위 개나 줘버려! 24시간 도파민과 한판 승부가 폭발하는 광기의 유흥 도시."
            }
        ]
    },
    "INFJ": {
        "tagline": "🌌 고독한 철학적 감성에 취하는 내면의 성지",
        "intro": "겉으론 웃지만 속으론 100가지 고민을 안고 사는 당신. 시끄러운 인싸 모임은 던져버리고 진짜 나를 만나는 고요함 속으로 가세요.",
        "destinations": [
            {
                "name": "🇯🇵 일본 교토",
                "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=800",
                "desc": "고즈넉한 대나무 숲길과 오래된 사찰. 혼자 조용히 걸으며 영혼의 깊은 곳까지 상찰하기 최적인 은신처."
            },
            {
                "name": "🇨🇿 체코 프라하",
                "img": "https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?w=800",
                "desc": "어두운 중세 골목길과 까를교의 노을. 혼자 일기장을 펴놓고 센티널한 신비로움에 빠지기 딱 좋은 도시."
            },
            {
                "name": "🏴󠁧󠁢󠁳󠁣󠁴󠁿 스코틀랜드 에든버러",
                "img": "https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?w=800",
                "desc": "고딕 양식의 웅장한 성과 돌길. 비 오는 날 카페 창가에 앉아 혼자 판타지 소설 구상하기 좋은 영감의 성지."
            }
        ]
    },
    "INFP": {
        "tagline": "💧 낭만에 살고 감성에 죽는 눈물겨운 피난처",
        "intro": "이어폰 끼고 우울한 음악 틀면 바로 영화 주인공 완성! 현실 감각은 살짝 내려놓고 몽환적인 꿈속으로 빠져들 시간입니다.",
        "destinations": [
            {
                "name": "🇫🇷 프랑스 파리",
                "img": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800",
                "desc": "센강 변에 앉아 아무 생각 없이 멍때려도 예술가가 된 기분! 감성 글귀 50줄이 절로 써지는 오리지널 낭만 도시."
            },
            {
                "name": "🇮🇹 이탈리아 피렌체",
                "img": "https://images.unsplash.com/photo-1543429776-2782fc8e1acd?w=800",
                "desc": "두오모 성당 지붕을 바라보며 사연 있는 표정 짓기. 르네상스 감성에 취해 가슴 시린 주옥같은 낭만을 누리세요."
            },
            {
                "name": "🇹🇭 태국 치앙마이",
                "img": "https://images.unsplash.com/photo-1528181304800-259b08848526?w=800",
                "desc": "조용한 올드시티 카페에서 일기 쓰고 책 읽기. 자아 찾기 여행의 성지에서 이상형을 꿈꿔보세요."
            }
        ]
    },
    "ENFJ": {
        "tagline": "❤️ 인류애 중독자의 세상 모든 사람 품어주기 코스",
        "intro": "어딜 가나 리더 역할을 맡아 남 챙기느라 지친 당신! 이제는 당신의 넘치는 따뜻함과 열정을 온몸으로 환영해 주는 곳으로 가세요.",
        "destinations": [
            {
                "name": "🇪🇸 스페인 바르셀로나",
                "img": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800",
                "desc": "지나가는 모든 이와 친구가 될 수 있는 미친 열정! 밤새 타파스를 나누고 인류애를 격하게 충전하세요."
            },
            {
                "name": "🇧🇷 브라질 리우데자네이루",
                "img": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=800",
                "desc": "쌈바 리듬 속에 온 세상 사람들을 꼭 끌어안을 수 있는 에너지 폭발 구역! 모두가 하나 되는 진정한 축제."
            },
            {
                "name": "🇮🇪 아일랜드 더블린",
                "img": "https://images.unsplash.com/photo-1549918864-48ac978761a4?w=800",
                "desc": "동네 펍에 들어가 10분 만에 현지인들과 어깨동무하고 유쾌한 인생 이야기를 나눌 수 있는 인싸 천국."
            }
        ]
    },
    "ENFP": {
        "tagline": "🎈 3초 만에 딴길로 새는 무계획 비타민의 도파민 탐험",
        "intro": "계획? 그게 뭐죠? 맛있는 냄새나 예쁜 등불만 보면 발길 닿는 대로 움직이는 인간 비타민을 위한 스펙타클 놀이터입니다.",
        "destinations": [
            {
                "name": "🇻🇳 베트남 다낭 & 호이안",
                "img": "https://images.unsplash.com/photo-1528127269322-539801943592?w=800",
                "desc": "알록달록 노란 등불 거리에서 길을 잃어도 대만족! 흥정하다 상인이랑 웃음 터지는 엉뚱 발랄 피서지."
            },
            {
                "name": "🇲🇽 메밀 멕시코 칸쿤",
                "img": "https://images.unsplash.com/photo-1510097467424-192d713be8b2?w=800",
                "desc": "흥분지수 200%! 일단 올인클루시브 리조트에 던져지면 24시간 춤추고 노래하며 세상의 모든 신남을 누립니다."
            },
            {
                "name": "🇺🇸 미국 하와이 오아후",
                "img": "https://images.unsplash.com/photo-1542259009477-d625272157b7?w=800",
                "desc": "무지개가 뜨는 해변에서 훌라춤을 추며 당장 옆 사람과 친구 먹는 미친 텐션 허용 구역."
            }
        ]
    },
    "ISTJ": {
        "tagline": "📏 0.1초의 오차도 용납하지 않는 극강 질서의 마스터피스",
        "intro": "계획표에서 5분만 틀어져도 스트레스 받는 당신! 칼같은 질서와 안전, 체계적인 동선이 보장된 최상의 안식처를 드립니다.",
        "destinations": [
            {
                "name": "🇩🇪 독일 뮌헨",
                "img": "https://images.unsplash.com/photo-1595867818082-083862f3d630?w=800",
                "desc": "정확한 기차 시간, 깔끔한 도시 정비! 칼같이 움직이는 시스템 속에서 마음의 평화와 시원한 맥주를 얻으세요."
            },
            {
                "name": "🇯🇵 일본 도쿄",
                "img": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800",
                "desc": "정갈함과 정돈됨의 대명사. 길거리에 쓰레기 하나 없고 예측 가능하여 마음이 지극히 편안해집니다."
            },
            {
                "name": "🇦🇹 오스트리아 비엔나",
                "img": "https://images.unsplash.com/photo-1516550893923-42d28e5677af?w=800",
                "desc": "클래식하고 완벽하게 정돈된 오스트리아의 정수. 오차 없는 가이드 투어로 교양 점수를 대폭 끌어올리세요."
            }
        ]
    },
    "ISFJ": {
        "tagline": "🧸 남 챙기다 지친 영혼을 위한 포근한 힐링 대피소",
        "intro": "항상 남들 배려하느라 속병 난 당신! 이제 남은 신경 쓰지 말고 오직 나만을 위한 따뜻한 온천과 힐링 푸드로 위로받으세요.",
        "destinations": [
            {
                "name": "🇯🇵 일본 후쿠오카 유후인",
                "img": "https://images.unsplash.com/photo-1528164344705-47542687990d?w=800",
                "desc": "따뜻한 료칸 온천에 몸을 녹이고 정갈한 가이세키 요리를 먹으며 그동안 쌓인 스트레스를 싹 씻어내세요."
            },
            {
                "name": "🇨🇭 스위스 루체른",
                "img": "https://images.unsplash.com/photo-1527668752968-14dc70a27c95?w=800",
                "desc": "범죄율 제로에 가까운 평화롭고 고요한 호수 마을. 사건사고 걱정 없이 마음 편히 거닐 수 있는 안심 구역."
            },
            {
                "name": "🇹🇭 태국 치앙마이 리조트",
                "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800",
                "desc": "친절한 사람들의 응대 속에서 친절 과다 복용! 따뜻한 마사지로 온몸의 피로를 사르르 녹여주는 곳."
            }
        ]
    },
    "ESTJ": {
        "tagline": "📢 효율성과 가성비에 미친 지도자의 완벽 가이드",
        "intro": "동선 낭비는 참을 수 없다! 가장 빠른 시간 내에 최고의 생산성과 만족도를 뽑아내는 관리형 명소들을 모았습니다.",
        "destinations": [
            {
                "name": "🇸🇬 싱가포르",
                "img": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=800",
                "desc": "관광, 쇼핑, 휴양을 동선 낭비 없이 완벽하게 마스터할 수 있는 체계적으로 관리된 최고 효율의 도시."
            },
            {
                "name": "🇩🇪 독일 프랑크푸르트",
                "img": "https://images.unsplash.com/photo-1565618198079-bc223aa34542?w=800",
                "desc": "유럽 비즈니스 중심지의 정교함! 합리적인 일정과 착착 진행되는 투어 코스로 가성비/고효율 승리 달성."
            },
            {
                "name": "🇺🇸 미국 워싱턴 D.C.",
                "img": "https://images.unsplash.com/photo-1501466044931-62695aada8e9?w=800",
                "desc": "질서정연한 격자형 도로 체계와 유익한 박물관이 일렬로 늘어선 생산성 200%의 학습 겸 여행지."
            }
        ]
    },
    "ESFJ": {
        "tagline": "📸 인스타 피드 300장 업로드! 친목 도모 인생샷 성지",
        "intro": "내가 잘 나온 것보다 남들과 함께 행복한 사진 남기는 게 최고! 사랑하는 사람들과 추억 만들기에 최적화된 최강 핫플입니다.",
        "destinations": [
            {
                "name": "🇮🇹 이탈리아 포시타노",
                "img": "https://images.unsplash.com/photo-1533105079780-92b9be482077?w=800",
                "desc": "어디서 찍어도 인생샷 완성! 절벽 마을과 푸른 바다 배경으로 단체 사진 3,000장 남기고 인스타 업로드 폭주."
            },
            {
                "name": "🇬🇷 그리스 산토리니",
                "img": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=800",
                "desc": "파란 지붕과 하얀 벽. 남들과 함께 웃으며 맛있는 와인을 마시는 낭만 가득 추억 저장소."
            },
            {
                "name": "🇫🇷 프랑스 니스",
                "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800",
                "desc": "지중해 햇살 아래 친한 사람들과 맛있는 파스타 먹으며 웃음꽃 피우기 좋은 감성 해변."
            }
        ]
    },
    "ISTP": {
        "tagline": "🏎️ 말 많은 놈은 질색! 오직 스릴과 익스트림 마이웨이",
        "intro": "귀찮은 가이드 설명은 됐고, 온몸의 세포가 깨어나는 익스트림 스포츠나 혼자만의 정적을 느끼고 싶은 야생 동물용 코스입니다.",
        "destinations": [
            {
                "name": "🇳🇿 뉴질랜드 퀸스타운",
                "img": "https://images.unsplash.com/photo-1507699622108-4be3abd695ad?w=800",
                "desc": "번지점프, 스카이다이빙, 샷오버 제트! 쓸데없는 대화 없이 도파민만 제대로 충전하는 액티비티 천국."
            },
            {
                "name": "🇺🇸 미국 모압 (유타)",
                "img": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=800",
                "desc": "오프로드 SUV 끌고 바위산을 누비는 사나이의 땅! 거친 대자연과 고독을 즐기기엔 여길 따라올 곳이 없음."
            },
            {
                "name": "🇮🇸 아이슬란드 싱벨리르",
                "img": "https://images.unsplash.com/photo-1504893524553-b855bce32c67?w=800",
                "desc": "대륙판 사이 스쿠버 다이빙! 말없이 물속에 들어가 차가운 정적을 만끽하는 극한의 마이웨이."
            }
        ]
    },
    "ISFP": {
        "tagline": "🛋️ 침대 밖은 위험해! 풀빌라 누워있기 극강 코스",
        "intro": "아무것도 안 하고 가만히 누워만 있어도 '크 감성 있다' 소리 나오는 곳. 발끝 하나 안 움직이고 쉬는 게 진정한 여행입니다.",
        "destinations": [
            {
                "name": "🇮🇩 인도네시아 발리 우붓",
                "img": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=800",
                "desc": "초록빛 숲속 풀빌라 침대에 누워 생과일주스 흡입하기. 누워만 있어도 예술가 기분을 누리는 게으름 허용 구역."
            },
            {
                "name": "🇺🇸 미국 하와이 호놀룰루",
                "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800",
                "desc": "따스한 모래사장에 누워 멍하니 파도 소리 듣기. 하루 종일 아무것도 안 해도 그 누구도 눈치 주지 않습니다."
            },
            {
                "name": "🇹🇭 태국 코사무이",
                "img": "https://images.unsplash.com/photo-1537956965359-7573183d1f57?w=800",
                "desc": "마사지받고 자고, 먹고 또 누워있기. 극강의 누워있기 대장을 위한 완벽한 트로피컬 안식처."
            }
        ]
    },
    "ESTP": {
        "tagline": "🎰 오늘만 산다! 24시간 돈과 도파민이 휘몰아치는 전장",
        "intro": "화려한 조명, 미친 음악, 오늘 밤을 불태울 자극적인 승부! 망설임 없이 직진하는 당신을 위한 스릴 만점 명소들.",
        "destinations": [
            {
                "name": "🇺🇸 미국 라스베이거스",
                "img": "https://images.unsplash.com/photo-1506146332389-18140dc7b2fb?w=800",
                "desc": "화려한 카지노와 거대한 쇼! 자극과 도파민을 극한까지 끌어올려 끝장나게 돈 쓰고 노는 일탈의 현장."
            },
            {
                "name": "🇪🇸 스페인 이비자",
                "img": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800",
                "desc": "세계 최고 EDM 클럽과 해변 파티! 아침 해가 뜰 때까지 멈추지 않고 미치도록 노는 인생의 피크 타임."
            },
            {
                "name": "🇺🇸 미국 마이애미",
                "img": "https://images.unsplash.com/photo-1506966953602-c20cc11f75e3?w=800",
                "desc": "슈퍼카 엔진 소리와 비키니 파티! 스피드와 도파민을 즐기는 직진남녀를 위한 최고의 미아애미 비치."
            }
        ]
    },
    "ESFP": {
        "tagline": "🎉 내가 바로 주인공! 세상의 모든 흥을 모은 파티원",
        "intro": "어딜 가나 모임의 중심! 관종력과 흥이 넘쳐흘러 주체할 수 없는 당신에게 세계 최고 레벨의 축제를 바칩니다.",
        "destinations": [
            {
                "name": "🇪🇸 스페인 이비자",
                "img": "https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=800",
                "desc": "여기보다 당신에게 어울리는 곳은 없음! 스테이지 중앙에서 춤추며 흥을 폭발시키는 슈퍼 인싸들의 성지."
            },
            {
                "name": "🇧🇷 브라질 리우 카니발",
                "img": "https://images.unsplash.com/photo-1516307365426-bea591f05011?w=800",
                "desc": "화려한 의상과 음악, 미친 퍼레이드! 세상 모든 사람들의 시선을 집중시키는 최고의 무대."
            },
            {
                "name": "🇹🇭 태국 코팡안 풀문 파티",
                "img": "https://images.unsplash.com/photo-1533105079780-92b9be482077?w=800",
                "desc": "보름달 아래 형광 페인트를 바르고 전 세계 배낭족들과 야광 댄스를 즐기는 미친 텐션의 해변 파티."
            }
        ]
    }
}

# --- 메인 화면 UI ---
st.markdown("<div class='main-title'>🔥 팩폭 주의! MBTI 매운맛 여행지 추천</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>위선은 빼고! 당신의 숨겨진 도파민과 본능을 자극하는 맞춤 여행지 3곳을 공개합니다.</div>", unsafe_allow_html=True)

# MBTI 선택 드롭다운
selected_mbti = st.selectbox(
    "👉 당신의 MBTI 유형을 선택하세요:",
    list(mbti_database.keys()),
    index=0
)

# 버튼
if st.button("🚨 내 맞춤 팩폭 여행지 3곳 공개!", type="primary", use_container_width=True):
    st.balloons()
    
    data = mbti_database[selected_mbti]
    
    # MBTI 요약 카드
    st.markdown(f"""
    <div class="mbti-card">
        <h2 style="color: #FF4B4B; margin-top:0;">[{selected_mbti}] {data['tagline']}</h2>
        <p style="font-size: 1.1rem; color: #333; margin-bottom: 0;"><b>⚡️ 팩폭 한마디:</b> {data['intro']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader(f"📍 {selected_mbti} 추천 여행지 TOP 3")
    st.write("")
    
    # 3개 여행지 카드를 3개 컬럼으로 배치
    cols = st.columns(3)
    
    for idx, dest in enumerate(data["destinations"]):
        with cols[idx]:
            st.image(dest["img"], use_container_width=True)
            st.markdown(f"<div class='dest-title'>{dest['name']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='dest-desc'>{dest['desc']}</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("💡 참고: 본 앱은 파이썬 기본 제공 기능과 Streamlit 표준 기능만으로 제작되었습니다. 일단 비행기표부터 예매하세요!")
