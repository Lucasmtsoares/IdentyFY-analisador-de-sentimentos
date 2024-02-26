responses = {
  "respostas": [
    {"id": 0, "comentario": "Lamento que esteja passando por isso. Estou aqui para oferecer meu apoio."},
    {"id": 1, "comentario": "Que situação difícil. Se precisar desabafar, estou à disposição."},
    {"id": 2, "comentario": "Estou aqui para oferecer meu suporte. Às vezes, compartilhar pode aliviar um pouco do peso."},
    {"id": 3, "comentario": "Sinto muito ouvir que está enfrentando momentos complicados. Estou aqui para ajudar."},
    {"id": 4, "comentario": "Estou aqui para apoiar você. Às vezes, compartilhar o fardo faz toda a diferença."},
    {"id": 5, "comentario": "Que desafio difícil. Se precisar de alguém para conversar, estou à disposição."},
    {"id": 6, "comentario": "Lamento que esteja se sentindo assim. Estou aqui para ajudar no que for necessário."},
    {"id": 7, "comentario": "É normal sentir-se para baixo às vezes. Estou aqui para oferecer meu suporte."},
    {"id": 8, "comentario": "Estou aqui para você. Se precisar conversar, estou disponível."},
    {"id": 9, "comentario": "Sinto muito que esteja passando por isso. Estou disponível para conversar."},
    {"id": 10, "comentario": "Lamento que esteja enfrentando essa situação. Se precisar de ajuda, estou à disposição."},
    {"id": 11, "comentario": "Estou aqui para oferecer meu apoio. Se precisar desabafar, estou à disposição."},
    {"id": 12, "comentario": "Que situação complicada. Se precisar de alguém para conversar, estou à disposição."},
    {"id": 13, "comentario": "Sinto muito ouvir que está passando por isso. Estou aqui para ajudar."},
    {"id": 14, "comentario": "Estou aqui para oferecer meu suporte. Às vezes, desabafar pode fazer diferença."},
    {"id": 15, "comentario": "Lamento que esteja enfrentando momentos difíceis. Estou aqui para ouvir."},
    {"id": 16, "comentario": "É compreensível sentir-se assim diante de desafios. Estou aqui para ajudar."},
    {"id": 17, "comentario": "Lamento que esteja se sentindo assim. Se precisar desabafar, estou aqui para ouvir."},
    {"id": 18, "comentario": "Estou aqui para apoiar você. Às vezes, compartilhar pode aliviar um pouco do peso."},
    {"id": 19, "comentario": "Que situação difícil. Saiba que não está sozinho(a). Estou aqui para ajudar."},
    {"id": 20, "comentario": "Sinto muito que esteja enfrentando momentos difíceis. Estou disponível para conversar."},
    {"id": 21, "comentario": "É normal se sentir para baixo às vezes. Estou aqui para oferecer meu suporte."},
    {"id": 22, "comentario": "Lamento que esteja se sentindo assim. Se precisar de ajuda, estou à disposição."},
    {"id": 23, "comentario": "Que desafio difícil. Estou aqui para te apoiar no que precisar."},
    {"id": 24, "comentario": "Sinto muito ouvir que está passando por isso. Estou aqui para ajudar."},
    {"id": 25, "comentario": "Estou aqui para oferecer meu apoio. Se precisar desabafar, estou à disposição."},
    {"id": 26, "comentario": "Lamento que esteja enfrentando momentos difíceis. Estou aqui para ouvir."},
    {"id": 27, "comentario": "Sinto muito que esteja passando por essa situação. Se precisar conversar, estou aqui."},
    {"id": 28, "comentario": "É compreensível sentir-se assim. Estou aqui para ajudar no que for possível."},
    {"id": 29, "comentario": "Estou aqui para oferecer meu suporte. Às vezes, desabafar pode fazer diferença."},
    {"id": 30, "comentario": "Lamento que esteja se sentindo assim. Se precisar de alguém para conversar, estou à disposição."},
    {"id": 31, "comentario": "Que desafio difícil. Saiba que estou aqui para te apoiar no que precisar."},
    {"id": 32, "comentario": "Sinto muito ouvir que está enfrentando momentos complicados. Estou aqui para ajudar."},
    {"id": 33, "comentario": "Estou aqui para oferecer meu apoio. Se precisar desabafar, estou à disposição."},
    {"id": 34, "comentario": "Lamento que esteja enfrentando momentos difíceis. Estou aqui para ouvir."},
    {"id": 35, "comentario": "É normal se sentir para baixo às vezes. Estou aqui para oferecer meu suporte."},
    {"id": 36, "comentario": "Sinto muito que esteja passando por isso. Estou disponível para conversar."},
    {"id": 37, "comentario": "Lamento que esteja se sentindo assim. Se precisar de ajuda, estou à disposição."},
    {"id": 38, "comentario": "Que situação difícil. Estou aqui para te apoiar no que precisar."},
    {"id": 39, "comentario": "Sinto muito ouvir que está enfrentando momentos complicados. Estou aqui para ajudar."},
    {"id": 40, "comentario": "Estou aqui para oferecer meu apoio. Se precisar desabafar, estou à disposição."},
    {"id": 41, "comentario": "Lamento que esteja enfrentando momentos difíceis. Estou aqui para ouvir."},
    {"id": 42, "comentario": "Sinto muito que esteja passando por essa situação. Se precisar conversar, estou aqui."},
    {"id": 43, "comentario": "É compreensível sentir-se assim. Estou aqui para ajudar no que for possível."},
    {"id": 44, "comentario": "Estou aqui para oferecer meu suporte. Às vezes, desabafar pode fazer diferença."},
    {"id": 45, "comentario": "Lamento que esteja se sentindo assim. Saiba que não está sozinho(a) e estou aqui para apoiar."}
  ]
}

def getResponse_negative(id):
    for resposta in responses["respostas"]:
        if resposta["id"] == id:
            return resposta["comentario"]
    return "Comentário não encontrado."
