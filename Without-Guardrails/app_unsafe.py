from groq import Groq

client = Groq(api_key="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")

# Dangerous API
def delete_users():
    return "🔥 All users deleted from database!"

def call_llm(prompt):
    response = client.chat.completions.create(
       model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

while True:
    user_input = input("You: ")

    # ❌ Direct execution (DANGEROUS)
    if "delete users" in user_input.lower():
        print("AI:", delete_users())
    else:
        print("AI:", call_llm(user_input))