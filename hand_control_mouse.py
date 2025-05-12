import cv2
import mediapipe as mp
import pyautogui
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
screen_w, screen_h = pyautogui.size()
cap = cv2.VideoCapture(0)

grab = False
click_bloqueado = False 

def calcular_distancia(lm1, lm2):
    return math.sqrt(
        (lm1.x - lm2.x) ** 2 +
        (lm1.y - lm2.y) ** 2
    )

def Escrever(frame, texto, x, y):
    cv2.putText(
        frame,
        texto,
        (int(x), int(y)),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    h, w, _ = frame.shape

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            x = hand_landmarks.landmark[5].x
            y = hand_landmarks.landmark[5].y

            distancia_indicador = calcular_distancia(hand_landmarks.landmark[8], hand_landmarks.landmark[6])
            distancia_medio = calcular_distancia(hand_landmarks.landmark[12], hand_landmarks.landmark[10])

            # Mostrar distâncias na tela
            Escrever(frame, f'Distancia Dedo Medio: {distancia_medio:.5f}', 50, screen_h / 2)
            Escrever(frame, f'Distancia Dedo Indicador: {distancia_indicador:.5f}', 50, screen_h / 2 + 30)
            Escrever(frame, f'Apertando: {grab}', 50, screen_h / 2 + 60)

            # Lógica de clique
            if not grab:
                if distancia_indicador < 0.03 and not click_bloqueado:
                    pyautogui.click()
                    click_bloqueado = True
                elif distancia_medio < 0.07:
                    pyautogui.mouseDown()
                    grab = True
            else:
                if distancia_medio > 0.07:
                    pyautogui.mouseUp()
                    grab = False
                    click_bloqueado = False

            # Mover o mouse
            screen_x = int(x * screen_w)
            screen_y = int(y * screen_h)
            pyautogui.moveTo(screen_x, screen_y)

            # Desenhar a mão
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    frame = cv2.resize(frame, (640, 350))  # ou qualquer tamanho menor que desejar

    cv2.imshow("Controle de Mouse com a Mão", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
