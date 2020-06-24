file = open("task1-test-input.txt")


def q1(polls, num_of_test_case):
    num_of_fruit = polls[0].split()[0]
    num_of_people = int(polls[0].split()[1])
    rankings = polls[1:num_of_people+1]

    to_exclude = set()
    ranking = {}
    for i in range(num_of_people):
        if i[0] not in ranking:
            ranking[i[0]] = 0
        rankings[i[0]]


    # print(polls[0:num_of_people])
    # ranking = [i for i in polls[0:num_of_people]]
    # print(ranking)

    

    # for key, item in fruits_aval.items():
    #     if fruits_aval[key] == True:
    #         print("Case #" + str(num_of_test_case) + ": " + key)


with file as f:
    lines = [line.rstrip() for line in f]
    # print(lines)
    polls = []
    cur_test_case = 1
    for n in range(2, len(lines)):
        if lines[n] == '':
            q1(polls, cur_test_case)
            cur_test_case += 1
            polls = []
        else:
            polls.append(lines[n])