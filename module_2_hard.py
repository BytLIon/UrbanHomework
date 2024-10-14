import random

def gates_1():
    stone = [i for i in range(3,21)]
    return random.choice(stone)



def alg_result(stone):
    result_alg = ""
    for i in range(1, stone // 2 + 1):
        for j in range(2, stone + 1):
            if stone % (i + j) == 0:
                result_alg += str(i)
                result_alg += str(j)
    return result_alg


if __name__ == '__main__':
    stone_password = {3: "12", 4: "13", 5: "1423",
    6: "121524", 7: "162534", 8: "13172635", 9: "1218273645",
    10: "141923283746", 11: "11029384756", 12: "12131511124210394857",
    13: "112211310495867", 14: "1611325212343114105968", 15: "1214114232133124115106978",
    16: "1317115262143531341251161079", 17: "11621531441351261171089", 18: "12151811724272163631545414513612711810",
    19: "118217316415514613712811910", 20: "13141911923282183731746416515614713812911"}

    num_stone = gates_1()
    print("Врата 1 камень", num_stone)
    result = alg_result(num_stone)
    print("Пароль: ",result)

    if stone_password[num_stone] == result:
        print("I am a talking traveler")
