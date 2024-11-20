class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            maxdistance = 0
            for participant in self.participants:  # отдельный цикл для пробежки за единицу времени для всех
                participant.run()
                if participant.distance > maxdistance:
                    maxdistance = participant.distance  # запоминаем кто дальше убежал

            for participant in self.participants:
                if participant.distance >= self.full_distance and participant.distance == maxdistance:  # плюс условие
                    # с этим небольшим условием тот, кто медленнее, не займет первое место, если его первым проверят.
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
