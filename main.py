import random


def play(runs, switch=False):
    wins = 0
    losses = 0
    for attempt in range(runs):
        doors = [0 for x in range(3)]
        doors[random.randint(0, 2)] = 1
        chosen = random.randint(0, 2)
        value = doors[chosen]
        goats = [num for num, door in enumerate(doors) if door != 1 and num != chosen]
        doors.pop(random.choice(goats))
        if switch:
            value = [door for door in doors if door != value][0]
        if value == 1:
            wins += 1
        else:
            losses += 1
    print(f"wins: {wins}")
    print(f"losses: {losses}")
    print(f"{round(((wins / (wins + losses)) * 100))}%")


def main():
    runs = 10000
    play(runs)
    play(runs, True)


if __name__ == '__main__':
    main()
