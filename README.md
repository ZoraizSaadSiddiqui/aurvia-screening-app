Overview

This project is a unified FastAPI + React application developed for the Aurvia Platform Technical Pre-Screening Challenge.

The application provides:

A FastAPI backend for threshold verification.
A React frontend served directly by FastAPI.
Pydantic-based request validation.
Mean and variance threshold analysis.
Single-command application startup without requiring a separate frontend development server.
Project Structure
aurvia-screening-app/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
Requirements
Python 3.10+
pip
Installation

Clone the repository and install dependencies:

pip install -r requirements.txt
Running the Application

Start the FastAPI server:
py -m uvicorn app:app --reload

The application will be available at:
http://127.0.0.1:8000

The React frontend is served directly by FastAPI from the templates directory.

API Specification
Endpoint
POST /api/threshold
Request Body
{
  "stream_values": [10, 15, 22, 19, 8],
  "max_variance": 10
}
Validation Rules
stream_values must be a non-empty array.
All values inside stream_values must be numeric.
max_variance must be numeric.
Empty arrays are rejected.
Invalid data types are rejected.
Processing Logic
Calculate the mean (average) of all values in stream_values.
Calculate the absolute deviation of each value from the mean.
Determine the largest deviation.
If any deviation exceeds max_variance, return:
{
  "status": "CRITICAL"
}
Otherwise return:
{
  "status": "STABLE"
}
Example Request
{
  "stream_values": [10, 15, 22, 19, 8],
  "max_variance": 10
}
Example Response
{
  "average": 14.8,
  "max_variance": 10.0,
  "element_count": 5,
  "status": "STABLE"
}
Frontend Features
React-based user interface.
Comma-separated numeric input parsing.
Configurable maximum variance value.
Asynchronous API requests using fetch().
Request button disabled while processing.
Error handling and validation feedback.
Green status indicator for STABLE results.
Red status indicator for CRITICAL results.
Dependencies
FastAPI
Uvicorn
Pydantic
Pandas
