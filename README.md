# InstaResume API

Lightweight demo API for the **InstaResume AI** hackathon project.
This repository provides a minimal Flask API that accepts an uploaded resume (file) and returns simple AI-style outputs (summary, headline, skills, LinkedIn about).

**This is a prompt/POC backend** — for the hackathon you can wire this to real LLM calls (OpenAI/Anthropic) or use as-is for demo purposes.

## Project structure
- `app.py` — Flask API server
- `utils.py` — simple helper functions (summary, headline, skills, linkedin about)
- `requirements.txt` — Python dependencies
- `.gitignore` — ignored files

## Quick run (local)
1. Create and activate a virtualenv (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run locally:
   ```bash
   python app.py
   ```
3. Test endpoints with `curl`:
   ```bash
   # health
   curl http://127.0.0.1:5000/

   # upload (multipart/form-data)
   curl -X POST -F "file=@sample_resume.txt" http://127.0.0.1:5000/upload

   # summary
   curl -X POST -H "Content-Type: application/json" -d '{"text":"Your resume text here"}' http://127.0.0.1:5000/summary
   ```

## API Endpoints
- `GET /` — health check
- `POST /upload` — accepts multipart form upload with key `file`, returns extracted text (simple decode)
- `POST /summary` — JSON `{"text": "... "}` returns an extractive summary
- `POST /headline` — JSON `{"text": "... "}` returns a short headline
- `POST /skills` — JSON `{"text": "... "}` returns a list of matched skills
- `POST /linkedin` — JSON `{"text": "... "}` returns a LinkedIn about string

## Deploy to Render (free tier)
1. Zip the repository or push to GitHub.
2. Create a free Render account: https://render.com
3. Create a new **Web Service** and connect the repo (or upload ZIP).
4. Set the **Build Command**: `pip install -r requirements.txt`
5. Set the **Start Command**: `gunicorn app:app`
6. Select the free plan and deploy — Render will provide a public URL.

## Next steps (recommended for full product)
- Integrate with OpenAI / Anthropic APIs for real LLM outputs
- Use `pdfminer.six` or `textract` to extract text from PDF resumes more reliably
- Add authentication & quota limits for public use
- Add frontend (Webflow / Bubble / Replit) or expose a simple static site for uploads
- Add tests & CI

## License
MIT
