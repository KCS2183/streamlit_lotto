import streamlit as st
import random
from datetime import datetime

st.title('로또 번호')

st.header('로또 번호를 생성합니다.')

def genlotto():
    lotto = set()
    while len(lotto) < 6:
        number = random.randint(1, 45)
        lotto.add(number)
    return tuple(lotto)


button = st.button('생성하기')
reset = st.button('Reset')

if button:
    # 랜덤 숫자 6개를 5개의 리스트에 담는다.
    for i in range(1, 6):
        numbers = sorted(genlotto())
        st.subheader(f':material/Settings: 번호 {i}: :orange[{numbers}]')
        
    # 시간
    st.write('시간: ', datetime.now().strftime('%Y-%m-%d %H:%M'))

if reset:
    st.rerun()