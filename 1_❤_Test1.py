from re import A
import streamlit as st

st.title("달리 테스트 1")

# input_user_name = st.text_input(label="User Name", value="default value")
# radio_gender = st.radio(label="Gender", options=["Male", "Female"])
# check_1 = st.checkbox(label="agree", value=False)
# memo = st.text_area(label="memo", value="")

# list1 = ['연애','좋은변화','창의성','배움성장','공감','경험','공정평등',
# '믿음신앙','친구우정','성취성공','겸손','논리적임','인정받기','계획과 안정',
# '조화 균형','외모 미모','도전용기','경쟁승부','호기심','자존감','개성 다양성',
# '능력 자신감','가족에 대한 사랑','자유로운 생각','건강','정직','리더십',
# '현실감각','협동 팀워크','부자 재테크','감정 솔직함','성실 부지런함']

# list2 = ['부동산','외국어','주식','외모','게임','과학','친구','연애 사랑'
# ,'영화','미술','음악','만화','스포츠','뉴스','책','정치','경제','경영',
# '자동차','연예인','음식','공예','기계','디자인','관찰','가르치기','글쓰기'
# ,'조언','청소','놀이','가십','여행']

def list1():
    global a
    a=0
    if st.checkbox('연애'):
        a+=1    
    if st.checkbox('좋은 변화'):
        a+=1
    if st.checkbox('창의성'):
        a+=1
    if st.checkbox('배움 성장'):
        a+=1
    if st.checkbox('공감'):
        a+=1
    if st.checkbox('경험'):
        a+=1
    if st.checkbox('공정평등'):
        a+=1
    if st.checkbox('믿음신앙'):
        a+=1
    if st.checkbox('친구우정'):
        a+=1
    if st.checkbox('성취성공'):
        a+=1
    if st.checkbox('겸손'):
        a+=1
    if st.checkbox('논리적임'):
        a+=1
    if st.checkbox('인정받기'):
        a+=1
    if st.checkbox('계획과 안정'):
        a+=1
    if st.checkbox('조화 균형'):
        a+=1
    if st.checkbox('외모 미모'):
        a+=1
    if st.checkbox('도전용기'):
        a+=1
    if st.checkbox('경쟁승부'):
        a+=1
    if st.checkbox('호기심'):
        a+=1
    if st.checkbox('자존감'):
        a+=1
    if st.checkbox('개선 다양성'):
        a+=1
    if st.checkbox('능력 자신감'):
        a+=1
    if st.checkbox('가족에 대한 사랑'):
        a+=1
    if st.checkbox('자유로운 생각'):
        a+=1
    if st.checkbox('건강'):
        a+=1
    if st.checkbox('정직'):
        a+=1
    if st.checkbox('리더십'):
        a+=1
    if st.checkbox('현실감각'):
        a+=1
    if st.checkbox('협동 팀워크'):
        a+=1
    if st.checkbox('부자 재테크'):
        a+=1        
    if st.checkbox('감정 솔직함'):
        a+=1
    if st.checkbox('성실 부지런함'):
        a+=1
    
list1()




if st.button("Confirm"):
    con = st.container()
    con.caption("Result")
    # con.write(f"User Name is {str(input_user_name)}")
    # con.write(str(radio_gender))
    # con.write(f"agree : {check_1}")
    # con.write(f"memo : {str(memo)}")
    if a == 3:
        con.write('다음으로')
    elif a>3:
        b=a-3
        con.write('%d개만큼 더 선택했습니다.'%b)
    else:
        c=3-a
        con.write('%d개만큼 더 선택해주세요'%c)        

	
