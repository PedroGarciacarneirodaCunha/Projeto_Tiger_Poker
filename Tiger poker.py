# Bibliotecas importadas:
import cv2
import numpy as np

# Iniciando a captura de imagem com C920:
cap = cv2.VideoCapture(1)  # Use 0 para a webcam padrão, ou 1 para a Logitech C920 (dependendo do sistema)

# vê se ligou a câmera corretamente:
if not cap.isOpened():
    print("Error: Could not open the Logitech C920.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Can't receive frame. Exiting...")
        break

    # Display the resulting frame
    cv2.imshow('Logitech C920 Feed', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('0'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()