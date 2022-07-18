import streamlit as st

st.set_page_config("3v3ryday p3opl3 translator",layout="wide")

main_title = st.title('3V3RYDAYP3OPL3 TRANSLATOR')

txt_input = st.text_area(label="Text Input", placeholder="Input text here")

select_caps = caps_lock = st.checkbox('Caps')


def Translator():
    if select_caps:
        lowercase_text = txt_input.replace("e", "3")
        uppercase_text = lowercase_text.upper()
        st.text_area(label="T3xt Output", value=uppercase_text)

    else:
        translated_text = txt_input.replace("e", "3")
        st.text_area(label="T3xt Output", value=translated_text)


Translator()

translate_button = st.button("Translat3")

about_txt = st.markdown("<label style='margin:69x; text-align:center; color: white'>This website is fan-made, "
                        "I'm not associated with Hangout Dao in any way, shape or form. Project created by ["
                        "aqthewitcher](https://twitter.com/aqthewitcher)</label>", unsafe_allow_html=True)
