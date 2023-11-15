import numpy as np
import matplotlib.pyplot as plt

random = False
normal = False

def create_checkerboard(size, num_squares):
    """
    Create a checkerboard image of given size and number of squares.
    This code is provided for you. You do not need to change it.

    Args:
    - size: int, size of the image
    - num_squares: int, number of squares in the checkerboard

    Returns:
    - checkerboard: numpy array, the checkerboard image
    """
    checkerboard = np.zeros((size, size))
    square_size = size // num_squares
    for i in range(num_squares):
        for j in range(num_squares):
            if (i + j) % 2 == 0:
                checkerboard[i * square_size: (i + 1) * square_size,
                             j * square_size: (j + 1) * square_size] = 1
    return checkerboard


def add_random_noise_to_image(image, noise_level=1):
    """
    Add random noise to an image.

    Args:
    - image: numpy array, the image to add noise to
    - noise_level: int, the maximum value of the noise

    Returns:
    - noisy_image: numpy array, the noisy image
    """
    noisy_image = image #TODO: Add random noise to the image
    return noisy_image


def add_normal_noise_to_image(image, mean, noise_level=1):
    """
    Add normally distributed noise to an image.

    Args:
    - image: numpy array, the image to add noise to
    - mean: float, the mean of the noise
    - noise_level: float, the standard deviation of the noise

    Returns:
    - noisy_image: numpy array, the noisy image
    """
    noisy_image = image #TODO: Add random noise to the image
    return noisy_image

def main():
    """
    Test adding noise to a simple image and plot the original checkerboard and the noisy version. Then print both.
    This code is provided for you. You do not need to change it.
    """
    image_size = 100
    num_squares = 10
    checkerboard = create_checkerboard(image_size, num_squares)

    if random:
        noisy_checkerboard = add_random_noise_to_image(checkerboard, noise_level=5)
    if normal:
        noisy_checkerboard = add_normal_noise_to_image(checkerboard, mean, noise_level=noise_level)

    # Plot the original checkerboard and the noisy version
    plt.subplot(1, 2, 1)
    plt.imshow(checkerboard, cmap='gray')
    plt.title('Original Checkerboard')
    plt.subplot(1, 2, 2)
    plt.imshow(noisy_checkerboard, cmap='gray')
    plt.title('Noisy Checkerboard')
    plt.show()

if __name__ == '__main__':
    random = False
    normal = False
    input_choice = input("Input 1 for random numbers and 2 for noise that is normally distributed: ")
    if input_choice == '1':
        random = True
        noise_level = input("Input noise level (valid input is an integer): ")
        try: noise_level = int(noise_level)
        except ValueError:
            print("Wrong input! Valid input is an integer. Exiting program.")
            exit()
    elif input_choice == '2':
        normal = True
        noise_level = input("Input noise level (valid input is a float between 0 and 1): ")
        try:
            noise_level = float(noise_level)
            if noise_level < 0 or noise_level > 1: raise ValueError
        except ValueError:
            print("Wrong input! Valid input is a float between 0 and 1. Exiting program.")
            exit()
        mean = 0
    else:
        print("Wrong input! Valid input is 1 or 2. Exiting program.")
        exit()
    main()
