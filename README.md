# University Game Project using Pygame

![image](https://github.com/user-attachments/assets/8da8037a-f2d8-453b-b64a-cbf9c30071b1)

## Installation
You will need to install a few external libraries
```bash
pip install pytz
pip install tweepy
pip install schedule
```

## Configuration
You will also need Twitter's developer keys that you can get in the Twitter Developer Portal 
```python
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
bearer_token = r"YOUR_BEARER_TOKEN"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
```

You will also need to update the image paths located in the 'Imagenes' folder, as all those paths are specified in the JSON file.
```json
[
    {
        "image_1": "Imagenes\\your_image_1.jpg",
        "image_2": "Imagenes\\your_image_2.jpg",
        "image_3": "Imagenes\\your_image_3.jpg",
        "image_4": "Imagenes\\your_image_4.jpg",
        "image_5": "Imagenes\\your_image_5.png",
        "image_6": "Imagenes\\your_gif_6.gif",
        "image_7": "Imagenes\\your_image_7.jpg",
