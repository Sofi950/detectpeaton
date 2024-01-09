import cv2


# Crear nuestro clasificador de cuerpos
body_classifier = cv2.CascadeClassifier('haarscascade_fullbody.xml')

# Inicializar la captura de video para nuestro archivo de video
cap = cv2.VideoCapture('walking.avi')

# Comenzar el bucle una vez que el video esté cargado exitosamente
while True: 
    gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
    
    # Leer el primer cuadro
    ret, frame = cap.read()

    # Convertir cada cuadro a escala de grises
    body_classifier.detectMultiScale()
    # Pasar el cuadro a nuestro clasificador de cuerpos
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    
    # Extraer las cajas envolventes para cualquier cuerpo identificado
    for x, y, w, h in bodies:
     cv2.rectangle(frame, (x,y), (x + w, y + h), (o, 250, 0), 2)
    if cv2.waitKey(1) == 32: #32 es la barra espaciadora
        break

cap.release()
cv2.destroyAllWindows()
