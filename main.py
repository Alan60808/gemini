import google.generativeai as genai

def configure_and_create_model():
    """Configures the Google Generative AI library and creates a model instance."""
    try:
        # Replace with your actual API key
        genai.configure(api_key="AIzaSyDruuncb4JPXLjka-9vfYymA637b_yVXVU")

        generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        return genai.GenerativeModel(model_name="gemini-pro",
                                    generation_config=generation_config,
                                    safety_settings=safety_settings)
    except Exception as e:
        print(f"An error occurred while configuring the model: {e}")
        return None  # Indicate failure

def handle_user_input():
    """Prompts the user for input (text or image) and returns the processed input."""
    print("How would you like to provide your query?")
    print("1. Text input (type your question)")
    print("2. Image upload (upload an image for explanation)")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        user_input = input("Enter your question: ")
        return user_input
    elif choice == '2':
        # Implement image upload functionality (consider libraries like Pillow)
        print("Image upload functionality not yet implemented.")
        return None
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return None

def generate_response(model, user_input):
    """Generates a response using the model and the provided user input."""
    if user_input:
        prompt_parts = [user_input]
        try:
            response = model.generate_content(prompt_parts)
            return response.text
        except Exception as e:
            print(f"An error occurred while generating the response: {e}")
            return None
    else:
        return None

if __name__ == "__main__":
    model = configure_and_create_model()
    if model:
        while True:
            user_input = handle_user_input()
            response = generate_response(model, user_input)
            if response:
                print(response)
            else:
                print("An error occurred. Please try again.")
            print("\nWould you like to ask another question? (y/n)")
            answer = input().lower()
            if answer != 'y':
                break
    else:
        print("Failed to create the model.")
