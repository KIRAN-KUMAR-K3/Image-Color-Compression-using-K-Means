
# Image Color Compression using K-Means

![Color Compression](images/1.png)

This project demonstrates color compression of images using the K-Means clustering algorithm. The main script `main.py` reads images from the `images` directory, performs color compression by reducing the number of colors using K-Means clustering, and outputs the compressed images.

## Features

- **Image Input:** Supports PNG images located in the `images` directory.
- **Color Compression:** Utilizes K-Means clustering to reduce the number of distinct colors.
- **Output:** Displays the original and compressed images side by side.

## Requirements

- Python 3.x
- Pillow (PIL)
- NumPy
- Matplotlib
- scikit-learn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KIRAN-KUMAR-K3/Image-Color-Compression-using-K-Means.git
   cd Image-Color-Compression-using-K-Means
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your PNG images in the `images` directory.
2. Run `main.py` to perform color compression:
   ```bash
   python main.py
   ```
3. View the original and compressed images in the output.

## Example

![Original and Compressed Image](images/4.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
