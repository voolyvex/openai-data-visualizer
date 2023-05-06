import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from streamlit.runtime.uploaded_file_manager import UploadedFile

import text_to_speech as tts
from explainer import retrieve_data_label, retrieve_data_summary # retrieve_data_insights, retrieve_data_visualization

TTS_ENABLED = True


def display_header() -> None:
    st.image("img/logo.jpg")
    st.title("Welcome to AI Data Visualizer")
    st.text("Just upload your data or copy and paste in the field below")
    st.warning("Warning: uploaded files have precendence on copied and pasted data.")


def display_widgets() -> tuple[UploadedFile, str]:
    file = st.file_uploader("Upload your .csv file here.")
    text = st.text_area("or copy and paste as text here (press Ctrl + Enter to send)")

    if not (text or file):
        st.error("Provide data with one of the options above.")

    return file, text


def retrieve_content_from_file(file: UploadedFile) -> str:
    return file.getvalue().decode("ISO-8859-1")



def extract_code() -> str:
    uploaded_script, pasted_code = display_widgets()

    if uploaded_script:
        return retrieve_content_from_file(uploaded_script)
    return pasted_code or ""


def choose_voice():
    voices = tts.list_available_names()
    return st.selectbox(
        "Please choose one of the available voices.",
        voices,
    )


def main() -> None:
    display_header()

    selected_voice = choose_voice()

    if data_to_explain := extract_code():
        with st.spinner(text="Let me analyze it..."):
            label = retrieve_data_label(code=data_to_explain)
            summary = retrieve_data_summary(code=data_to_explain)
            # insights = retrieve_data_insights(code=data_to_explain)
            # visuals = retrieve_data_visualization(code=data_to_explain)

        with st.spinner(text="Give me a little bit more time, this data is complex..."):
            tts.convert_text_to_mp3(
                message=label, voice_name=selected_voice, mp3_filename="label.mp3"
            )
        with st.spinner(
            text=(
                "I created a label for this data."
                "I'm thinking about how to summarize this in a few words now..."
            )
        ):
            tts.convert_text_to_mp3(
                message=summary,
                voice_name=selected_voice,
                mp3_filename="summary.mp3",
            )

        st.success("Task completed. Here is your summary about the data you provided.")
        st.warning("Remember to turn on your audio!")

        st.markdown(f"**Label:** {label}")
        st.audio("label.mp3")

        st.markdown(f"**Summary:** {summary}")
        st.audio("summary.mp3")

        # st.markdown(f"**Insights:** {insights}")
        # st.audio("insights.mp3")

        # st.markdown(f"**Visualization:** {visuals}")
        
        # st.altair_chart(visuals, use_container_width=False, theme="streamlit")

if __name__ == "__main__":
    main()