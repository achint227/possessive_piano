from collections import defaultdict


def fullAttendance(teams, attendees):
    
    team_members=defaultdict(set)


    def resolve(candidate):
        if candidate in teams:
            if not team_members[candidate]:
                for member in teams[candidate]:
                    team_members[candidate].update(resolve(member))
            return team_members[candidate]
        return set([candidate])
    
    for team in teams:
        resolve(team)
    
    res=[]

    for team in team_members:
        if team_members[team].issubset(attendees):
            res.append(team)
    return res


if __name__ == "__main__":
    teams = {
        "Hooters": ["Thunders", "Tim"],
        "Sharks": ["Hooters", "Ronan"],
        "Thunders": ["Drew", "Candace"],
    }
    attendees = {"Tim", "Drew", "Candace"}

    print(fullAttendance(teams, attendees))
