# Crop Image Classification App

## 🌾 About the Project
This project provides a **Crop Image Classification** tool using **Streamlit** and the OpenAI GPT-4o model. Given an image of a crop, the app can classify it into one of six predefined classes:
- **cotton**
- **groundnut**
- **paddy**
- **sorghum**
- **sugarcane**
- **black gram**

It also provides a **confidence score** and determines the **stage of plant growth** based on the input image.

---

## 🚀 Features
1. **Upload an Image:** Upload a crop image in formats like `JPEG`, `JPG`, `PNG`, or `GIF`.
2. **Crop Classification:** Classifies the crop and provides the crop name, confidence score, and stage of plant growth.
3. **Interactive UI:** Built using Streamlit for an easy-to-use and responsive interface.
4. **Powered by OpenAI:** Leverages GPT-4o for accurate classification and response generation.

---

## 🛠️ Installation

To run this project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/crop-classification-app.git
   cd crop-classification-app
   ```

2. **Install Dependencies:**
   Ensure you have Python 3.10 or later installed. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add OpenAI API Key:**
   - Create a `secrets.toml` file under the `.streamlit` directory:
     ```
     [secrets]
     openai_api_key = "YOUR_API_KEY"
     ```

4. **Run the App:**
   ```bash
   streamlit run app.py
   ```

---

## 📋 Usage
1. **Launch the App:** After running the app, open the browser link shown in the terminal.
2. **Upload an Image:** Choose a crop image to upload.
3. **Classify:** Click on the **Classify Image** button to receive the results.
4. **View Results:** Results include:
   - Crop Name 🌱
   - Confidence Score 🔍
   - Stage of Plant Growth 🌿

---

## 📦 Dependencies
In requirements.txt file

---

## 🖼️ Demo Screenshot
![Demo Screenshot](demo-screenshot.png)

---

## 🤝 Contributions
Contributions are welcome! Feel free to fork the project and submit a pull request.

---

## 🧾 License
This project is licensed under the **MIT License**.

---
