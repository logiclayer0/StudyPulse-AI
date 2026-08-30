import streamlit as st
import os
from dotenv import load_dotenv

from utils.pdf_processor import extract_text_from_pdf
from utils.youtube_processor import get_youtube_transcript
from utils.gemini_engine import generate_study_materials

load_dotenv()

st.set_page_config(
    page_title="StudyPulse AI — Enterprise Workspace", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🎓 StudyPulse AI — Intelligent Learning Workspace")
st.caption("AI-Powered Platform for Automating Study Decks, Quizzes, and Knowledge Maps")
st.divider()

st.header("Step 1: Choose Knowledge Source")

source_type = st.tabs(["📺 YouTube Video", "📄 PDF Document", "📝 Direct Text & Audio"])

raw_content = ""

with source_type[0]:
    st.subheader("Extract Knowledge from YouTube")
    yt_url = st.text_input("Enter YouTube Video Link:", placeholder="https://www.youtube.com/watch?v=...")
    if yt_url:
        if st.button("Extract Transcript", type="secondary"):
            with st.spinner("Processing video captions..."):
                try:
                    raw_content = get_youtube_transcript(yt_url)
                    st.session_state['raw_content'] = raw_content
                    st.success("YouTube Transcript Extracted Successfully!")
                except Exception as e:
                    st.error(f"Error extracting transcript: {e}")

with source_type[1]:
    st.subheader("Extract Knowledge from PDF")
    uploaded_pdf = st.file_uploader("Upload Study Document (PDF)", type=["pdf"])
    if uploaded_pdf:
        if st.button("Parse PDF Content", type="secondary"):
            with st.spinner("Extracting text from PDF pages..."):
                bytes_data = uploaded_pdf.read()
                raw_content = extract_text_from_pdf(bytes_data)
                st.session_state['raw_content'] = raw_content
                st.success("PDF Content Extracted Successfully!")

with source_type[2]:
    st.subheader("Direct Text Input")
    user_text = st.text_area("Paste Lecture Notes / Transcript:", height=180)
    if user_text:
        if st.button("Save Text Input", type="secondary"):
            st.session_state['raw_content'] = user_text
            st.success("Notes Saved Successfully!")

if 'raw_content' in st.session_state and st.session_state['raw_content']:
    st.divider()
    st.header("Step 2: Generate AI Learning Packet")
    
    if st.button("🚀 Generate Comprehensive Study Workspace", type="primary", use_container_width=True):
        with st.spinner("Groq AI is building your quizzes, PYQs, flashcards, and concept summaries..."):
            try:
                data = generate_study_materials(st.session_state['raw_content'])
                st.session_state['study_data'] = data
                st.success("AI Generation Complete!")
            except Exception as e:
                st.error(f"Error in Groq Engine: {e}")

if 'study_data' in st.session_state:
    st.divider()
    st.header("Step 3: Interactive Learning Dashboard")
    
    data = st.session_state['study_data']
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📘 Deep Concept Summary", 
        "⚡ Mind-Blowing Facts", 
        "🎴 Memory Flashcards", 
        "📝 Exam PYQs & Solutions", 
        "🧩 Interactive Quiz Engine"
    ])
    
    with tab1:
        st.markdown("### Core Conceptual Overview")
        st.write(data.get("summary", ""))

    with tab2:
        st.markdown("### Key Real-World Insights & Facts")
        for fact in data.get("fun_facts", []):
            st.info(f"• {fact}")

    with tab3:
        st.markdown("### Active Recall Flashcards")
        for idx, card in enumerate(data.get("flashcards", [])):
            with st.expander(f"Flashcard {idx+1}: {card.get('question', '')}"):
                st.write(card.get('answer', ''))

    with tab4:
        st.markdown("### Previous Year Exam Questions (PYQs)")
        for idx, pyq in enumerate(data.get("pyqs", [])):
            st.markdown(f"#### Question {idx+1}: {pyq.get('question', '')}")
            st.markdown(f"**Detailed Solution:** {pyq.get('answer', '')}")
            st.divider()

    with tab5:
        st.markdown("### Test Your Understanding")
        quizzes = data.get("quizzes", [])
        for q_idx, q in enumerate(quizzes):
            st.markdown(f"**Question {q_idx+1}: {q.get('question', '')}**")
            selected = st.radio(
                f"Select option for Question {q_idx+1}",
                q.get("options", []),
                key=f"quiz_opt_{q_idx}"
            )
            if st.button(f"Submit Choice Q{q_idx+1}", key=f"btn_quiz_{q_idx}"):
                correct_idx = q.get("correct_option_index", 0)
                options = q.get("options", [])
                if options and selected == options[correct_idx]:
                    st.success("✨ Correct Answer!")
                else:
                    st.error(f"❌ Incorrect. Correct choice: {options[correct_idx] if options else ''}")
                st.info(f"**Explanation:** {q.get('explanation', '')}")
            st.divider()