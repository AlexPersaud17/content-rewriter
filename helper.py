import streamlit as st
from prompt_generators import generate_sample_data_user_message
from writerai import Writer
from palmyra import palmyra_query
from dotenv import load_dotenv
load_dotenv()

client = Writer()
PALMYRA_OMNI = "palmyra-x-004"


def create_sample_data():
    user_message = generate_sample_data_user_message(
        st.session_state.get("selected_domain", "Creative"))
    system_message = f"""
    You are a professional content strategist helping developers test rewriting tools.
    You create realistic, fictional content samples tailored to specific industries.
    Your goal is to write authentic user-submitted input text that feels natural and professional for that field.

    Sample content:
    """
    with st.spinner("Generating example input..."):
        response = palmyra_query(system_message, user_message, PALMYRA_OMNI)
    st.session_state.generated_input = response.choices[0].message.content
    st.rerun()
