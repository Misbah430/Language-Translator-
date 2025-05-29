# E:\Minicinda\conda\LanguageTranslator\LANGUAGETRANSLATOR
import streamlit as st
from googletrans import Translator, LANGUAGES

translator = Translator()
st.set_page_config(page_title="Language Translator", layout="centered")
st.title("🌐 Language Translator")

text = st.text_area("Enter text to translate:", height=100)
languages = dict(sorted(LANGUAGES.items(), key=lambda x: x[1].capitalize()))
targets = st.multiselect(
    label="Select target language(s)",
    options=list(languages.values()),
    default=["english"]
)

if st.button("Translate"):
    if not text:
        st.warning("Please enter some text to translate.")
    else:
        st.subheader("Translations:")
        for lang in targets:
           
            lang_code = [code for code, name in languages.items() if name == lang][0]
            result = translator.translate(text, dest=lang_code)
            st.markdown(f"**{lang.capitalize()}:** {result.text}")



