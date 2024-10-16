# 📊 WhatsApp Chat Analyzer

Welcome to the **WhatsApp Chat Analyzer**! This project is a Streamlit-based web application designed to help you analyze your WhatsApp chat exports. By leveraging **Natural Language Processing (NLP)** techniques, this app provides insights into your conversations, such as message frequency, most active participants, emoji usage, and more!

## 🚀 Features

- **Upload and Analyze**: Upload your WhatsApp chat export file (`.txt`) and analyze its content.
- **Message Statistics**: Get statistics such as total messages, number of participants, and the most active participants.
- **Word Cloud**: Visualize the most frequently used words in the chat using a word cloud.
- **Emoji Analysis**: Analyze which emojis were used the most during the conversation.
- **Activity Timeline**: See when the chat is most active (daily, weekly, or monthly).
- **Sentiment Analysis**: Analyze the sentiment (positive, negative, neutral) of the messages using NLP.
- **Top Words & Messages**: Discover the most commonly used words and messages by participants.

## 📦 Tech Stack

| Component              | Technology/Tool          |
|------------------------|--------------------------|
| **Frontend/UI**         | Streamlit                |
| **Backend**             | Python                   |
| **NLP & Analysis**      | NLTK, Pandas, Matplotlib  |
| **Visualization**       | Matplotlib, Seaborn, Wordcloud |
| **Deployment**          | Streamlit Cloud           |

## 🛠️ Setup and Installation

### Prerequisites
- Python 3.x installed on your local machine.

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SartHak-0-Sach/WhatsApp_chat_analyzer_NLP_project.git
   cd WhatsApp_chat_analyzer_NLP_project
   ```

2. **Install dependencies**:
   Use the following command to install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Upload WhatsApp chat file**:
   - Export your WhatsApp chat as a `.txt` file from the WhatsApp app.
   - Upload the file into the application and start analyzing!

## 📊 How It Works

1. **Chat File Upload**: Upload your WhatsApp `.txt` export file.
2. **Data Preprocessing**: The app parses and processes the chat text to extract key information such as timestamps, participant names, and messages.
3. **Analysis**:
   - **Message Counts**: Shows how many messages each participant sent.
   - **Word Cloud**: A graphical representation of the most common words.
   - **Emoji Usage**: Displays the most used emojis in the conversation.
   - **Activity Timeline**: Visualizes activity over time.
   - **Sentiment Analysis**: Categorizes the overall sentiment of the conversation.

## 📝 Example Usage

1. Export your WhatsApp chat from the app.
2. Run the Streamlit app locally.
3. Upload your `.txt` chat export file.
4. View the detailed analytics of your chat, including activity, sentiment, and message breakdowns.

## 🌟 Contributing

Feel free to open issues or pull requests if you find bugs or want to enhance the app. Contributions are welcome!

## 👨‍💻 Author

**Sarthak Sachdev**

- GitHub: [@Sarthak-0-Sach](https://github.com/Sarthak-0-Sach)
- LinkedIn: [Sarthak Sachdev](https://www.linkedin.com/in/sarthak2004/)
- Twitter: [@sarthak_sach69](https://twitter.com/sarthak_sach69)

## 🙌 Acknowledgments

- Special thanks to CampusX youtube channel for guidance and programming support.

### Happy Coding!!😇✌🏻
