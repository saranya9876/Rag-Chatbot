import streamlit as st
from retriever import retrieve
from generator import generate_answer

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title(" RAG Chatbot (PDF Knowledge Assistant)")

# ---------------------------
# Session memory (chat history)
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# Display chat history
# ---------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------
# Input box
# ---------------------------
query = st.chat_input("Ask something from your documents...")

if query:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Retrieve documents
    with st.spinner("🔍 Retrieving relevant chunks..."):
        docs = retrieve(query)

    # Generate answer
    with st.spinner("🤖 Generating answer..."):
        answer = generate_answer(query, docs)

    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Optional debug (REMOVE later if needed)
    with st.expander("📚 Retrieved Chunks"):
        for i, d in enumerate(docs):
            st.markdown(f"**Chunk {i+1}:**")
            st.write(d.page_content[:500])
            st.caption(d.metadata)