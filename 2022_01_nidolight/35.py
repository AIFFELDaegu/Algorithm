def solution(brown, yellow):
    b = 2+brown/2
    c = brown+yellow
    
    x = (b + (b**2 - 4*c)**(1/2)) / 2

    return [x, c/x]


print(solution(10,2))

    # brown = 2*x + 2*(y-2) = 2(x+y-2)
    # x+y-2-brown/2 = 0

    # brown+yellow = x*y
    # y = (brown+yellow)/x

    # x+(brown+yellow)-2-brown/2 = 0
    # x^2 -(2+brown/2)*x + brown+yellow = 0

    # x = (2+brown/2 + ((2+brown/2)^2 - 4(brown+yellow))^1/2) / 2 #음의 경우 xy값이 반대

    


