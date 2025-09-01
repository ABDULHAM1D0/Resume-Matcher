import requests
import re
import time


class ResumeMatcher:
    def __init__(self, api_url, api_key, max_retries=5):
        self.api_url = api_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        self.max_retries = max_retries

    def _post_with_retry(self, payload):
        for i in range(self.max_retries):
            response = requests.post(self.api_url, headers=self.headers, json=payload)

            if response.status_code == 429:  # rate limited
                wait = 2 ** i  # exponential backoff
                print(f"[429 Too Many Requests] Waiting {wait}s before retry...")
                time.sleep(wait)
                continue

            try:
                response.raise_for_status()
                return response
            except requests.exceptions.HTTPError as e:
                print("HTTP Error:", e.response.status_code, e.response.text)
                raise

        raise Exception("Max retries exceeded due to rate limiting")

    def comparing(self, prompt):
        payload = {
            "model": "deepseek/deepseek-r1:free",  # ✅ DeepSeek Free model
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = self._post_with_retry(payload)
        resp_json = response.json()

        # Parse model output
        try:
            output = resp_json["choices"][0]["message"]["content"].strip()
        except (KeyError, IndexError):
            return {"score": None, "skills": [], "raw_output": resp_json}

        # Extract similarity score
        match = re.search(r"Similarity:\s*(\d+)%", output)
        similarity = int(match.group(1)) if match else None

        # Extract skills (comma or semicolon separated)
        skills_match = re.search(r"Skills?:\s*(.*)", output, re.IGNORECASE)
        skills = []
        if skills_match:
            skills_text = skills_match.group(1)
            skills = [s.strip() for s in re.split(r",|;", skills_text) if s.strip()]

        return {"score": similarity, "skills": skills, "raw_output": output}
