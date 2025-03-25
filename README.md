# Crawler GCP

This project deploys a **FastAPI-based web crawler** to **Google Cloud Run**, allowing users to **send a URL via a POST request** and receive extracted content in **Markdown format**.

---

## 🚀 Features  
- Accepts a JSON payload with a `url` field.  
- Uses `crawl4ai` for **asynchronous web crawling**.  
- Deployed as a **serverless service** on **Google Cloud Run**.  
- **Dockerized** for portability and easy deployment.  

---

## 📌 Prerequisites  
Ensure you have the following installed:  
- **Google Cloud SDK (`gcloud`)** – [Install Guide](https://cloud.google.com/sdk/docs/install)  
- **Docker** – [Install Guide](https://docs.docker.com/get-docker/)  
- **Python 3.12+**  
- **Postman (Optional)** for testing  

---

## 📂 Project Structure  
```plaintext
├── build/
│   └── cloudbuild.yaml  # Google Cloud Build configuration
├── main.py              # FastAPI app handling requests
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── README.md            # Project documentation
```
---

## ⚙️ Setup and Run Locally  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-repo/web-crawler-api.git
cd web-crawler-api
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run crawl4ai setup
```bash
crawl4ai-setup
```

### 4️⃣ Run the FastAPI server
```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

---

## 🐳 Deploy to Google Cloud Run

### 1️⃣ Build and Submit Docker Image
```bash
gcloud builds submit --tag REGION/PROJECT-ID/REPO-NAME/IMAGE-NAME:TAG
```

### 2️⃣ Deploy to Cloud Run
```bash
gcloud run deploy IMAGE-NAME \
  --image REGION/PROJECT-ID/REPO-NAME/IMAGE-NAME:TAG \
  --platform managed \
  --region REGION \
  --allow-unauthenticated \
  --memory 1Gi \
  --cpu 2
```
---

## 📨 Making API Requests

### 📌 POST Request in Postman
* URL:
  ```plaintext
  https://your-cloud-run-url/
  ```
* Headers:
  ```plaintext
  Content-Type: application/json
  ```
* Body (raw, JSON format):
  ```json
  {
    "url": "https://www.nbcnews.com/business"
  }
  ```
---

## 📌 Using curl
```bash
curl -X POST "https://your-cloud-run-url/" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.nbcnews.com/business"}'
```
---

## 📖 Response Format
The API returns extracted Markdown content:
```json
{
  "content": "# Headline\n\nSome extracted text from the page..."
}
```
