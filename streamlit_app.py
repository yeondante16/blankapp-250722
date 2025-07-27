import streamlit as st
import random
import numpy as np

st.set_page_config(page_title="주사위 실험기", layout="centered")
st.title("🎲 주사위 실험기")

# 1. 주사위 개수 슬라이더
dice_count = st.slider("굴릴 주사위 개수 선택 (1 ~ 200)", min_value=1, max_value=200, value=10)

# 2. 주사위 굴리기 버튼
if st.button("주사위 굴리기 🎲"):
    results = [random.randint(1, 6) for _ in range(dice_count)]
    average = np.mean(results)

    st.success(f"🎯 주사위 평균값: **{average:.2f}**")
    
    # 각 눈금별 빈도수 시각화 (1~6)
    counts = np.bincount(results, minlength=7)[1:]  # 인덱스 1~6
    st.bar_chart(counts)
