import requests
import json
from bs4 import BeautifulSoup

job_results = []

def scrape_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    jobs = soup.find_all('h2')
    print(f"--- Found {len(jobs)} potential listings ---")
    
    for job in jobs:
        title = job.text.strip()
        print(f"Job Found: {title}")
        
        job_data = {
            "title": title,
            "source": "Real Python Website"
        }
        
        job_results.append(job_data)

scrape_jobs('https://realpython.github.io/fake-jobs/')

with open("results.json", "w") as f:
    json.dump(job_results, f, indent=4)

print("File 'results.json' has been created successfully!")