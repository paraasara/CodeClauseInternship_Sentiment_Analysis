# Sentiment Analysis Tool

## Problem Statement
The goal of this project is to develop a **Sentiment Analysis Tool** that can determine the sentiment (Positive, Negative, or Neutral) of user-provided text. This tool leverages the power of **TextBlob** for sentiment analysis and provides a graphical user interface (GUI) using **customtkinter**. The sentiment score is scaled between 0 and 100, making it intuitive for users to understand how positive or negative a given text is.

## Features
- **Sentiment Analysis**: Classifies text as Positive, Negative, or Neutral.
- **Polarity Score**: Displays a polarity score on a scale from 0 to 100 for easier interpretation of sentiment strength.
- **User-Friendly GUI**: Built using `customtkinter` for a modern and clean interface.
- **Real-time Input**: Users can input sentences, reviews, or any form of text and receive instant feedback.

## Challenges
During the development of this project, the following challenges were encountered:
1. **Polarity Score Scaling**: The raw polarity score returned by TextBlob ranges from -1 to 1, which can be less intuitive for users. This project overcame the challenge by scaling the score to a more user-friendly range of 0 to 100, where:
   - 0 indicates a highly negative sentiment.
   - 100 indicates a highly positive sentiment.
   - 50 represents a neutral sentiment.
   
2. **GUI Design**: Designing a modern, easy-to-use GUI required careful use of `customtkinter`, ensuring the interface was not only functional but also visually appealing.

3. **Efficient Text Processing**: Analyzing real-time user input efficiently while maintaining accuracy in sentiment classification was another key focus of this project. Using a lightweight library like **TextBlob** helped streamline the process.

## Uses of the Tool
This tool can be used in various real-world applications, including:
- **Customer Feedback Analysis**: Analyzing customer reviews or feedback for businesses to understand customer satisfaction.
- **Social Media Monitoring**: Evaluating the sentiment of social media posts to track public opinion on brands, products, or services.
- **Market Research**: Understanding the general sentiment around a particular product or topic from survey responses or comments.
- **Content Moderation**: Automatically detecting negative or inappropriate comments in online communities.

## Installation and Usage
### Requirements:
- **Python 3.x**
- `TextBlob` library
- `customtkinter` library

### Setup Instructions:
1. Clone the repository.

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the project:
   ```bash
   python sentiment_analysis_gui.py
   ```

4. Enter a sentence or review in the text box, click **"Analyze Sentiment"**, and view the results.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
