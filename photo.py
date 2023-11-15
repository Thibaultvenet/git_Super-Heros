import cv2

# Initialise la capture vidéo à partir de la webcam (index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("La webcam n'est pas accessible")
    exit()

# Capture une image
ret, frame = cap.read()

# Si la capture est réussie, sauvegarde l'image
if ret:
    cv2.imwrite('photo_webcam.jpg', frame)  # Sauvegarde l'image capturée

# Libère la capture
cap.release()