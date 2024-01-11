import re
import streamlit as st
import json
from datetime import datetime
from xata.client import XataClient

XATA_API_KEY=st.secrets["XATA_API_KEY"]
XATA_DB_URL=st.secrets["XATA_DB_URL"]

xata = XataClient(api_key=XATA_API_KEY, db_url=XATA_DB_URL)

st.set_page_config(
    page_title="Researchify",
    page_icon="🦋",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "### Search the Arxiv.org AI Research Papers with ease!"
    }
)

with st.sidebar:
    with st.expander("About the dataset", expanded=True):
        st.subheader("Arxiv.org AI Research Papers Dataset [↗](https://www.kaggle.com/datasets/yasirabdaali/arxivorg-ai-research-papers-dataset)")
        st.markdown("This dataset is a valuable resource for researchers and practitioners in the field of AI. It can be used to track the latest research trends, identify emerging areas of research, and find relevant papers. This dataset contains the metadata for 10,000 research papers in the field of artificial intelligence (AI) that were published on arXiv.org.")
        st.markdown("License: [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)")
    
def datetime_format(dateTime):

    # Parse the timestamp string
    timestamp = datetime.strptime(dateTime, "%Y-%m-%dT%H:%M:%SZ")

    # Format the timestamp
    formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_timestamp

def redact(text):
    # Define the pattern to match the text tag
    pattern = r"(?i)<em>(.*?)</em>"

    # Replace the tag with the desired format
    replaced_text = re.sub(pattern, r":violet[\1]", text)

    return replaced_text

def display(data):

    # Access totalCount
    total_count = data.get("totalCount", 0)
    st.toast(f"Results found: {total_count}")

    # Iterate through records and display title and summary from xata
    for record in data['records']:
        xata_info = record.get('xata', {})  # Retrieve xata field, default to empty dictionary if not present
        highlight_info = xata_info.get('highlight', {})
        
        if 'title' in highlight_info:
            highlighted_title = f"{', '.join(highlight_info['title'])}"
            redacted_highlighted_title = redact(highlighted_title)
            st.subheader(redacted_highlighted_title)
            
        else:
            st.subheader(record['title'])
        
        timestamp_str = record['published']
        
        if timestamp_str is not None:
            
            formatted_timestamp = datetime_format(timestamp_str)
            st.caption(f"{formatted_timestamp} | {record['primary_category']}")
        
        if 'summary' in highlight_info:
            highlighted_summary = f"**Highlighted Summary:** {', '.join(highlight_info['summary'])}"
            redacted_highlighted_summary = redact(highlighted_summary)
            st.write(redacted_highlighted_summary)
        else:
            st.write(f"Summary: {record['summary']}")

        st.link_button("PDF ↗", record["pdf_url"])

        st.write("---")

@st.cache_data
def paper_search(query, fuzziness):
    
    data = xata.data().search_table("arxiv_ai", {
        "query": f"{query}",
        "fuzziness": fuzziness,
        "prefix": "phrase"
    })


    return data

def main():
    
    st.title("Researchify")
    st.subheader("Research smarter, discover faster.")
    st.caption("powered by Xata")
    
    col1, col2 = st.columns([2, 1])
    with col1: 
        # Get user input
        text_input = st.text_input("Enter your search query 👇")

    with col2: 
        fuzziness = st.slider("Fuzziness", 0, 2, 1, help="0: no typo tolerance 1: one letter changed/added/removed (default) 2: two letters changed/added/removed")

    if text_input is not None and fuzziness is not None:
        response = paper_search(text_input, fuzziness)
        if response is not None:
            display(response)

if __name__ == "__main__":
    main()
