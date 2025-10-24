import imageio.v2 as iio
import matplotlib.pyplot as plt
import numpy as np
import time

IMAGE = f"C:\\Users\\memoo\\Desktop\\python\\parallel\\img\\wallpaper.jpg"

def image_to_grayscale(img):
    result_image = np.zeros_like(img)
    for row in range(len(img)):
        for column in range(len(img[row])):
            pixel = img[row][column]
            gray_value = np.mean(pixel)
            result_image[row][column] = [gray_value, gray_value, gray_value]
    return result_image

def execution(img, method):
    inicio = time.perf_counter()
    result_image = method(img)
    fin = time.perf_counter()
    execution_time = fin - inicio
    print(f"Tiempo de ejecución: {execution_time:.6f} segundos")
    return result_image, execution_time


if __name__ == "__main__":

    img = iio.imread(IMAGE)

    result_image, execution_time = execution(img, method=image_to_grayscale)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    plt.suptitle(f"SEQUENTIAL - Tiempo de ejecución: {execution_time:.4f} segundos", fontsize=16) 
    axes[0].imshow(img)
    axes[0].set_title("Original")
    axes[1].imshow(result_image)
    axes[1].set_title("image_to_grayscale")
    plt.show()