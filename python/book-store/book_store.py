def total(basket):
    basket_count = [basket.count(i) for i in range(1,6)]
    discount_values = [.75,.80,.90,.95,1.]
    result = 0

    for discount in range(len(basket_count)):

        point = basket_count.count(0)

        if (point ==5):
            return int(result)

        if equi(basket_count) == 1 or equi(basket_count) == 2:
            result += discount_values[1] * 800 *(5-1)* 2
            t = 0 if equi(basket_count) == 1 else 2

        else:
            result += discount_values[point] * 800 *(5-point)
            t = 1

        if t == 1:
            for i in range(0,5):
                if basket_count.count(0) == 5:
                    break
                else:
                    basket_count[i] = basket_count[i]-1  if basket_count[i] >= 1 else basket_count[i]
        elif t == 2:
            if basket_count.count(0) == 5:
                    break
            else:
                for i in range(1,3):
                    basket_count[i] = basket_count[i]-1  if basket_count[i] >= 1 else basket_count[i]
                basket_count[0] =basket_count[0]-2
                basket_count[4] =basket_count[4]-2
                basket_count[3] =basket_count[3]-2
        elif t ==0:
            if basket_count.count(0) == 5:
                    break
            else:
                for i in range(0,3):
                    basket_count[i] = basket_count[i]-2  if basket_count[i] >= 2 else basket_count[i]
                basket_count[3] =basket_count[3]-1
                basket_count[4] =basket_count[4]-1

    return int(result)

def equi(cou)->bool:
    if cou[0] == cou[1] and cou[1]==cou[2] and cou[2]==cou[3] and cou[3]==cou[4]:
        return 0

    elif cou[3]>=1 and cou[4] >=1 and cou[3] == cou[4]\
    and cou[0]==cou[1] and cou[1]==cou[2] and cou[0] >=2:
        return 1

    elif cou[1]== cou[2] and cou[1]>=1 and cou[2] >=1\
    and cou[0] == cou[3] and cou[3]==cou[4] and cou[0] >=2:
        return 2

    else:
        return 0
