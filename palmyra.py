from writerai import Writer
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

client = Writer()
PALMYRA_CREATIVE = "palmyra-creative"
PALMYRA_MED = "palmyra-med"
PALMYRA_FIN = "palmyra-fin"
PALMYRA_OMNI = "palmyra-x-004"


def palmyra_query(system_message, user_message, model, stream=False):
    response = client.chat.chat(
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        model=model,
        stream=stream
    )
    return response


def stream_output(response):
    streamed_output = ""
    placeholder = st.empty()
    for chunk in response:
        if chunk.choices[0].delta.content:
            streamed_output += chunk.choices[0].delta.content
            placeholder.markdown(streamed_output)
