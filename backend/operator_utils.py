from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import os

# Load the API key

def operator_request(prompt, system_role="assistant"):
    """
    Sends a prompt to Operator using the new OpenAI API interface.
    """
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7)
        return response.choices[0].message.content
    except Exception as e:
        return f"Operator Error: {str(e)}"

