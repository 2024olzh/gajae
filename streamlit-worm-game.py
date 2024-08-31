import streamlit as st
import pandas as pd
import numpy as np
import time

# 게임 상태를 저장할 세션 상태 변수들
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'worm' not in st.session_state:
    st.session_state.worm = {
        'x': 400,
        'y': 300,
        'radius': 15,
        'thickness': 1,
        'speed': 3,
        'length': 20,
        'segments': []
    }
if 'foods' not in st.session_state:
    st.session_state.foods = []
if 'game_started' not in st.session_state:
    st.session_state.game_started = False

# 음식 타입 정의
food_types = {
    'grains': ['🍚', '🍜', '🍝', '🍞', '🥐', '🥖', '🥨', '🥯', '🥞', '🧇', '🌽', '🌾', '🥔', '🍠'],
    'proteins': ['🥩', '🍗', '🍖', '🍤', '🍳', '🥚', '🧀', '🥜', '🫘', '🍣', '🐟', '🦐', '🦀', '🦞'],
    'veggiesFruits': ['🥦', '🥬', '🥒', '🍅', '🍆', '🥕', '🌶️', '🫑', '🥔', '🍠', '🍎', '🍐', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓', '🫐', '🍑', '🍍'],
    'dairy': ['🥛', '🧃', '🥤']
}

def create_food():
    food_type = np.random.choice(list(food_types.keys()))
    return {
        'x': np.random.randint(20, 780),
        'y': np.random.randint(20, 580),
        'type': food_type,