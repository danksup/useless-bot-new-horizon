import httpx
import random

API_KEY = 'silly' 
CX = 'silly' 

async def search_image(query: str) -> str:
    """Search for an image on Google and return the image URL."""
    search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={CX}&key={API_KEY}&searchType=image&safe=active"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(search_url)

    if response.status_code == 200:
        data = response.json()
        print(f"Response data: {data}")  
        image_results = data.get("items", [])

        if not image_results:
            return "tidak ada gambar"

        random_image = random.choice(image_results)
        image_url = random_image['link']

        return image_url
    else:
        return f"Error fetching image results: {response.status_code} - {response.text}"

async def handle_image_request(args):
    """Handles the image search request."""
    if not args:
        return "prompt g boleh kosong."

    prompt = ' '.join(args)  

    if not prompt.strip():
        return "prompt g boleh kosong."

    image_url = await search_image(prompt)
    
    if image_url.startswith("Error"):
        return image_url  

    return f"Here is the image result: {image_url}"

