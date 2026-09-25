import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)


def get_home_recommendations(budget, room, style, items):
    prompt = f"""
You are PocketSmart AI, a smart budget and shopping recommendation assistant.

Create a practical home interior plan based on the user's information.

Budget: ₹{budget}
Room: {room}
Style: {style}
Required items: {items}

Give the response in this format:

1. Budget allocation
2. Recommended items
3. Estimated price for each item
4. Suggested platform such as Amazon, Flipkart or IKEA
5. Total estimated cost
6. Remaining budget
7. Short explanation of why the recommendations fit the room and style

Important:
- Keep the total estimated cost within the user's budget.
- Do not claim that you checked live prices.
- Prices should be clearly described as approximate estimates.
- Give practical recommendations.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text