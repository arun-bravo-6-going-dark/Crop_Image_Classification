import streamlit as st
import base64
import requests
import json
from PIL import Image
import re
import pandas as pd

# Function to encode the image
def encode_image(image):
    try:
        return base64.b64encode(image.read()).decode('utf-8')
    except Exception as e:
        st.error(f"Error encoding image: {e}")
        return None

# Function to classify an image
def classify_image(base64_image, api_key):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": """You will be provided an image of a crop. You should classify them as one of these six crops: cotton, groundnut, paddy, sorghum, sugarcane, black gram, others. You should give a confidence score. You should also provide the stage of plant growth from the image. The final response should be in the following format:
```
{
"crop_name": "<crop name>",
"confidence_score": "<confidence score in percentage>"
"stage_of_plant_growth": "<stage of plant growth>"
}
```"""
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is the crop in this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            },
        ],
        "temperature": 0,
        "max_tokens": 2048,
        "top_p": 0.5,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API request error: {e}")
        return None
    
# Streamlit UI
# Set wide mode as default
st.set_page_config(layout="wide")
st.title("🌾 Crop Image Classification 🌾")

# api_key = st.text_input("API Key", type="password")
api_key = st.secrets["openai_api_key"]

# uploaded_file = st.file_uploader("Choose an image...", type="jpg")
uploaded_file = st.file_uploader("Choose an image...", type=["jpeg", "jpg", "gif", "png"])


if uploaded_file is not None:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(uploaded_file, caption='📸 Uploaded Image', use_column_width=False, width=250)
        if st.button("Classify Image", type="primary"):
            base64_image = encode_image(uploaded_file)
            if base64_image:
                response_json = classify_image(base64_image, api_key)
                if response_json:
                    try:
                        response_content = response_json['choices'][0]['message']['content']
                        
                        # Define the regex pattern to extract content including the curly braces
                        pattern = r'\{.*?\}'

                        # Use re.search to find the first match of the pattern
                        match = re.search(pattern, response_content, re.DOTALL)

                        if match:
                            # Extract the content including the braces
                            content = match.group(0)
                        else:
                            st.error("Unexpected response format. Please try again.")
                            content = "{}"  # Assigning empty json structure to avoid json.loads error

                        response_data = json.loads(content)
                        
                        with col2:
                            st.subheader("Classification Result")
                            df = pd.DataFrame({
                                "🌱 Crop Name 🌱": [response_data['crop_name']],
                                "🔍 Confidence Score 🔍": [response_data['confidence_score']],
                                "🌰 Stage 🌿": [response_data['stage_of_plant_growth']],
                            })
                            st.markdown(df.to_html(index=False), unsafe_allow_html=True)
                            
                    except (KeyError, json.JSONDecodeError) as e:
                        st.error(f"Unexpected response format: {response_json}")

