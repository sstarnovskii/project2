import random as r
gold = 0
print("Добро пожаловать в игру «Алазония», текстовый квест в средневековом фентезийном мире.")
print("Вы - молодой искатель приключений по имени Бинк. Только что вы вошли в город Торба.")
print("Как и любой другой начинающий герой, вы грезите о славе и сражениях, но начинать надо с чего-то поскромнее.")
print("Ваш баланс: ", gold, " золотых", sep="")
print("Выбирайте, чем заняться:")
q1 = int(input("1 - помочь старушке нарубить дров, 2 - попробовать обворовать дом купца, 3 - поспать. "))
if q1 == 1:
    print("Пожилая женщина отблагодарила вас 10 золотыми. Плюс в карму вам тоже обеспечен.")
    gold = gold + 10
elif q1 == 2:
    success = int(r.choice("12"))
    if success == 1:
        print("Вы успешно украли у купца 20 золотых! Но в груди возникло зудящее неприятное чувство.")
        gold = gold + 20
    else:
        print("Купец поймал вас за воровством! Вы с позором изгнаны из города. Ваше будущее остается туманным.")
        print("Игра окончена. Вы накопили", gold, "золотых и ничем не прославились. Попробуйте снова.")
        exit()
else:
    print("Вы отоспались. Сон - это хорошо, но вы не стали ближе к славе, о которой так мечтали.")

print("Ваш баланс: ", gold, " золотых", sep="")

print('Вы наткнулись на странствующего торговца. Он предлагает вам добротный меч по "скромной" цене в 10 золотых.')
if gold >= 10:
    sw = int(input("Желаете ли вы приобрести меч? 1 - да, 2 - нет. "))
    if sw == 1:
        gold = gold - 10
        sword = 1
        print("Вы приобрели меч. Торговец уверяет, что он прослужит еще долго.")
    else:
        print("Вы решаете оставить деньги при себе. Торговец обиженно уходит.")
else:
    print("Вы спешите убраться отсюда, поняв, что вам не хватает средств. Торговец ехидно ухмыльнулся вслед.")
print("Ваш баланс: ", gold, " золотых", sep="")
