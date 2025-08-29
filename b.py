import streamlit as st

st.set_page_config(page_title="숙명여자대학교 좌석 추천 시스템", layout="wide")

for key in ["logged_in", "seat", "show_seat_select"]:
    if key not in st.session_state:
        st.session_state[key] = False if key != "seat" else ""

# 로그인
if not st.session_state.logged_in:
    st.title("숙명여자대학교 도서관 좌석 추천 시스템 로그인")
    user_id = st.text_input("ID")
    user_pw = st.text_input("PW", type="password")

    if st.button("로그인"):
        if user_id and user_pw:
            st.session_state.logged_in = True
            st.success("로그인 성공!")
        else:
            st.error("ID와 PW를 모두 입력하세요.")

if st.session_state.logged_in:
    st.title("해당하는 항목을 입력하시면 도서관 좌석을 추천해드려요:)")

    talk = st.checkbox("대화 허용")
    typing = st.checkbox("타이핑 허용")
    eating = st.checkbox("음식 섭취 허용")
    people = st.slider("인원 수 선택", 1, 6, 1)
    noise = st.slider("주변 소음 허용 수준 선택", 1, 5, 1)

    if st.button("추천받기"):
        if people == 1 and not talk and not typing and not eating and noise <= 2:
            st.session_state.seat = "🌞 세계여성문학관"
        elif people == 1 and talk and typing and not eating and 3 <= noise <= 4:
            st.session_state.seat = "🛋️ 1층 신한로비"
        elif people == 1 and talk and typing and not eating and noise >= 4:
            st.session_state.seat = "💡 2층 DICA 플라자 또는 SMART 플라자 양끝 1인석"
        else:
            st.session_state.seat = "🪑 2층 일반 열람석 또는 5층 C.C 플라자"

        st.success(f"추천 좌석: {st.session_state.seat}")

        seat_images = {
            "🛋️ 1층 신한로비": [
                r"academicfestimage/1sh.jpg"
            ],
            "🌞 세계여성문학관": [
                r"academicfestimage/1sym.jpg"
            ],
            "💡 2층 DICA 플라자 또는 SMART 플라자 양끝 1인석": [
                r"academicfestimage/2dica.jpg",
                r"academicfestimage/2smart.jpg"
            ],
            "📘 3층 자료실 A 또는 B 또는 6층 S4열람실": [
                r"academicfestimage/3A.jpg",
                r"academicfestimage/3B.jpg",
                r"academicfestimage/6s4.jpg"
            ],
            "📚 4층 자료실": [
                r"academicfestimage/4.jpg"
            ],
            "🍽️ 5층 C.C 플라자": [
                r"academicfestimage/5cc.jpg"
            ],
            "🔕 6층 S1~S3열람실": [
                r"academicfestimage/6s1.jpg",
                r"academicfestimage/6s2.jpg",
                r"academicfestimage/6s3.jpg"
            ],
            "🪑 2층 일반 열람석 또는 5층 C.C 플라자": [
                r"academicfestimage/2dica.jpg",
                r"academicfestimage/2smart.jpg",
                r"academicfestimage/5cc.jpg"
            ]
        }

        clean_seat = st.session_state.seat.strip()
        if clean_seat in seat_images:
            for img_path in seat_images[clean_seat]:
                st.image(img_path, caption=clean_seat, width=600)

    # 예약 버튼
    if st.session_state.seat and st.button("예약하러 가기"):
        st.session_state.show_seat_select = True

    # 예약창 표시
    if st.session_state.show_seat_select:
        st.subheader("희망 좌석을 선택하세요")

        if st.session_state.seat=='🛋️ 1층 신한로비':
            st.title("1층-신한로비의 희망 좌석 번호를 지정하세요")
            options=list(range(1,51))
            selected=st.selectbox('좌석 번호를 선택하세요: ', options)
            st.write('좌석 번호: ',selected)
        elif st.session_state.seat=='🌞 세계여성문학관':
            st.title("1층-세계여성문학관의 희망 좌석 번호를 지정하세요")
            options=list(range(1,58))
            selected=st.selectbox('좌석 번호를 선택하세요: ', options)
            st.write('좌석 번호: ',selected)
        elif st.session_state.seat=='2층 DICA 플라자 또는 SMART 플라자 양끝 1인석':
            st.title("2층 1인석의 희망 구역을 선택하세요")
            options1=['DICA 플라자','SMART플라자']
            selected1=st.selectbox('희망 구역을 지정하세요: ', options1)
            if selected1=='DICA 플라자':
                st.title("2층-DICA 플라자의 희망 좌석 번호를 지정하세요")
                options=list(range(1,25))+list(range(64,71))
                selected=st.selectbox('좌석 번호를 선택하세요: ', options)
                st.write('좌석 번호: ',selected)
            elif selected1=='SMART 플라자':
                st.title("2층-SMART 플라자의 희망 좌석 번호를 지정하세요")
                options=list(range(1,10))+list(range(130,142))
                selected=st.selectbox('좌석 번호를 선택하세요: ', options)
                st.write('좌석 번호: ',selected)
        elif st.session_state.seat=='📘 3층 자료실 A 또는 B 또는 6층 S4열람실"':
            st.title("희망 구역을 선택하세요")
            options1=['자료실A','자료실B','6층 S4열람실']
            selected1=st.selectbox('희망 구역을 지정하세요: ', options1)
            if selected1=='자료실A':
                st.title("3층-자료실A의 희망 좌석 번호를 지정하세요")
                options=list(range(1,85))
                selected=st.selectbox('좌석 번호를 선택하세요: ', options)
                st.write('좌석 번호: ',selected)
            elif selected1=='자료실B':
                st.title("3층-자료실B의 희망 좌석 번호를 지정하세요")
                options=list(range(1,41))
                selected=st.selectbox('좌석 번호를 선택하세요: ', options)
                st.write('좌석 번호: ',selected)
            elif selected1=='6층 S4열람실':
                st.title("6층-S4열람실의 희망 좌석 번호를 지정하세요")
                options=list(range(1,40))
                selected=st.selectbox('좌석 번호를 선택하세요: ', options)
                st.write('좌석 번호: ',selected)
        elif st.session_state.seat=='📚 4층 자료실':
                st.title("4층-자료실의 희망 좌석 번호를 지정하세요")
                options=list(range(1,85))
                selected=st.selectbox('좌석 번호를 선택하세요: ', options)
                st.write('좌석 번호: ',selected)
        elif st.session_state.seat=='👥 3층 스터디룸 2인실':
                st.title("3층-스터디룸 2인실의 희망 스터디룸 번호를 지정하세요")
                options=list(range(31,39))
                selected=st.selectbox('스터디룸 번호를 선택하세요: ', options)
                st.write('스터디룸 번호: ',selected)
        elif st.session_state.seat=='👨‍👩‍👧‍👦 5층 스터디룸 4~6인실':
                st.title("5층-스터디룸 4~6인실의 희망 스터디룸 번호를 지정하세요")
                options=list(range(51,55))+['상상부스1','상상부스2','상상부스3','상상부스4','상상부스5','상상부스6']
                selected=st.selectbox('스터디룸 번호를 선택하세요: ', options)
                st.write('스터디룸 번호: ',selected)
        elif st.session_state.seat=='🔕 6층 S1~S3 열람실':
            st.title("6층 열람실의 희망 구역을 선택하세요")
            options1=['S1열람실','S2열람실','S3열람실']
            selected1=st.selectbox('희망 구역을 지정하세요: ', options1)
            if selected1=='S1열람실':
                st.title("6층-S1열람실의 희망 좌석 번호를 지정하세요")
                options=list(range(1,77))
                selected=st.selectbox('좌석 번호를 선택하세요: ', options)
                st.write('좌석 번호: ',selected)
            elif selected1=='S2열람실':
                st.title("6층-S2열람실의 희망 좌석 번호를 지정하세요")
                options=list(range(1,79))
                selected=st.selectbox('좌석 번호를 선택하세요: ', options)
                st.write('좌석 번호: ',selected)
            elif selected1=='S3열람실':
                st.title("6층-S3열람실의 희망 좌석 번호를 지정하세요")
                options=list(range(1,125))
                selected=st.selectbox('좌석 번호를 선택하세요: ', options)
                st.write('좌석 번호: ',selected)
        elif st.session_state.seat=='🍽️ 5층 C.C 플라자':
            st.title("5층-C.C 플라자의 희망 좌석 번호를 지정하세요")
            options=list(range(1,71))
            selected=st.selectbox('좌석 번호를 선택하세요: ', options)
            st.write('좌석 번호: ',selected)
        elif st.session_state.seat=='🪑 2층 일반 열람석 또는 5층 C.C 플라자':
            st.title("희망 구역을 선택하세요")
            options1=['2층 일반 열람석','5층 C.C 플라자']
            selected1=st.selectbox('희망 구역을 지정하세요: ', options1)
            if selected1=='2층 일반 열람석':
                st.title("2층-일반 열람석의 희망 구역을 지정하세요")
                options2=['DICA 플라자','SMART 플라자']
                selected2=st.selectbox('희망 구역을 지정하세요: ', options2)
                if selected2=='DICA 플라자':
                    st.title("2층-DICA 플라자의 희망 좌석 번호를 지정하세요")
                    options=list(range(25,64))+list(range(71,95))
                    selected=st.selectbox('좌석 번호를 선택하세요: ', options)
                    st.write('좌석 번호: ',selected)
                elif selected2=='SMART 플라자':
                    st.title("2층-SMART 플라자의 희망 좌석 번호를 지정하세요")
                    options=list(range(10,122))
                    selected=st.selectbox('좌석 번호를 선택하세요: ', options)
                    st.write('좌석 번호: ',selected)
            elif selected1=='5층 C.C 플라자':
                st.title("5층-C.C 플라자의 희망 좌석 번호를 지정하세요")
                options=list(range(1,71))
                selected=st.selectbox('좌석 번호를 선택하세요: ', options)
                st.write('좌석 번호: ',selected)
        if st.button("예약하기"):
            st.success(f"✅️예약이 완료되었습니다!")




