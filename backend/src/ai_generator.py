# send request to a LLM to give us a code challenge question. 
# We want the answer In a specifc format

import os
import json
from typing import Dict, Any
from google import genai
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ChallengeStructure(BaseModel):
    title: str
    options: list[str]
    correct_answer_id: int
    explanation: str

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:

    # TODO: add specific coding language/stach/concepts
    # TODO: in the output add a link of a video and/or online free resources that explain the concept
    # TODO: Add resources to go deeper in the topic
    # TODO: Make it useful for interviews -> combine theory and practice. 
    system_prompt = """ You are an expert coding challenge creator with 30 years of experience.
    Your task is to generate a coding question with multiple choice answers.
    The question should be appropriate for the specified difficulty level.
    
    For easy questions: Focus on basic syntax, simple operations, or common programming concepts.
    For medium questions: Cover intermediate concepts like data structures, algorithms, or language features.
    For hard questions: Include advanced topics, design patterns, optimization techniques, or complex algorithms.

    Return the challenge in the following JSON structure:
    {
        "title": "the question",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "correct_answer_id"L 0, //index of the correct answer(0 - 3),
        "explanation": "Detailed explanation of why the correct answer is right"
    }

    Make sure the options are possible but only one clearly correct answer.
    Make sure the output only includes the JSON. 
    Do not add any conversational text.
    do not wrap it in markdown or json blocks. 
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents= system_prompt,
            config={
                'response_mime_type': 'application/json',
                # 'response_schema': ChallengeStructure
                },
            
        )

        challenge_data = json.loads(response.text)

        required_fields = ["title", "options", "correct_answer_id", "explanation"]
        for field in required_fields:
            if field not in challenge_data:
                raise ValueError(f"Missing required field: {field}")
            
        return challenge_data

    except Exception as e:
        print(str(e))
        return{
            "title": "Basic Python List Operation",
            "options": [
                "my_list.append(5)",
                "my_list.add(5)",
                "my_list.push(5)",
                "my_list.insert(5)",
            ],
            "correct_answer_id": 0,
            "explanation": "In Python, append() is the correct method to add an element to the end of a list"
            ""
        }
