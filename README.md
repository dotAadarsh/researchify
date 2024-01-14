
# Researchify
Research smarter, discover faster.

The researchify is designed to streamline and expedite the process of finding research papers. Leveraging the powerful combination of [Streamlit](https://streamlit.io/) and [Xata](https://xata.io/), the application provides users with a user-friendly and efficient platform for accessing academic literature.

[![Researchify Home](https://github.com/dotAadarsh/researchify/assets/71810927/6de9f65e-0087-45b5-b457-20313c5cdd68)](https://researchify.streamlit.app/)

### Features

1. **Efficient Search:** Quickly locate relevant research papers based on keywords.

2. **User-Friendly Interface:** Enjoy an intuitive and visually appealing interface, ensuring a seamless user experience.

3. **Xata Database Integration:** Benefit from the reliability of the Xata database for efficient data storage, retrieval, and organization.

4. **Ask AI**:  With the conversational interface, ask the question related to the database. [Xata's AI](https://xata.io/docs/sdk/ask) has you covered! 

5. **Quick Access to Full Papers:** Efficiently access the full texts of research papers for in-depth exploration.


### Getting Started

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/dotAadarsh/researchify)

Follow these steps to get started with researchify locally:

1. **Importing the data**: Download the [dataset](https://www.kaggle.com/datasets/yasirabdaali/arxivorg-ai-research-papers-dataset), create a database in Xata and import the CSV file.
 
2. **Clone the Repository:**
   ```git clone https://github.com/dotAadarsh/researchify.git```

3. **Install Dependencies:**
```pip install -r requirements.txt```

4. **Add your Xata credentials:**
Get your API Key and Database URL from Xata and add it to the .streamlit/secrets.toml file

5. **Run the App:**
```streamlit run app.py```

### Dataset

 Arxiv.org AI Research Papers Dataset [↗](https://www.kaggle.com/datasets/yasirabdaali/arxivorg-ai-research-papers-dataset)
 
This dataset is a valuable resource for researchers and practitioners in the field of AI. It can be used to track the latest research trends, identify emerging research areas, and find relevant papers. This dataset contains the metadata for 10,000 research papers in the field of artificial intelligence (AI) that were published on arXiv.org.

License: [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

### Set up - Xata

If you are new to Xata I'd suggest you read [Getting started with Xata | Aadarsh (aadarshkannan.tech)](https://www.aadarshkannan.tech/posts/Getting-Started-With-Xata/). Sign up at [Xata - The serverless database built for modern development](https://xata.io/) and start creating a database and make a note of Xata API and Database URL which we will need later on to connect with our database through Python SDK.

### Import CSV data

Once you create a database you will see import CSV data. Click on that and upload the downloaded dataset. Xata can guess column types from your data automatically, and if needed to change you can choose the dropdown and select the desired type. Once the import is completed, you will be able to see the table.

![xata_researchify_table](https://github.com/dotAadarsh/researchify/assets/71810927/618b53c5-5e8b-4a48-a11c-df3a15736eb0)

![Xata CSV Import](https://github.com/dotAadarsh/researchify/assets/71810927/9647aac8-0ca1-44d3-84a4-ea7c44b8d2d1)

### Search Engine

As you insert data into Xata, it is automatically indexed for full-text search. Try exploring the Search Engine feature which you can find in the left side pane. Try changing various parameters and see what happens. Click on Get the code snippet, select the language Python and copy the code. We will be using this snippet to build the search feature through our app.

![Xata's Search Engine](https://github.com/dotAadarsh/researchify/assets/71810927/90144356-7cd4-4d73-88d4-e1b33957b78e)

### AskAI

Now go to the playground and try out different operations you want to perform through programming. [Xata's `ask` endpoint](https://xata.io/docs/sdk/ask) utilizes current data from your Xata database and leverages Xata's search functionalities to retrieve pertinent information from our database. It then utilizes the OpenAI's ChatGPT API to understand your query and produce natural language responses. Run the following example in the playground and see the result. 

```Python
result = xata.data().ask("Table_name", "Question")
```

![Xata Playground](https://github.com/dotAadarsh/researchify/assets/71810927/8363a43e-6659-4542-af23-3fee3af72ddb)

Here is what the response might looks like: 

![Xata_AI_response](https://github.com/dotAadarsh/researchify/assets/71810927/2f8ac7da-1e2d-4522-a7e9-bfd3bb2ca889)

### User Interface

The Researchify app is built upon Streamlit and Xata's Python SDK. It has two pages, one is for search and other one is for chatbot.

### Resources

- [Xata Documentation](https://xata.io/docs)
- [Import CSV data | Xata](https://xata.io/docs/csv-data/import-data)
- [Xata SDK for Python](https://xata.io/docs/sdk/python/overview)
- [Streamlit Documentation](https://docs.streamlit.io/library/api-reference)
- [Secrets management | Streamlit](https://docs.streamlit.io/library/advanced-features/secrets-management)
