# tests/test_papers.py
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app  # Make sure to import your FastAPI app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.mark.asyncio
async def test_create_new_paper(client):
    # Define the sample paper data to send in the POST request
    paper_data = {
        "title": "Sample Paper Title",
        "type": "previous_year",
        "time": 180,
        "marks": 100,
        "params": {
            "board": "CBSE",
            "grade": 10,
            "subject": "Maths"
        },
        "tags": [
            "algebra",
            "geometry"
        ],
        "chapters": [
            "Quadratic Equations",
            "Triangles"
        ],
        "sections": [
            {
                "marks_per_question": 5,
                "type": "default",
                "questions": [
                    {
                        "question": "Solve the quadratic equation: x^2 + 5x + 6 = 0",
                        "answer": "The solutions are x = -2 and x = -3",
                        "type": "short",
                        "question_slug": "solve-quadratic-equation",
                        "reference_id": "QE001",
                        "hint": "Use the quadratic formula or factorization method",
                        "params": {}
                    },
                    {
                        "question": "In a right-angled triangle, if one angle is 30°, what is the other acute angle?",
                        "answer": "60°",
                        "type": "short",
                        "question_slug": "right-angle-triangle-angles",
                        "reference_id": "GT001",
                        "hint": "Remember that the sum of angles in a triangle is 180°",
                        "params": {}
                    }
                ]
            }
        ]
    }

    # Make the POST request to create a new paper
    response = client.post("/papers/", json=paper_data)

    # Check the response status code
    assert response.status_code == 201

    # Check that the response contains the ID of the newly created paper
    assert "id" in response.json()

    # Optionally, you can check if the ID is a valid format (e.g., string)
    assert isinstance(response.json()["id"], str)
