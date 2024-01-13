# Researchify
Research smarter, discover faster.

The researchify is designed to streamline and expedite the process of finding research papers. Leveraging the powerful combination of [Streamlit](https://streamlit.io/) and [Xata](https://xata.io/), the application provides users with a user-friendly and efficient platform for accessing academic literature.

### About the dataset

 Arxiv.org AI Research Papers Dataset [↗](https://www.kaggle.com/datasets/yasirabdaali/arxivorg-ai-research-papers-dataset)
 
This dataset is a valuable resource for researchers and practitioners in the field of AI. It can be used to track the latest research trends, identify emerging areas of research, and find relevant papers. This dataset contains the metadata for 10,000 research papers in the field of artificial intelligence (AI) that were published on arXiv.org.

License: [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

### Features

1. **Efficient Search:** Quickly locate relevant research papers based on keywords.

2. **User-Friendly Interface:** Enjoy an intuitive and visually appealing interface, ensuring a seamless user experience.

3. **Xata Database Integration:** Benefit from the reliability of the Xata database for efficient data storage, retrieval, and organization.

4. **Ask AI**:  With the conversational interface, just ask the question related to the database. [Xata's AI](https://xata.io/docs/sdk/ask) has you covered! 

5. **Quick Access to Full Papers:** Efficiently access the full texts of research papers for in-depth exploration.


### Getting Started

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/dotAadarsh/researchify)

Follow these steps to get started with researchify locally:

1. **Clone the Repository:**
   ```git clone https://github.com/dotAadarsh/researchify.git```

2. **Install Dependencies:**
```pip install -r requirements.txt```

3. **Add your Xata credentials:**
Get your API Key and Database URL from Xata and add it the .streamlit/secrets.toml file

4. **Run the App:**
``` streamlit run app.py```

Note 1: If you are running it locally you need to install the streamlit package, which is not included in the requirements.txt file since the app is hosted on the streamlit server, it is not required.

Note 2: If you are running it locally, you need to create a secrets.toml file inside the ./streamlit folder to include your XATA Credentials.

### Resources

- [Xata Documentation](https://xata.io/docs)
- [Import CSV data | Xata](https://xata.io/docs/csv-data/import-data)
- [Xata SDK for Python](https://xata.io/docs/sdk/python/overview)
- [Streamlit Documentation](https://docs.streamlit.io/library/api-reference)
- [Secrets management | Streamlit](https://docs.streamlit.io/library/advanced-features/secrets-management)
