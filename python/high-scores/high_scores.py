def latest(scores):
    #一番最後の数を引き値
    return scores[-1]

def personal_best(scores):
    # 最大値を引き値
    return max(scores)

def personal_top_three(scores):
    # 点数が高い順に左から並べる
    if len(scores) < 3:
        return sorted(scores,reverse = True)
    else:
        return sorted(scores,reverse = True)[:3]
