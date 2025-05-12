# hand_control_mouse
# 🖱️ Controle de Mouse com a Mão usando Python, OpenCV e MediaPipe

Este projeto permite controlar o mouse do computador utilizando gestos da mão captados pela webcam, com detecção precisa baseada em `MediaPipe` e automação via `pyautogui`.

## ✨ Funcionalidades

- 🖐️ **Movimentação do mouse** com a posição da mão.
- 👉 **Clique simples** ao aproximar o dedo indicador do médio.
- ✊ **Clique sustentado (drag)** ao fechar a mão e soltar ao abrir.
- 📺 Feedback visual com anotações em tempo real na tela.

## ⚙️ Tecnologias utilizadas

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)

## 🎯 Objetivo
Este projeto tem como foco a acessibilidade digital, criando uma interface alternativa para controle do computador por pessoas com limitações motoras, utilizando apenas uma webcam comum e gestos com as mãos.

## 📽️ Demonstração
![2025-05-11-22-59-35-Trim2](https://github.com/user-attachments/assets/a1d5d4c1-be53-48b6-a18c-7971dae8d803)


## 🧠 Como funciona?
- A webcam detecta a mão em tempo real.
- A posição da mão é usada para mover o cursor.
- A distância entre os dedos define as ações:
- Indicador para baixo → clique simples.
- Dedo médio para baixo → clique e arraste.

## 💡 Possíveis aplicações
Pessoas com deficiência motora nos membros inferiores ou superiores.
Ambientes onde o uso de periféricos físicos não é viável.
Exploração de interfaces naturais para controle de dispositivos.

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se livre para abrir issues e pull requests com melhorias, sugestões ou correções.
