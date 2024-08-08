import cv2
import numpy as np

def simulate_color_vision(image, vision_type='normal'):
    """
    Simulate different types of color vision impairments or animal vision.

    Args:
    - image: Input BGR image
    - vision_type: Type of vision to simulate ('normal', 'deuteranopia', 'protanopia', 'tritanopia', 'dog', 'cat', 'bird', 'shark', 'snake')

    Returns:
    - Transformed image simulating the specified type of vision
    """
    
    transform_matrices = {
        'normal': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float),
        'deuteranopia': np.array([[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.3, 0.7]], dtype=float),
        'protanopia': np.array([[0.567, 0.433, 0], [0.558, 0.442, 0], [0, 0.242, 0.758]], dtype=float),
        'tritanopia': np.array([[0.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, 0.525]], dtype=float),
        'dog': np.array([[0.5, 0.5, 0], [0.3, 0.7, 0], [0, 0.2, 0.8]], dtype=float),
        'cat': np.array([[0.2, 0.8, 0], [0.2, 0.8, 0], [0, 0.5, 0.5]], dtype=float),
        'bird': np.array([[0.1, 0.9, 0], [0.1, 0.1, 0.8], [0, 0.2, 0.8]], dtype=float),
        'shark': np.array([[0.3, 0.7, 0], [0.3, 0.7, 0], [0, 0.5, 0.5]], dtype=float), 
        'snake': np.array([[0.5, 0.5, 0], [0.5, 0.5, 0], [0.5, 0.5, 0]], dtype=float)  
    }

    transform_matrix = transform_matrices.get(vision_type, transform_matrices['normal'])

    transformed_img = cv2.transform(image, transform_matrix)
    transformed_img = np.clip(transformed_img, 0, 255).astype(np.uint8)
    return transformed_img

source_type = 'camera'
vision_type = 'tritanopia'

if source_type == 'image':
    image = cv2.imread('path_to_image.jpg')
    transformed_image = simulate_color_vision(image, vision_type=vision_type)
    cv2.imshow('Transformed Vision', transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif source_type == 'video' or source_type == 'camera':
    cap = cv2.VideoCapture(0 if source_type == 'camera' else 'path_to_video.mp4')

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        transformed_image = simulate_color_vision(frame, vision_type=vision_type)
        cv2.imshow('Transformed Vision', transformed_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
