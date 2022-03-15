def solution(genres, plays):
    tmp_dict = {} #dict[장르] = 합, 1등(i, play), 2등(i,play)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in tmp_dict.keys():
            tmp_dict[genre] = [0, [i, play], [i, play]]
        tmp_dict[genre][0] = tmp_dict[genre][0]+play
        play_is_max = tmp_dict[genre][1][1] < play
        play_is_same = ((tmp_dict[genre][2][1] == play)
                        or (tmp_dict[genre][1][1] == play))

        if play_is_max:
            tmp_dict[genre][2] = tmp_dict[genre][1]
            tmp_dict[genre][1] = [i, play]
        elif tmp_dict[genre][1] == tmp_dict[genre][2]:
            if play_is_max:
                tmp_dict[genre][1] = [i, play]
            else:
                tmp_dict[genre][2] = [i, play]
        elif ((tmp_dict[genre][2][1] < play) 
            and (tmp_dict[genre][1][1] > play)):
            tmp_dict[genre][2] = [i,play]
        elif play_is_same:
            tmp_list = [tmp_dict[genre][1], tmp_dict[genre][2], [i, play]]
            tmp_list.sort(key=lambda x: -x[1])
            tmp_dict[genre][1] = tmp_list[0]
            tmp_dict[genre][2] = tmp_list[1]
 
    answer = []
    while tmp_dict: #딕셔너리도 람다로 정렬 가능!!
        tmp_max = 0, tmp_dict.keys()
        for k in tmp_dict.keys():
            if tmp_dict[k][0] > tmp_max[0]:
                tmp_max = [tmp_dict[k][0], k]
        tmp = tmp_dict.pop(tmp_max[1])
        answer.append(tmp[1][0])
        if tmp[1][0] != tmp[2][0]:
            answer.append(tmp[2][0])

    return answer


# print(solution(['A', 'B', 'A', 'A', 'B'], [
#       500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
# print(solution(['B', 'A'], [500, 600]) == [1, 0])
# print(solution(['B'], [500]) == [0])
# print(solution(['B', 'A'], [600, 500]) == [0, 1])
# print(solution(['A', 'B'], [600, 500]) == [0, 1])
# print(solution(['A', 'A', 'B'], [600, 500, 300]) == [0, 1, 2])
# print(solution(['A', 'B', 'A'], [600, 500, 600]) == [0, 2, 1])
# print(solution(['A', 'B', 'A'], [600, 500, 700]) == [2, 0, 1])
# print(solution(['A', 'A', 'A'], [600, 500, 700]) == [2, 0])
# print(solution(['A', 'A', 'A'], [30, 20, 10]) == [0, 1])
# print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
#                [500, 600, 150, 800, 2500])==[4,1,3,0])
# print(solution(['classic'], [2500]) == [0])
# print(solution(['A', 'B', 'C'], [1, 2, 3]) == [2, 1, 0])
# print(solution(['A', 'A', 'B', 'A'], [20, 20, 20, 30]) == [3, 0, 2])
# print(solution(['A', 'A', 'B', 'A'], [5, 5, 6, 5]) == [0, 1, 2])
# print(solution(['A', 'A', 'B', 'A', 'B', 'B'], [50, 50, 60, 50, 70, 70]) == [4, 5, 0, 1])
# print(solution(['B', 'B', 'B'], [60, 70, 70]) == [1, 2])

print(solution(['a','b','c','d','a','d','d','d','a','a','c','c'],[100,300,400,150,100,300,200,600,700,110,900,9000]))