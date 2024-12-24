
if __name__ == '__main__':
    team1_num = 5
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451
    tasks_total = 82
    time_avg = 45.2
    challenge_result = 'Победа команды Волшебники данных!'


    team1_num = input("количество участников первой команды: ")
    print("В команде Мастера кода участников: %s !" % team1_num)

    team1_num, team2_num = input("количество участников в обеих командах:"), input()
    print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))


    score_2 = input('количество задач решённых командой 2 ')
    print("Команда Волшебники данных решила задач: {} !".format(score_2))

    team2_time = input('время за которое команда 2 решила задачи ')
    print("Волшебники данных решили задачи за {} с !".format(team2_time))


    score_1, score_2 = input('количество решённых задач по командам:'), input()
    print(f"Команды решили {score_1} и {score_2} задач.")

    challenge_result = input('исход соревнования: ')
    print(f'Результат битвы: {challenge_result}')

    tasks_total, time_avg = input('количество задач: '), input('среднее время решения: ')
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')




