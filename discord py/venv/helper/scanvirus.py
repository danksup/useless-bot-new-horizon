import os
import requests
from typing import Final
from dotenv import load_dotenv


load_dotenv()
VIRUSTOTAL_API_KEY: Final[str] = os.getenv('VIRUSTOTAL_API_KEY')

if VIRUSTOTAL_API_KEY is None:
    raise ValueError("The environment variable 'VIRUSTOTAL_API_KEY' is not set.") 
VIRUSTOTAL_UPLOAD_URL = "https://www.virustotal.com/api/v3/files"

async def scan_attachment(message):
    if not message.attachments:
        return "No attachment found. Use `@multilinear scan <attachment>`."

    attachment = message.attachments[0]
    download_dir = "./downloads"
    os.makedirs(download_dir, exist_ok=True)  # Create directory if it doesn't exist
    file_path = os.path.join(download_dir, attachment.filename)

    try:
        # Save the attachment locally
        await attachment.save(file_path)  # Assuming this is an async method

        # Upload the file to VirusTotal
        with open(file_path, "rb") as file:
            headers = {"x-apikey": VIRUSTOTAL_API_KEY}
            files = {"file": (attachment.filename, file)}
            response = requests.post(VIRUSTOTAL_UPLOAD_URL, headers=headers, files=files)

        if response.status_code == 200:
            data = response.json()
            analysis_id = data["data"]["id"]
            return f"File uploaded successfully. Check scan results here: https://www.virustotal.com/gui/file/{analysis_id}"
        else:
            return f"Failed to scan file. Error: {response.status_code}, {response.text}"
    except Exception as e:
        return f"Error: {e}"
    finally:
        # Remove the local file
        if os.path.exists(file_path):
            os.remove(file_path)