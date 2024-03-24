import openai

openai.api_key = 'your-api-key-here'

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
    )
    return response.choices[0].text.strip()