# Tech Haven Backend - Q&A API

This Flask service provides a simple customer support Q&A API for Tech Haven.

Key endpoints:
- GET /              -> Health check
- POST /api/ask      -> Submit a question { "question": "..." }
- GET /api/knowledge-base -> View predefined KB entries

Swagger/OpenAPI docs:
- /docs/openapi.json (spec)
- /docs/ (Swagger UI)

CORS is enabled for all origins to allow the React frontend to call the API.

Run locally:
- python run.py

Regenerate OpenAPI spec:
- python generate_openapi.py
