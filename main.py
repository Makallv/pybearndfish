from World.Bear import Fish, Planet, Bear, random
import time


def main():
    """
       Create some fish and bears, have the bears eat the fish and perform various actions,
       and print the number of fish in the world and the number of alive bears. Create also planet
       """
    # create some fish
    fish1 = Fish("trout", 10, 10000)  # there are 10000 trout in the world
    fish2 = Fish("salmon", 15, 10000)  # there are 10000 salmon in the world
    fish3 = Fish("catfish", 10, 10000)  # there are 10000 catfish in the world
    fish4 = Fish("Red snapper", 20, 10000)  # there are 10000 Red snappers in the world
    fish5 = Fish("Bass", 12)  # there are 10000 bass in the world
    fish6 = Fish("Tuna", 30)  # there are 10000 tuna fish in the world
    fish7 = Fish("walleye", 14)  # there are 10000 walleye fish in the world
    fish8 = Fish("swordfish", 36)  # there are 10000 swordfish fish in the world
    fish9 = Fish("grouper", 18)  # there are 10000 grouper fish in the world
    fish10 = Fish("snook", 22)  # there are 10000 snook fish in the world  # NOQA

    # create some bears%%
    bear1 = Bear("Yogi", 100, 0, "male")
    bear2 = Bear("Pooh", 50, 0, "female")
    bear3 = Bear("Grizzly", 80, 0, "male")
    bear4 = Bear("Panda", 75, 0, "female")
    bear5 = Bear("Kodiak", 90, 0, "male")
    bear6 = Bear("Baloo", 85, 0, "male")
    bear7 = Bear("Honey", 95, 0, "female")
    bear8 = Bear("BamBam", 60, 0, "male")
    bear9 = Bear("Smokey", 65, 0, "male")
    bear10 = Bear("BooBoo", 70, 0, "male")

    i = 0  # 10 ticks are gonna happen

    # bears actions
    while i < 10:
        for bear in Bear.ALIVE_BEARS:
            action = random.randint(1, 3)
            bear.check_energy()
            if action == 3:
                while bear.starvation < 100 and Fish.FISH_COUNT < 0:
                    x = random.randint(0, len(Fish.FISH_LIST) - 1)
                    random_fish = Fish.FISH_LIST[x]
                    bear.eat(random_fish)
            else:
                Bear.random_action(bear, action)
            bear.check_energy()
            time.sleep(10)
        i += 1

    # print the number of fish in the world
    print(f"Number of fish in the world: {Fish.FISH_COUNT}")

    # print the number of alive bears
    print(f"Number of alive bears: {len(Bear.ALIVE_BEARS)}")

    # print the alive bears
    for bear in Bear.ALIVE_BEARS:
        text2 = f" it's starvation level is {bear.starvation} "
        text1 = f"{bear.name} is alive with {bear.energy} remaining in it's tank and"
        text = text1 + text2
        for char in text:
            print(char, end="")
            time.sleep(1)
    # print the number of dead bears if there are any
    if len(Bear.DEAD_BEARS) > 0:
        for bear in Bear.DEAD_BEARS:
            text = f"{bear.name} has died"

    # create a planet
    earth = Planet("Earth", 29.1, 70.9)

    # calculate the total area of the planet
    total_area = earth.total_area()
    print(f"Total area of {earth.name}: {total_area}")


if __name__ == '__main__':
    """Check for imported or script"""
    main()
