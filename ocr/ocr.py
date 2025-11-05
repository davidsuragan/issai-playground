import requests
from config import API_MAIN  # Import all configurations like API_MAIN

def ocr_image(file_path, api_key):
    """
    Send an image file to the Mangisoz OCR endpoint and get recognized text.
    :param file_path: Path to the image file (e.g., .png, .jpg)
    :param api_key: Bearer token for authentication
    :return: OCR result as JSON or None if error
    """
    url = "https://mangisoz.nu.edu.kz/api/file/ocr/"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare multipart/form-data
    with open(file_path, "rb") as f:
        files = {"file": (file_path.split("/")[-1], f, "image/png")}
        response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        try:
            result = response.json()
            return result
        except ValueError:
            print("⚠️ Сервер JSON қайтармады:", response.text)
            return None
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return None

if __name__ == "__main__":
    result = ocr_image("example.png", API_MAIN)
    print("🔍 OCR Result:")
    print(result)
