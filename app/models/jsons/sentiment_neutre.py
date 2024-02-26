responses = {
  "respostas": [
    {"id": 0, "comentario": "É bom ter dias tranquilos, nos quais podemos relaxar um pouco."},
    {"id": 1, "comentario": "Às vezes, passar o tempo sem expectativas é uma oportunidade para descobrir algo novo."},
    {"id": 2, "comentario": "Fases neutras são normais. Use esse tempo para se reconectar consigo mesmo(a)."},
    {"id": 3, "comentario": "Manter a rotina pode trazer estabilidade. Surpresas nem sempre são necessárias."},
    {"id": 4, "comentario": "Nem todos os dias precisam ser emocionantes. Às vezes, a calmaria é reconfortante."},
    {"id": 5, "comentario": "A serenidade do dia pode ser um convite para apreciar as pequenas coisas."},
    {"id": 6, "comentario": "A ausência de grandes acontecimentos pode ser uma pausa bem-vinda."},
    {"id": 7, "comentario": "Aproveite para se envolver em atividades que trazem conforto e tranquilidade."},
    {"id": 8, "comentario": "Dias sem grandes mudanças são como intervalos necessários na música da vida."},
    {"id": 9, "comentario": "Manter a paz interior é uma conquista em si. Continue assim."},
    {"id": 10, "comentario": "Às vezes, a simplicidade do dia a dia é o que precisamos para recarregar."},
    {"id": 11, "comentario": "Fases neutras oferecem espaço para autoreflexão e autoconhecimento."},
    {"id": 12, "comentario": "A estabilidade na rotina pode ser um alicerce para alcançar objetivos a longo prazo."},
    {"id": 13, "comentario": "A falta de grandes emoções pode ser uma oportunidade para desfrutar a paz interna."},
    {"id": 14, "comentario": "A monotonia às vezes é o solo fértil para o crescimento pessoal."},
    {"id": 15, "comentario": "Apreciar a simplicidade do momento é uma arte em si."},
    {"id": 16, "comentario": "Acalme-se e aprecie a suavidade deste dia sem grandes acontecimentos."},
    {"id": 17, "comentario": "A ausência de surpresas pode ser uma pausa restauradora."},
    {"id": 18, "comentario": "Dias assim oferecem uma chance de descanso para a mente e o coração."},
    {"id": 19, "comentario": "Às vezes, a neutralidade é o terreno fértil para futuras experiências."},
    {"id": 20, "comentario": "Desfrute da tranquilidade deste momento, ela tem sua própria beleza."},
    {"id": 21, "comentario": "A simplicidade muitas vezes esconde preciosidades que só descobrimos no silêncio."},
    {"id": 22, "comentario": "Continue fluindo com a rotina. Às vezes, é nessa calma que se encontra a clareza."},
    {"id": 23, "comentario": "Os dias sem grandes eventos são como capítulos calmos em uma história."},
    {"id": 24, "comentario": "A estabilidade na rotina pode ser a base para futuras conquistas."},
    {"id": 25, "comentario": "A neutralidade é como uma tela em branco, pronta para ser preenchida com novas experiências."},
    {"id": 26, "comentario": "Aproveite o equilíbrio do dia, ele é uma paleta de cores suaves."},
    {"id": 27, "comentario": "Os momentos tranquilos são como pequenas pausas na melodia da vida."},
    {"id": 28, "comentario": "Às vezes, a paz está na simplicidade dos dias sem grandes reviravoltas."},
    {"id": 29, "comentario": "A ausência de expectativas pode ser libertadora. Aprecie o presente."},
    {"id": 30, "comentario": "Manter o equilíbrio emocional em dias neutros é uma habilidade valiosa."},
    {"id": 31, "comentario": "A serenidade do dia é um convite para se conectar consigo mesmo(a)."},
    {"id": 32, "comentario": "Continue navegando nas águas tranquilas do seu dia."},
    {"id": 33, "comentario": "Dias sem grandes emoções muitas vezes escondem preciosidades nas pequenas coisas."},
    {"id": 34, "comentario": "A ausência de eventos marcantes é como um descanso para a alma."},
    {"id": 35, "comentario": "A neutralidade permite que você aprecie as nuances simples da vida."},
    {"id": 36, "comentario": "A tranquilidade do dia é uma oportunidade para nutrir a paz interior."},
    {"id": 37, "comentario": "Dias sem expectativas são como uma tela em branco, pronta para ser pintada com novas experiências."},
    {"id": 38, "comentario": "Continue navegando nas águas calmas da sua rotina habitual."},
    {"id": 39, "comentario": "A ausência de grandes acontecimentos é um convite para apreciar as pequenas alegrias."},
    {"id": 40, "comentario": "A neutralidade do dia oferece espaço para simplesmente ser."},
    {"id": 41, "comentario": "A calmaria é como um abraço suave do universo, permita-se senti-la."},
    {"id": 42, "comentario": "Continue aproveitando a suavidade deste dia sem grandes emoções."},
    {"id": 43, "comentario": "Os dias tranquilos são oportunidades para recarregar as energias."},
    {"id": 44, "comentario": "A paz do dia é um convite para respirar fundo e apreciar o momento presente."},
    {"id": 45, "comentario": "A simplicidade do dia é uma canção suave que embala a alma."}
  ]
}
    
def getResponse_neutre(id):
    for resposta in responses["respostas"]:
        if resposta["id"] == id:
            return resposta["comentario"]
    return "Comentário não encontrado."