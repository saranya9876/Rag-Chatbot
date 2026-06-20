from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

SYSTEM_PROMPT = """
You are a strict RAG assistant.

RULES:
- Use ONLY given context
- If not found, say "I don't know based on documents"
- Be short and precise (max 120 words)
- Do not hallucinate
- Use bullet points if needed
"""

def generate_answer(query, docs):
    context = "\n\n".join(
        [f"SECTION {i + 1}:\n{doc.page_content}" for i, doc in enumerate(docs)]

    )

    try:
        response = client.chat.completions.create(
            model="phi-3",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"""
Context:
{context}

Question:
{query}

Answer strictly:
"""
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"ERROR: {str(e)}"