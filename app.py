
import streamlit as st
from gemma import ask_gemma

st.set_page_config(
    page_title="Gemma 4 Hackathon",
    page_icon="🤖"
)

st.title("Gemma 4 AI Assistant")
st.write("Ask a question or upload an image!")

question = st.text_area("What do you want to know?")

image = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if image:
    st.image(image, caption="Uploaded image")

if st.button("Ask Gemma"):
    if not question and not image:
        st.warning("Enter a question or upload an image.")
    else:
        with st.spinner("Gemma is thinking..."):
            try:
                answer = ask_gemma(
                    question or "Describe this image.",
                    image.getvalue() if image else None,
                    image.type if image else None
                )
                st.write(answer)
            except Exception as error:
                st.error(f"Something went wrong: {error}")

