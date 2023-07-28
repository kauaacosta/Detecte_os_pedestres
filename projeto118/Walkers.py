import cv2


# Crie nosso classificador de corpos
body_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture("C:/Users/comma/OneDrive/Área de Trabalho/Programação/projeto118/walking.avi")

# Faça o loop assim que o vídeo for carregado com sucesso
while True:
    
    # Leia o primeiro quadro
    ret, frame = cap.read()

    if not ret:
        break
    
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  

    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)   
    
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        
    cv2.imshow('Corpos Rastreados', frame)

    if cv2.waitKey(1) == 32: #32 é a barra de espaço
        break

cap.release()
cv2.destroyAllWindows()
