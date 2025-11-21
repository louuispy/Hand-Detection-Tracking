# Detector de Mãos
---

Este projeto consiste em um sistema com foco em detectar mãos a partir da webcam e fazer um mapeamento dos pontos da mão. O projeto foi desenvolvido com o objetivo de aprofundar meus estudos em visão computacional com Python, visto que esse projeto é algo que .

<img width="461" height="304" alt="image" src="https://github.com/user-attachments/assets/1d5ace94-e033-4581-9f7c-b4175a905a0d" />

---

## Tecnologias utilizadas:

- Python (3.9)
- OpenCV
- MediaPipe

---

## Como utilizar:
1. Clone o repositório

```bash
git clone https://github.com/louuispy/Hand-Detection-Tracking.git
cd Hand-Detection-Tracking
```

2. Crie e ative um ambiente virtual

- Windows
```bash
python -m venv venv
venv\Scripts\activate
```


- Linux/MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Execute o script principal
```python
python main.py
```
Após isso, o sistema irá abrir sua webcam e iniciar a detecção das mãos e de um ponto específico da sua mão (no caso do código, o padrão está 8, mas pode ser qualquer ponto) em tempo real.

---

## Como o projeto funciona?

O projeto em si é organizado em torno da classe `DetectorMaos`, responsável por detectar as mãos, desenhar os pontos, conexões, extrair os landmarks para identificação dos pontos e afins.


Dentro dessa classe, temos a função `encontrar_pontos`, que retorna uma lista no formato:
```python
[id_do_ponto, x, y]
```

Essa lista armazena basicamente a localização do ponto específico que você quer detectar (exemplo do código: 8) em pixels, retornando tanto o ID desse ponto, como também suas coordenadas no eixo X e Y.

---

### Materiais para estudo:
Esse projeto foi desenvolvido, como dito anteriormente, para aprofundar meus conhecimentos em Visão Computacional, que é uma área que possuo interesse em atuar.
Essa parte de materiais contém justamente vídeos, documentações e tutoriais que me ajudaram a construir o projeto. (Recomendo bastante o tutorial do Mundo Python)

- [Documentação do Mediapipe](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker/python?hl=pt-br)
- [Tutorial de Detecção de Mãos - Mundo Python](https://youtu.be/JAJEnRaOU0A?si=OUuEmAWCdm-L6fnv)
- [Playlist de Projetos com Mediapipe (incluindo Hand Tracking)](https://youtube.com/playlist?list=PLBg7GSvtrU2OaYp2F-FqqZk0RUB4IUvvb&si=ILkcTFNWXk4YeEi_)

---

### 👨🏻‍💻 Autor
Luís Henrique
Data Scientist | UX/UI Designer 

[Conecte-se comigo no LinkedIn](https://www.linkedin.com/in/luishenrique-ia/)
