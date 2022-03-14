def solution(tickets):
    tickets.sort(key=lambda x: x[1])  # 뒤에꺼 기준 정렬
    answer = [t for t in tickets if t[0] == "ICN"][0]
    tickets.remove(answer)
    selected_tickets = []

    def recursive(tickets):
        # print("answer: {}\ntickets: {}\nselected:{}\n".format(answer,tickets,selected))
        if not tickets:  # tickets가 비어있으면 종료
            return
        for i, t in enumerate(tickets):
            if answer[-1] == t[0]:
                answer.append(tickets.pop(i)[1])
                break
            # 티켓이 남는다면(더이상 진행이 안되는 경우)
            # answer의 마지막 하나 빼고 다른 티켓으로 진행
            elif i == len(tickets)-1:
                selected_tickets.append([answer[-2], answer.pop(-1)])
        return recursive(tickets)

    recursive(tickets)
    if selected_tickets:  # 남은 티켓들 마저 선택
        recursive(selected_tickets)

    return answer


print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], [
      "BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

'''
테스트 케이스 예시
https://programmers.co.kr/questions/18184
'''
