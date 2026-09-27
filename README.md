# COM3021 2026 — Workshop 1: Getting started with GCP

In this workshop you will explore the Google Cloud Console and Cloud Shell, then run and preview a small Flask data service from Cloud Shell.

This exercise does **not** deploy to Cloud Run or create billable Google Cloud resources. The app runs temporarily in your Cloud Shell environment and is previewed through the Cloud Shell web preview.

## Learning goals

- Find your way around the Google Cloud Console and open Cloud Shell.
- Clone and inspect a small application repository.
- Start a Python web application in a remote shell environment.
- Send HTTP requests, inspect responses and logs, and make a small change.
- Explain the difference between previewing an app in Cloud Shell and deploying a persistent cloud service.

## Requirements

- A Google account with access to Cloud Shell.
- No workshop credits or billing-enabled project are required for this activity.
- Internet access from Cloud Shell to clone this repository and install Flask.

## Activity

### 1. Explore Cloud Shell

Open Cloud Shell from the Console. Notice the terminal and open the Cloud Shell Editor. They show the same files. Cloud Shell is a Google-managed environment; it is not a virtual machine that you created in your project.

### 2. Clone and inspect this repository

```bash
git clone https://github.com/hsbarbosa/com3021-2026-w1-getting-started.git
cd com3021-2026-w1-getting-started
```

In the Editor, inspect `app.py`, `data/sample.csv`, and `requirements.txt`. Before running anything, predict what `/health` and `/api/summary` will return.

### 3. Install dependencies and start the app

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Leave this terminal running. The app listens on port `8080`.

### 4. Preview the app

In Cloud Shell, choose **Web Preview → Preview on port 8080**. Visit the home page, then try `/health` and `/api/summary` at the end of the preview URL.

The preview is private to your account and is intended for this temporary exercise; it is not a production deployment.

### 5. Trace requests and responses

Open a second terminal and run:

```bash
curl http://localhost:8080/health
curl http://localhost:8080/api/summary
```

Compare the JSON responses with the browser. Return to the first terminal and find the request log entries. In your own words, describe how a URL request reaches a route in `app.py` and becomes a response.

### 6. Make a change

Edit `app.py` to add a `max_value` field to `/api/summary`, calculated from the CSV data. Save the file, restart the app if needed, and confirm the new field appears in the browser and in `curl` output.

## Troubleshooting

- **The preview cannot connect:** make sure the app is still running and listening on `0.0.0.0:8080`; reopen Web Preview on port `8080`.
- **Address already in use:** stop the earlier app with `Ctrl+C`, then start it again.
- **Flask is not found:** activate the virtual environment with `source .venv/bin/activate`, then run `python -m pip install -r requirements.txt` again.
- **Clone or package installation fails:** check that Cloud Shell has internet access and retry once. If the issue persists, show the error to the instructor rather than changing project billing settings.

## Discussion

1. Which part of the exercise ran in Cloud Shell, and which part ran in your browser?
2. What did the HTTP request contain, and what did the application return?
3. What would need to change for this to become a persistent service other people could access?
4. Why is the Flask development server appropriate for this short exercise but not a production deployment?

## Stop

Press `Ctrl+C` in the server terminal when you finish. No cloud service has been deployed.
