def translate(content: str) -> str:
    from together import Together
    client = Together()

    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
    messages=[
      {
        "role": "system",
        "content": "Translate the provided economic news headline from English into Korean, using concise and professional language. Ensure accurate use of economic and technical terminology. Return only the concise Korean translation without additional commentary."
      },
      {
        "role": "user",
        "content": content
      }
    ]

    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return completion.choices[0].message.content