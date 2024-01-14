from xata.client import XataClient
import streamlit as st
import json

# Retrieve API key and database URL from Streamlit secrets
XATA_API_KEY = st.secrets["XATA_API_KEY"]
XATA_DB_URL = st.secrets["XATA_DB_URL"]

# Initialize XataClient with API key and database URL
xata = XataClient(api_key=XATA_API_KEY, db_url=XATA_DB_URL)

# Streamlit page configuration
st.set_page_config(
    page_title="RAI - Researchify AI Assistant",
    page_icon="🦋",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://github.com/dotAadarsh/researchify',
        'Report a bug': "https://github.com/dotAadarsh/researchify",
        'About': "### Search the Arxiv.org AI Research Papers with ease!"
    }
)

# Function to follow up on a user's prompt in a session
def follow_up(prompt, session_id):
    result = xata.data().ask_follow_up("Tutorial", f"{prompt}", session_id)
    return result["answer"], result["sessionId"]

# Function to get a response from Xata AI based on user's prompt
def get_xata_ai(prompt):
    result = xata.data().ask(
        "arxiv_ai",   # reference table
        f"{prompt}",  # question to ask
        [
            "If asked about a question outside of the context, respond with 'It doesn't look like I have enough information to answer that. Sorry!",
            "Use 'RAI' as the name in all interactions to maintain a consistent identity.",
            "If asked for research papers, share the relevant pdf url's from the pdf_url column",
            "If uncertain about an answer, express the lack of information and suggest referring to online search",
            "Acknowledge user queries promptly and strive to provide accurate and helpful information within the defined context."
        ],
        options={
            "searchType": "keyword",
            "search": {
                "fuzziness": 2,
                "prefix": "phrase"
            }
        }
    )                   
    return result

# Function to handle the chat interface
def chat():
    session_count = 0

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        if session_count == 0:
            AIreponse = get_xata_ai(prompt)
            answer = AIreponse["answer"]
            session_id = AIreponse["sessionId"]
            record_ids = AIreponse.get("records", [])

            session_count += 1

        elif session_count > 0 and session_count < 2:

            AIreponse = follow_up(prompt, session_id)
            answer = AIreponse["answer"]
            session_id = AIreponse["sessionId"]
            record_ids = AIreponse.get("records", [])

        else:
            answer = "Max Session reached!"

        # Display assistant response in chat message container
        with st.chat_message("assistant", avatar="https://github.com/dotAadarsh/researchify/blob/main/xatafly-removebg-preview.png?raw=true"):
            st.markdown(answer)
            for i in record_ids:
                record_data = xata.records().get("arxiv_ai", i)
                st.link_button(record_data["title"], record_data["pdf_url"])

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": answer})
        

# Main function
def main():
    # Streamlit app
    st.title("ResearchifyAI")
    st.caption("Your AI research assistant!")
    st.write("---")
    chat()

# Run the main function
if __name__ == "__main__":
    main()
