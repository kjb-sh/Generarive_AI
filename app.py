import openai
import requests
from io import BytesIO
from PIL import Image

# Set your OpenAI API key here
openai.api_key = 'AIzaSyBRdlTpn7AKEwEg8ZPWziryPZHzS9Kdwpo'

# Function to generate an image from a prompt
def generate_image_from_prompt(prompt, size="1024x1024"):
    try:
        # Call the OpenAI API to generate the image from the prompt
        response = openai.Image.create(
            prompt=prompt,
            n=1,  # Number of images to generate
            size=size  # Image size (1024x1024, 1024x1792, 1792x1024)
        )
        
        # Extract the URL of the generated image
        image_url = response['data'][0]['url']
        
        # Download the image
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        
        # Show the image
        image.show()
        
        # Optionally, save the image to a file
        image.save("generated_image.png")
        
        print(f"Image generated and saved as 'generated_image.png'.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Example prompt
prompt = "A futuristic city skyline with flying cars and neon lights at night."
generate_image_from_prompt(prompt)
