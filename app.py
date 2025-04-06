import streamlit as st
from writerai import Writer
from config_setup import config_sidebar, load_config
from prompt_generators import generate_rewriter_user_message, generate_rewriter_system_message
from palmyra import palmyra_query, stream_output

PALMYRA_CREATIVE = "palmyra-creative"
PALMYRA_MED = "palmyra-med"
PALMYRA_FIN = "palmyra-fin"
PALMYRA_OMNI = "palmyra-x-004"

st.set_page_config(page_title="Content Rewriter", layout="wide")
st.title("Content Rewriter")


def rewrite_content(text, config, palmyra_model):
    user_message = generate_rewriter_user_message(text, config)
    system_message = generate_rewriter_system_message(palmyra_model)
    response = palmyra_query(system_message, user_message, palmyra_model, True)
    stream_output(response)


def app():
    config_file, input_text, domain = config_sidebar()
    palmyra_model = PALMYRA_CREATIVE
    if domain == "Creative":
        palmyra_model = PALMYRA_CREATIVE
    elif domain == "Medical":
        palmyra_model = PALMYRA_MED
    elif domain == "Finance":
        palmyra_model = PALMYRA_FIN
    elif domain == "Omni":
        palmyra_model = PALMYRA_OMNI

    if st.session_state.submitted and input_text:
        config_json = load_config(config_file)
        st.divider()
        st.subheader("Rewritten Content")
        rewrite_content(input_text, config_json, palmyra_model)
        st.divider()
        st.subheader("Original Content")
        st.write(input_text)
    else:
        st.info(
            "Add some content to get started.")

    st.session_state.submitted = False


if __name__ == "__main__":
    app()
