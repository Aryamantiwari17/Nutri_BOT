import base64
import google.generativeai as genai
import cv2
import pytesseract

# Configure Gemini AI
genai.configure(api_key="Enter Your API Key Here")

# Global variables to store extracted text, user profile, and conversation history
stored_extracted_text = None
user_profile = {}
conversation_history = []  # List to store the chat history

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def perform_ocr(image_path):
    """Perform OCR on the given image path and return extracted text."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(threshold)
    return text

def extract_text_with_gemini(text):
    """Extract structured information using Gemini AI."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Please extract and analyze the nutritional information and ingredients from the following text.
        Provide a structured output with the following:
        1. List of ingredients
        2. Nutritional facts (calories, fats, carbs, proteins)
        3. Any health claims mentioned
        4. Potential allergens
        
        Text:
        {text}
        """
        
        # Call the Gemini API with the text input
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        return f"Error with Gemini extraction: {str(e)}"

def health_analysis(product_info, user_profile):
    """Generate a health analysis of the product using Gemini AI, personalized for the user."""
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')

        # Extract relevant information from user profile
        name = user_profile.get('name', 'User')
        age = user_profile.get('age', 'Unknown')
        height = user_profile.get('height', 'Unknown')
        weight = user_profile.get('weight', 'Unknown')
        medical_conditions = user_profile.get('medical_conditions', 'None')

        # Construct the prompt with specific parameters
        prompt = f"""
        Generate a health analysis for the following product information considering the user's profile and Remember, I am your AI chatbot for health analysis, designed to assist like a real dietitian.
        I can help analyze nutritional information and provide personalized health advice. Please respond accordingly also tell my bmi also:

        User Profile:
        Name: {name}
        Age: {age}
        Height: {height}
        Weight: {weight}
        Medical Conditions: {medical_conditions}

        Product Information: {product_info}

        Analysis:"""
        

        # Call the Gemini API with the text input
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        return f"Error generating health analysis: {str(e)}"


def gather_user_profile():
    """Function to gather user profile information."""
    user_profile['name'] = input("What is your name? ")
    user_profile['age'] = input("What is your age? ")
    user_profile['height'] = input("What is your height? (e.g., 5'10\") ")
    user_profile['weight'] = input("What is your weight? (e.g., 70 kg) ")

    # Collecting medical conditions
    conditions = input("Do you have any medical conditions? (comma-separated) ")
    user_profile['medical_conditions'] = [condition.strip() for condition in conditions.split(',')] if conditions else []

def weighted_conversation_history():
    """Return a string representation of the conversation history."""
    return [f"{item}" for item in conversation_history]

def answer_question_with_gemini(context, question):
    """Use Gemini AI to answer a question based on the extracted and stored context."""
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        prompt = f"""
        Based on the following context about a food product and previous conversations, please answer the question.
        
        Context:
        {context}
        
        Previous Conversations:
        {' '.join(weighted_conversation_history())}
        
        User Profile:
        Name: {user_profile['name']}
        Age: {user_profile['age']}
        Height: {user_profile['height']}
        Weight: {user_profile['weight']}
        Medical Conditions: {', '.join(user_profile['medical_conditions'])}
        
        Question: {question}
        
        Please provide a concise and accurate answer based solely on the information given in the context.
        """
        
        # Call Gemini AI to generate a response based on context and question
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        return f"Error with Gemini Q&A: {str(e)}"

def chatbot():
    global stored_extracted_text
    
    # Check if there's stored context
    if not stored_extracted_text:
        print("No context available. Please extract text first.")
        return
    
    # Allow the user to ask questions based on the stored context
    while True:
        question = input("\nAsk a question about the product (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get the answer from Gemini AI, including the user's profile
        answer = answer_question_with_gemini(stored_extracted_text, question)
        
        # Add the question and answer to the conversation history
        conversation_history.append(f"Q: {question} A: {answer}")
        
        print("Answer:", answer)

def main():
    global stored_extracted_text
    
    image_path = "/home/aryaman/testing/af43ab11f009db14f24f61f6963c6ec3.png"
    
    # Step 2: Perform OCR using pytesseract
    ocr_text = perform_ocr(image_path)
    
    # Step 3: Extract text with Gemini AI using the extracted OCR text
    stored_extracted_text = extract_text_with_gemini(ocr_text)
    
    # Notify user that processing is done
    print("Processing done. You can now ask questions about the product.")
    
    # Gather user profile information
    gather_user_profile()
    
    # Generate health analysis
    analysis = health_analysis(stored_extracted_text, user_profile)
    print("Health Analysis:", analysis)
    
    # Start the chatbot
    chatbot()

if __name__ == "__main__":
    main()
