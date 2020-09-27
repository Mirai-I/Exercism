def tally(rows):
    membre_info = [i.split(';') for i in rows]

    membre_name = [i[:2] for i in membre_info]
    membre_name = set(sum(membre_name,[]))
    membre_name = sorted(membre_name)

    player, place =[],[]
    player +=[{"name":i, "MP":0, "W":0, "D":0, "L":0, "P":0} for i in membre_name]

    for info in membre_info:
        place += [[i for i, personne in enumerate(membre_name) if personne in info]]

    for i in range(len(place)):
#    membre_info[i], player[personne[0]], player[personne[1]])
        if membre_info[i][2] == "win":
            if player[place[i][0]]["name"] == membre_info[i][0]:
                player[place[i][0]]["W"] += 1
                player[place[i][0]]["P"] += 3
                player[place[i][1]]["L"] += 1
            else:
                player[place[i][1]]["W"] += 1
                player[place[i][1]]["P"] += 3
                player[place[i][0]]["L"] += 1

        elif membre_info[i][2] == "draw":
            player[place[i][0]]["D"] += 1
            player[place[i][1]]["D"] += 1
            player[place[i][0]]["P"] += 1
            player[place[i][1]]["P"] += 1

        else:
            if player[place[i][0]]["name"] == membre_info[i][0]:
                player[place[i][0]]["L"] += 1
                player[place[i][1]]["P"] += 3
                player[place[i][1]]["W"] += 1
            else:
                player[place[i][1]]["L"] += 1
                player[place[i][0]]["P"] += 3
                player[place[i][0]]["W"] += 1

        player[place[i][0]]["MP"] += 1
        player[place[i][1]]["MP"] += 1

    result = sorted(player, key=lambda x:x["P"], reverse=True)
    result.insert(0,{"name":"Team", "MP":"MP", "W":"W", "D":"D", "L":"L", "P":"P"})

    conclu = ["{0:<24}       | {1:^3}|  {2:} |  {3:} |  {4:} |  {5:}".format(i["name"],i["MP"],i["W"],i["D"],i["L"],i["P"]) for i in result]
    return conclu
