# image_classifier/utils.py

import numpy as np
from PIL import Image
from io import BytesIO

def read_file_as_image(file_data) -> np.ndarray:
	try:
		image = Image.open(BytesIO(file_data))
		image = np.array(image.convert("RGB").resize((256, 256)))
		return image
	except Exception as e:
		# Handle the error gracefully, e.g., log the error message and return an error response
		print(f"Error while reading image: {str(e)}")
		return None
