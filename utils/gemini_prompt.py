gemini_prompt = """You are required to extract structured information from a provided text or PDF file, mapping it to a predefined JSON format for a sample paper. The JSON object must include the following fields:
title: The title of the sample paper.
type: The type of sample paper (e.g., "previous_year"). If the type is unknown, default to "article."
time: The total time allocated for the paper, defaulting to 180 minutes if not specified.
marks: The total marks for the paper, defaulting to 100 if not provided.
params: A dictionary containing board, grade and subject only:
board: The educational board, defaulting to "CBSE" if not specified.
grade: The grade level, defaulting to 10 if not provided.
subject: The subject of the sample paper.
tags: A list of relevant keywords associated with the sample paper (e.g., ["algebra", "geometry"]). max keeep 7 tags.
chapters: A list of chapter titles extracted as strings (e.g., ["Quadratic Equations", "Triangles"]). Ensure that only titles are included, not full dictionaries.
sections: An array of section objects, each containing marks_per_question, type then a nested dictionary called questions which has question, answer, type, question_slug, reference_id, hint,params in it:
marks_per_question: The marks assigned to each question in the section, defaulting to 5 if not specified.
type: The type of section, defaulting to "default" if not provided.
questions: A list of question objects, each containing:
question: The text of the question.
answer: The corresponding answer to the question.
type: The type of question (e.g., "short", "long", "true/false"). Default to "short" if unspecified.
question_slug: A URL-friendly version of the question, generated based on the question text.
reference_id: A randomly generated identifier for each question (e.g., "QE001" for a quadratic equation).
hint: A hint to guide the user toward the answer, defaulting to a generic hint if none is found.
params: It is a nullable nested dictionary which is part of questions
It is crucial to ensure that all fields are populated in the output JSON. If any information is missing, use sensible defaults as specified. The final output should be a well-structured JSON object that can be directly stored in a MongoDB collection."""