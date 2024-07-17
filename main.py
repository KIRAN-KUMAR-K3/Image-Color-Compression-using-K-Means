import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans

# Load the image using PIL
image_path = '<path_of_the_image>'
image = Image.open(image_path)

# Convert the image to RGB if it's not already in that mode
if image.mode != 'RGB':
    image = image.convert('RGB')

# Convert the image to a NumPy array
image_np = np.array(image)

# Reshape the image to be a list of pixels
pixels = image_np.reshape(-1, 3)

# Number of colors (clusters)
n_colors = 16

# Perform K-Means clustering
kmeans = KMeans(n_clusters=n_colors, random_state=42)
kmeans.fit(pixels)

# Get the cluster centers (the colors)
colors = kmeans.cluster_centers_

# Assign each pixel to the nearest cluster center
new_pixels = colors[kmeans.predict(pixels)]

# Reshape the new pixels to the original image shape
new_image_np = new_pixels.reshape(image_np.shape).astype(np.uint8)

# Convert the compressed NumPy array back to an image
compressed_image = Image.fromarray(new_image_np)

# Display the original and compressed images
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image_np)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(new_image_np)
axes[1].set_title(f'Compressed Image with {n_colors} colors')
axes[1].axis('off')

plt.show()

