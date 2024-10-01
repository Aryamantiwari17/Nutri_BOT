# Nutri_BOT

Nutri_BOT is an AI-powered nutritional analysis tool that extracts and analyzes nutritional information from food product images using OCR and Gemini AI.

## Features

- OCR-based text extraction from food product images
- AI-powered nutritional information analysis
- Personalized health analysis based on user profiles
- Interactive Q&A chatbot for nutritional inquiries

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/Nutri_BOT.git
   cd Nutri_BOT
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install google-generativeai opencv-python pytesseract
   ```

4. Install Tesseract OCR:
   - Ubuntu/Debian:
     ```
     sudo apt-get install tesseract-ocr
     ```
   - macOS:
     ```
     brew install tesseract
     ```
   - Windows: Download and install from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

5. Set up your Gemini AI API key:
   - Sign up for Gemini AI and obtain an API key
   - Replace `"Enter Your API Key Here"` in the script with your actual API key

## Usage

1. Open `nutritional_analyzer.py` and modify the `image_path` variable:
   ```python
   image_path = "/path/to/your/image.png"
   ```

2. Run the script:
   ```
   python nutritional_analyzer.py
   ```

3. Follow the prompts to enter your user profile information and interact with the chatbot.

## Important Notes

- Ensure you have a valid Gemini AI API key and sufficient credits for API calls.
- The accuracy of the analysis depends on the quality of the input image and the OCR process.
- This tool is for informational purposes only and should not replace professional medical advice.

## Output
![Output](https://github.com/user-attachments/assets/59a7e039-6d3d-4fe1-8f66-ef8e0f6207ee)


## Troubleshooting

If you encounter issues:
- Verify that Tesseract OCR is correctly installed and accessible in your system's PATH.
- Check your internet connection for API calls to Gemini AI.
- Ensure your API key is correctly set in the script.

For any other problems, please open an issue on the GitHub repository.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

