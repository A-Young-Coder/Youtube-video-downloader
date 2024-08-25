import requests

url = "http://0.0.0.0:5000/download"
payload = [
    {"url": "https://www.youtube.com/watch?v=QAgRgucIFQM", "resolution": "720p"}
]
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
if response.status_code == 200:
    with open("combined_videos.zip", "wb") as f:
        f.write(response.content)
    print("Download successful, file saved as combined_videos.zip")
else:
    print(f"Failed to download: {response.status_code}")
    print(response.text)  # Print the response text for debugging
