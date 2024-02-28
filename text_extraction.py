import easyocr
import cv2
import csv
import matplotlib.pyplot as plt
def extract_register_number(imgage_path):
    reader = easyocr.Reader(["en"])
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = reader.readtext(image)
    extracted_text = []
    for (bbox, text, _) in results:
        # Draw rectangles and put text on the image (your existing code)
        (top_left, top_right, bottom_right, bottom_left) = bbox
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(image, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Append the extracted text to the list
        extracted_text.append(text)