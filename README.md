# RAG-Model_Website

A user-friendly interface to use Retrieval-Augmented Generation (RAG) with LangChain. This application allows users to upload PDF documents and query them using an intuitive interface, leveraging the power of the OpenAI API for efficient information retrieval.

## Features

- **Document Upload**: Upload PDFs to be processed by the RAG model.
- **Query Interface**: Easily query your uploaded documents from a dedicated query page.
- **Built with LangChain**: Uses LangChain for seamless integration of retrieval-augmented generation.
- **API Integration**: Supports integration with OpenAI API for enhanced query capabilities.

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/Mochoye/RAG-Model_Website
   ```

2. **Navigate to the folder:**

   ```bash
   cd RAG-Model_Website
   ```

3. **Create a virtual environment:**

   ```bash
   conda create --name venv python=3.11.3
   ```

4. **Activate the environment:**

   ```bash
   conda activate venv
   ```

5. **Set your API key:**

   Replace `"your-api-key"` with your actual OpenAI API key.

   ```bash
   setx OPENAI_API_KEY "your-api-key"
   ```

6. **Install necessary dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

Sure, here’s the README from the **Usage** section onward:

```markdown
## Usage

1. **Run the Application**:

   Start the application by running the following command:

   ```bash
   python app.py
   ```

2. **Upload PDFs**:

   - Open your browser and navigate to the upload page.
   - Use the interface to upload the PDF files you wish to query.
   - If the upload process seems slow or gets stuck, restart the server by pressing `CTRL + C` in the terminal and running `python app.py` again.

3. **Query PDFs**:

   - After uploading, navigate to the query page.
   - Enter your query, and the app will use the RAG model to fetch relevant information from your documents.
   - Results will display in the interface, allowing for quick and effective document search.

## Troubleshooting

- **App Stuck on Upload/Query**: Restart the server with `CTRL + C` and rerun `python app.py`.
- **API Key Issues**: Ensure your API key is set correctly. Run `setx OPENAI_API_KEY "your-api-key"` if needed.

---

Enjoy your enhanced document search experience with RAG-Model_Website!
```
