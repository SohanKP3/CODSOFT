# Importing necessary libraries for processing, modeling, and displaying output
import numpy as np                   # For numerical operations
import pandas as pd                 # For structured data presentation
import matplotlib.pyplot as plt     # For image visualization
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dense, Dropout
import os
import glob

# Load the ResNet50 model pre-trained on ImageNet and remove the final classification layer
cnn_model = ResNet50(weights='imagenet')                              # Load pre-trained ResNet50
cnn_model = Model(inputs=cnn_model.input, outputs=cnn_model.layers[-2].output)  # Remove last layer for feature extraction

# Define a function to extract features from an image
def extract_image_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))           # Load and resize image
    img_array = image.img_to_array(img)                              # Convert image to array
    img_array = np.expand_dims(img_array, axis=0)                    # Add batch dimension
    img_array = preprocess_input(img_array)                          # Preprocess image for ResNet
    features = cnn_model.predict(img_array)                          # Extract features using ResNet
    return features                                                  # Return extracted feature vector

# Sample captioning corpus and tokenizer for demo purposes
captions = {
    "dog.jpg": "a dog running through a field",
    "car.jpg": "a red car parked by the road"
}

# Prepare tokenizer and sequences
tokenizer = Tokenizer()                                              # Initialize tokenizer
tokenizer.fit_on_texts(captions.values())                            # Fit tokenizer on captions
vocab_size = len(tokenizer.word_index) + 1                           # Vocabulary size (+1 for padding)
max_length = max(len(c.split()) for c in captions.values())          # Maximum caption length

# Build a simple caption generator model (CNN+RNN architecture)
def create_caption_model():
    model = Sequential()                                             # Sequential model container
    model.add(Embedding(input_dim=vocab_size, output_dim=50))       # Word embedding layer
    model.add(LSTM(256, return_sequences=False))                     # LSTM for sequential captioning
    model.add(Dropout(0.5))                                          # Dropout for regularization
    model.add(Dense(vocab_size, activation='softmax'))              # Output layer for word prediction
    model.compile(loss='categorical_crossentropy', optimizer='adam') # Compile the model
    return model

caption_model = create_caption_model()  # Create the captioning model

# Simulated function to generate a caption from features (actual generation needs training)
def generate_caption(features):
    # Just returning sample captions for illustration; this part would normally involve beam search or greedy decoding
    return "a simulated caption of the image"

# Visualize image with generated caption and tabular output
def display_caption(img_path):
    features = extract_image_features(img_path)                    # Extract image features
    caption = generate_caption(features)                           # Generate caption
    img = image.load_img(img_path, target_size=(224, 224))         # Load image for display

    # Display image
    plt.imshow(img)
    plt.axis('off')
    plt.title("Generated Caption")
    plt.show()

    # Display in tabular format
    data = {
        "Image Path": [img_path],
        "Extracted Features Shape": [features.shape],
        "Generated Caption": [caption]
    }
    df = pd.DataFrame(data)                                       # Create a DataFrame for clean output
    print(df.to_string(index=False))                              # Print table without row indices

# Example usage
display_caption("C:/Users/asus/Pictures/Rabbit.jpg")  # More universally accepted)  # Replace with your image path