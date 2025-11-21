# --- Importação das Bibliotecas --- #
import cv2 
import mediapipe as mp

# --- Criando a classe de detector de mãos --- #
class DetectorMaos:
    """Classe responsável pela detecção das mãos"""
    def __init__(self, modo=False, max_maos=2, deteccao_confianca=0.5, rastreio_confianca=0.5, cor_pontos=(0,0,255), cor_conexoes=(255, 255, 255)):

        """
        Função responsável por inicializar a classe.

        :param modo: Modo da captura da imagem. Serve para saber se o mediapipe vai ficar o tempo todo rastreando. Esse parâmetro vai deixar o rastreio melhor, porém vai consumir mais processamento. Deixamos false para a detecção não ocorrer a todo momento.

        :param max_maos: Número máximo de mãos que serão detectados.

        :param deteccao_confianca: Percentual da taxa de detecção da mão. Se for menor que este limite, a detecção não ocorre. 

        :param rastreio_confianca: Percentual da taxa de rastreio dos pontos da mão. Se menor que este limite que definimos, o rastreio não ocorre.

        :param cor_pontos: Cor dos pontos

        :para cor_conexoes: Cor das conexões entre os pontos
        
        """

        # --- Inicializar os parâmetros --- #
        self.modo = modo 
        self.max_maos = max_maos
        self.deteccao_confianca = deteccao_confianca
        self.rastreio_confianca = rastreio_confianca
        self.cor_pontos = cor_pontos 
        self.cor_conexoes = cor_conexoes

        # --- Inicializar os módulos de detecção das mãos --- #

        self.maos_mp = mp.solutions.hands
        self.maos = self.maos_mp.Hands(
            self.modo,
            self.max_maos,
            1, # Complexidade do modelo. Já é valor 1 por padrão.
            self.deteccao_confianca,
            self.rastreio_confianca
        )

        # --- Função para desenhar os pontos nas mãos --- #
        self.desenho_mp = mp.solutions.drawing_utils

        # --- Configurações do desenho dos pontos
        self.desenho_config_pontos = self.desenho_mp.DrawingSpec(color=self.cor_pontos)

        # --- Configurações dos desenhos das conexões --- #
        self.desenho_config_conexoes = self.desenho_mp.DrawingSpec(color=self.cor_conexoes)

    # --- Criando um método para encontrar as mãos --- #
    def encontrar_maos(self, imagem, desenho=True):
        """
        Função responsável por detectar as mãos.
        :param imagem: Imagem capturada
        :param desenho: Desenhar os pontos e as conexões nas mãos
        :return: Retorna a imagem com a detecção
        """

        # --- Conversão do BGR para RGB --- #
        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

        # --- Passar a imagem convertida em RGB para o detector --- #
        self.resultado = self.maos.process(imagem_rgb)

        # --- Verificar se alguma mão foi detectada
        if self.resultado.multi_hand_landmarks:
            for pontos in self.resultado.multi_hand_landmarks:
                if desenho:
                    # --- Desenhar os pontos nas mãos detectadas --- #
                    self.desenho_mp.draw_landmarks(
                        imagem, # Imagem de captura
                        pontos, # Pontos da mão
                        self.maos_mp.HAND_CONNECTIONS, # Conexão entre os pontos
                        self.desenho_config_pontos, # Cor dos pontos
                        self.desenho_config_conexoes # Cor das conexões
                    )

        return imagem
    
    def encontrar_pontos(self, imagem, mao_num=0, desenho=True, cor=(0, 0, 255), raio=7, ponto_detectado = 8):
        """
        Função responsável por encontrar a posição dos pontos das mãos

        :param imagem = imagem capturada
        :param mao_num = número da mão detectada
        :param desenho = desenhar o ponto encontrado
        :param cor = tupla com a cor do ponto no padrão BGR
        :param raio = raio do círculo do ponto
        :param ponto_detectado = ponto a ser detectado (caso queira detectar um ponto específico da mão. O parâmetro na função é `ponto_detectado=0`, com o 0 podendo ser substituído por qualquer outro ponto da mão)
        :return = lista com os pontos detectados
        """

        # --- Lista com os pontos detectados --- #
        lista_pontos = []

        # --- Verificar se alguma mão foi detectada --- #
        if self.resultado.multi_hand_landmarks:
            # --- Obter os pontos de UMA mão que forem detectadas --- #
            mao = self.resultado.multi_hand_landmarks[mao_num]

            # --- Obter as informações dos pontos --- #
            for id, ponto in enumerate(mao.landmark):
                # --- Obter as dimensões da imagem capturada --- #
                altura, largura, _ = imagem.shape

                # --- Transformar a posição do ponto de proporção para pixel
                centro_x, centro_y = int(ponto.x * largura), int(ponto.y * altura)

                # --- Adicionar os pontos da mão detectada na lista --- #
                lista_pontos.append([id, centro_x, centro_y])

                # --- Colocar um círculo em um ponto --- #
                if desenho:
                    if id == ponto_detectado:
                        cv2.circle(
                            imagem, # imagem da captura
                            (centro_x, centro_y), # centro do círculo
                            raio, # raio do círculo
                            cor, # cor do círculo
                            cv2.FILLED # espessura
                        )
        
        return lista_pontos


# --- Criando função para fazer os testes --- #
def main():
    # --- Captura do vídeo pela webcam --- #
    captura = cv2.VideoCapture(0)

    # --- Instaciar a classe do detector --- #
    detector = DetectorMaos()

    # --- Realizar a captura --- #
    while True:
        # --- Obter o frame --- #
        _, imagem = captura.read()

        # --- Realizar a detecção das mãos
        imagem = detector.encontrar_maos(imagem)


        # --- Lista com os pontos --- #
        lista_pontos = detector.encontrar_pontos(imagem)

         # --- Mostrar a imagem de captura --- #
        cv2.imshow('Captura', imagem)

        # --- Tempo de atualização do loop de captura --- #
        cv2.waitKey(1) # Atualiza a captura com delay de 1 milisegundo


if __name__ == '__main__':
    main()