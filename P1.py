import customtkinter as ctk
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment():
    # Get the input from the text box
    user_input = text_input.get("1.0", "end-1c")
    
    # Analyze sentiment using TextBlob
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity
    scaled_polarity = int((polarity+1)*50)
    
    # Determine the sentiment
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    # Update the result label
    sentiment_label.configure(text=f"Sentiment: {sentiment}")
    polarity_label.configure(text=f"Polarity Score: {scaled_polarity}/100")

# Initialize customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Create the main window
root = ctk.CTk()
root.title("Sentiment Analysis Tool")
root.geometry("400x300")

# Create and place widgets
title_label = ctk.CTkLabel(root, text="Sentiment Analysis Tool", font=("Arial", 20))
title_label.pack(pady=10)

text_input = ctk.CTkTextbox(root, height=100, width=300)
text_input.pack(pady=10)

analyze_button = ctk.CTkButton(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack(pady=10)

sentiment_label = ctk.CTkLabel(root, text="Sentiment: ", font=("Arial", 15))
sentiment_label.pack(pady=5)

polarity_label = ctk.CTkLabel(root, text="Polarity Score: ", font=("Arial", 15))
polarity_label.pack(pady=5)

# Run the main loop
root.mainloop()