# YouTube AI Responder

The **YouTube AI Responder** is a Streamlit-based application that uses an open-source language model to generate thoughtful responses to YouTube comments. It leverages the Hugging Face `transformers` library and a pre-trained model (e.g., GPT-2) to provide AI-generated replies without requiring any API keys.

---

## Features

- **AI-Powered Responses**: Generates thoughtful and context-aware replies to YouTube comments.
- **Open-Source Model**: Uses free, open-source models like GPT-2 for text generation.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive experience.
- **Dataset Preview**: Displays a preview of the YouTube comments dataset in the sidebar.

---

## Installation

Follow these steps to set up and run the YouTube AI Responder on your local machine.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MAITREED03/YOUTUBE_AI_RESPONDER
   cd youtube-ai-responder

   Create a Virtual Environment

   python -m venv venv
source venv/bin/activate  # On Windows:

Install Dependencies:
Install the required Python packages using the following command:

pip install -r requirements.txt

Download the Dataset:
Place your YouTube comments dataset (YoutubeCommentsDataSet.csv) in the project directory. Ensure the file is named correctly and contains a column with comments.

Usage
Run the Application:
Start the Streamlit app by running the following command:
streamlit run main.py

Interact with the App:

The app will open in your default web browser.

Enter a YouTube comment in the text area and click Generate Response.

The AI will generate a thoughtful reply to the comment.

Dataset Preview:

The sidebar displays a preview of the first 10 rows of the dataset for reference.

Customization
Model Selection:
You can switch to a different open-source model by modifying the load_model function in main.py. For example:

Contributing
Contributions are welcome! If you'd like to improve this project, please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Commit your changes and push them to your fork.

Submit a pull request with a detailed description of your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Hugging Face for providing the transformers library and open-source models.

Streamlit for the easy-to-use web app framework.

The open-source community for their contributions to AI and machine learning.

Contact
For questions or feedback, feel free to reach out:

Your Name: maitreede330@gmail.com

GitHub: MAITREED03