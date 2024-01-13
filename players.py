import  datetime

class cricketplayer():
    def __init__(self,fname,lname,birth_year,team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []


    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def add_scores(self,score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores)/len(self.scores)

    def __lt__(self, other):
        my_score = self.get_average_score()
        other_score = other.get_average_score()
        return my_score < other_score


    def __str__(self):
        return (f'{self.first_name} {self.last_name} is one of the best cricket player from {self.team} , '
                f'his age is {self.get_age()} and his average score is {self.get_average_score()}')


virat = cricketplayer('virat','kholi',1988,'India')

virat.add_scores(100)
virat.add_scores(80)
virat.add_scores(0)

david = cricketplayer('david','warner',1987,'Australia')

david.add_scores(51)
david.add_scores(37)
david.add_scores(40)

print(f"Virat's average score is : {virat.get_average_score()}")
print(f"Virat's age is : {virat.get_age()}")

print(f"David's average score is : {david.get_average_score()}")
print(f"David's age is : {david.get_age()}")

print(virat<david)
print(virat)
print(david)
