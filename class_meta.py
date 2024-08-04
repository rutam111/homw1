class Team:
    def __init__(self, name, participants, coach, captain):
        self.name = name
        self.participants = participants
        self.coach = coach
        self.captain = captain

    def __str__(self):
        return (f"Team: {self.name}, Participants: {self.participants}, "
                f"Coach: {self.coach}, Captain: {self.captain}")

    @staticmethod
    def sort_teams_by_name(teams):
        return sorted(teams, key=lambda team: team.name)

    @staticmethod
    def find_team_by_name(teams, new_team_name):
        for team in teams:
            if team.name == new_team_name:
                return team
        return "No such team found."

teams = [
    Team("Eagles", 11, "John Doe", "Jane Smith"),
    Team("Tigers", 15, "Jim Brown", "Jack Johnson"),
    Team("Lions", 12, "Emily Davis", "Emma Thompson"),
    Team("Panthers", 14, "Alex Green", "Ava White"),
    Team("Bears", 10, "Chris Black", "Chloe Red")
]

sorted_teams = Team.sort_teams_by_name(teams)
for team in sorted_teams:
    print(team)

team_search = Team.find_team_by_name(teams, "Tigers")
print(team_search)
