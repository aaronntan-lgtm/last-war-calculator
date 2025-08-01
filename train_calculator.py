
import streamlit as st

def render_train_calculator():
    st.set_page_config(page_title="Best Train Cabin Calculator")

    st.markdown("""
        <style>
        div[data-testid="stSelectbox"][id^="language_selector"] > div {
            border: 1px solid #28a745 !important;
            box-shadow: 0 0 0 1px #28a745 !important;
        }
        div[data-testid="stSelectbox"][id^="language_selector"] > div:focus,
        div[data-testid="stSelectbox"][id^="language_selector"] > div:focus-within {
            border: 1px solid #28a745 !important;
            box-shadow: 0 0 0 1px #28a745 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    languages = {
        "English": "en",
        "Tiếng Việt": "vi",
        "繁體中文": "zh"
    }

    lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言",
                               list(languages.keys()), key="language_selector")
    lang = languages[lang_choice]

    text = {
        "title": {
            "en": "🚂 Best Train Cabin Calculator",
            "vi": "🚂 Công Cụ Chọn Toa Tàu Tốt Nhất",
            "zh": "🚂 最佳車廂選擇器"
        },
        "intro": {
            "en": "Select your best cabin based on current queue sizes...",
            "vi": "Chọn khoang tốt nhất dựa trên số người xếp hàng hiện tại...",
            "zh": "根據目前排隊人數選擇最佳車廂..."
        },
        "ev_description": {
            "en": "**What is EV?** Expected Value (EV) estimates your average gain over time...",
            "vi": "**EV là gì?** Giá trị kỳ vọng (EV) ước tính mức lợi trung bình của bạn...",
            "zh": "**什麼是 EV？** 期望值 (EV) 表示你長期平均能獲得的收益..."
        },
        "input_header": {
            "en": "📥 Input Queue Sizes for Each Cabin",
            "vi": "📥 Nhập số người đang xếp hàng tại mỗi khoang",
            "zh": "📥 輸入每個車廂的排隊人數"
        },
        "input_label": {
            "en": "{name} (Enter the number of passengers in the queue here)",
            "vi": "{name} (Nhập số người xếp hàng tại đây)",
            "zh": "{name}（請輸入排隊人數）"
        },
        "ranking_header": {
            "en": "📊 Cabin Rankings by EV",
            "vi": "📊 Xếp hạng các khoang theo EV",
            "zh": "📊 根據 EV 排名的車廂"
        },
        "no_input_msg": {
            "en": "(Please input number of passengers in queue)",
            "vi": "(Vui lòng nhập số người xếp hàng)",
            "zh": "（請輸入排隊人數）"
        },
        "full_entry_msg": {
            "en": "100% chance of entry",
            "vi": "100% được vào",
            "zh": "100% 可進入"
        }
    }

    cabin_names = {
        'A': 'First Cabin',
        'B': 'Second Cabin',
        'C': 'Third Cabin',
        'D': 'Fourth Cabin'
    }

    st.title(text["title"][lang])
    st.markdown(text["intro"][lang])

    st.subheader(text["input_header"][lang])
    queue_a = st.number_input(text["input_label"][lang].format(name=cabin_names['A']), min_value=0, value=0)
    queue_b = st.number_input(text["input_label"][lang].format(name=cabin_names['B']), min_value=0, value=0)
    queue_c = st.number_input(text["input_label"][lang].format(name=cabin_names['C']), min_value=0, value=0)
    queue_d = st.number_input(text["input_label"][lang].format(name=cabin_names['D']), min_value=0, value=0)

    cabins = {
        'A': {'queue': queue_a, 'value': 2},
        'B': {'queue': queue_b, 'value': 1},
        'C': {'queue': queue_c, 'value': 1},
        'D': {'queue': queue_d, 'value': 4}
    }

    def calculate_ev(queue_size, cabin_value):
        if queue_size == 0:
            return float('inf')
        return (5 / queue_size) * cabin_value

    ev_list = []
    for name, data in cabins.items():
        ev = calculate_ev(data['queue'], data['value'])
        cabins[name]['ev'] = ev
        ev_list.append((name, ev))

    ev_list.sort(key=lambda x: -x[1])

    st.subheader(text["ranking_header"][lang])
    for rank, (name, ev) in enumerate(ev_list, start=1):
        label = cabin_names.get(name, f"Cabin {name}")
        queue = cabins[name]['queue']
        if queue == 0:
            st.markdown(f"**{rank}. {label} — {text['no_input_msg'][lang]}**")
        elif ev == float('inf'):
            st.markdown(f"**{rank}. {label} — {text['full_entry_msg'][lang]}**")
        else:
            st.markdown(f"**{rank}. {label} — EV = {ev:.2f}**")

    st.markdown("---")
    st.markdown(text["ev_description"][lang])
