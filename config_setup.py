import streamlit as st
import json
from helper import create_sample_data


def config_sidebar():
    st.sidebar.header("1. Upload Content Settings")
    config_file = st.sidebar.file_uploader("Upload JSON config", type=["json"])

    st.sidebar.header("2. Input Content")
    input_text = st.sidebar.text_area(
        "Paste your content here",
        value=st.session_state.get("generated_input", ""),
        height=200
    )

    st.sidebar.header("3. Select Domain or Industry Focus")
    domain = st.sidebar.radio(
        label="3. Select Domain or Industry Focus",
        options=["Creative", "Medical", "Finance", "Omni"],
        index=None,
        horizontal=True,
        label_visibility="collapsed"
    )
    st.session_state.selected_domain = domain

    if st.sidebar.button("Generate Example Text"):
        create_sample_data()

    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    if st.sidebar.button("Submit"):
        if not input_text:
            st.sidebar.warning("Please enter some content before submitting.")
        else:
            st.session_state.submitted = True

    return config_file, input_text, domain


def load_config(file):
    if not file:
        return {}
    return json.load(file)
