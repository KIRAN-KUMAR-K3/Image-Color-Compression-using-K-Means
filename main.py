import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans
import sys
from tkinter import Tk, filedialog, simpledialog

def load_image(image_path):
    """Load and return an image in RGB mode."""
    try:
        image = Image.open(image_path)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        sys.exit(1)

def compress_image(image, n_colors):
    """Compress the image to a specified number of colors using K-Means clustering."""
    image_np = np.array(image)
    pixels = image_np.reshape(-1, 3)
    
    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(pixels)
    
    colors = kmeans.cluster_centers_
    new_pixels = colors[kmeans.predict(pixels)]
    
    new_image_np = new_pixels.reshape(image_np.shape).astype(np.uint8)
    return Image.fromarray(new_image_np)

def display_images(original_image, compressed_image, n_colors):
    """Display the original and compressed images side by side."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(original_image)
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    axes[1].imshow(compressed_image)
    axes[1].set_title(f'Compressed Image with {n_colors} Colors')
    axes[1].axis('off')

    plt.show()

def save_compressed_image(compressed_image):
    """Prompt the user to select a location to save the compressed image and save it."""
    root = Tk()
    root.withdraw()  # Hide the root window

    # Ensure 'outputs' directory exists
    output_dir = 'outputs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    file_path = filedialog.asksaveasfilename(
        title="Save Compressed Image",
        initialdir=output_dir,
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")]
    )

    if file_path:
        compressed_image.save(file_path)
        print(f"Compressed image saved as: {file_path}")
    else:
        print("No file selected for saving. The compressed image was not saved.")

def main():
    """Main function to execute the image compression and display results."""
    # Input file path and number of colors
    image_path = input("Enter the path to the image file: ")
    if not os.path.isfile(image_path):
        print("The provided file path does not exist. Exiting.")
        sys.exit(1)

    n_colors = int(input("Enter the number of colors for compression: "))

    # Load and process the image
    image = load_image(image_path)
    
    # Display original image size
    original_size = os.path.getsize(image_path)
    print(f"Original file size: {original_size} bytes")
    
    # Compress the image
    compressed_image = compress_image(image, n_colors)
    
    # Display images
    display_images(image, compressed_image, n_colors)

    # Save the compressed image
    save_compressed_image(compressed_image)

if __name__ == "__main__":
    main()
