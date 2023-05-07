import os
from functools import partial

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def send_question(question: str) -> dict:
    prompt=f"Data scientist, {question}"

    return openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=250,
        n=1,
        stop=None,
        temperature=0.7,
    )


def retrieve_ai_answer(response: dict) -> str:
    return response.choices[0].text


def get_code_info(question: str, code: str) -> str:
    resp = send_question(f"{question}\n\n{code}")
    return retrieve_ai_answer(resp)


retrieve_data_label = partial(
    get_code_info,
    question="Provide a pandas dataframe that summarizes this data set.",
)

retrieve_data_summary = partial(
    get_code_info,
    question="Summarize this data in 1 word.",
)

# retrieve_data_insights = partial(
#     get_code_info,
#     question="Provide insight for this data in 2 sentences.",
# )

# retrieve_data_visualization = partial(
#     get_code_info,
#     question="Can you display a visualization of the data?",
# )
