import player

from playerFile import playerClass
player = playerClass()

numberOfSpins = 0
toggle10Degrees = False
toggle350Degrees = False

listOfEnemies360 = []


def fire():
    global listOfEnemies360
    print("firing at " + str(len(listOfEnemies360)))
    print("listOfEnemies360: " + str(listOfEnemies360))

    for enemy in listOfEnemies360:
        enemyCoordinates = enemy['coordinates']
        distanceToEnemy = player.get_distance_to_coord(enemyCoordinates)
        enemy['distance'] = distanceToEnemy
    listOfEnemies360 = sorted(
        listOfEnemies360, key=lambda d: d['distance'])

    for enemy in listOfEnemies360:
        if player.get_ammo() == 0:
            player.reload()
        enemyCoordinates = enemy['coordinates']
        print('firing at enemy ' + str(enemy['id']) +
              ' on coordinates ' + str(enemyCoordinates) + ' at distance ' + str(enemy['distance']))
        player.aim_at_coordinate(enemyCoordinates)
        player.set_turret_velocity(1)
        player.shoot(True)

    del listOfEnemies360[:]


def infoGathering(player):
    print("info gathering")
    enemies = player.get_trigger()
    listOfEnemies360.extend(enemies)


def reload(player):
    torretHeading = player.get_turret_heading()
    if (player.get_ammo() and (torretHeading >= 130 or torretHeading <= 230)) or player.get_ammo() == 0:
        player.reload()


def moveTurrret(player):
    player.set_turret_velocity(-100)
    # print("--> " + str(player.get_turret_heading()))


def getNumberOfSpins(player):
    global toggle10Degrees, toggle350Degrees, numberOfSpins
    if (not toggle10Degrees) and player.get_turret_heading() > 20 and player.get_turret_heading() < 30:
        print("10 degrees passed")
        toggle10Degrees = True
    if (not toggle350Degrees) and toggle10Degrees and player.get_turret_heading() > 355:
        print("350 degrees passed")
        toggle350Degrees = True
    if toggle10Degrees and toggle350Degrees:
        numberOfSpins = numberOfSpins + 1
        resetSpin()
    return numberOfSpins


def resetSpin():
    global toggle10Degrees, toggle350Degrees
    toggle10Degrees = False
    toggle350Degrees = False


while True:
    player.set_fire_rate(.01)
    player.set_turret_velocity(1000)
    moveTurrret(player)
    print()
    # based on torret position
    # 0 gather, 1 fire
    if getNumberOfSpins(player) % 2 == 0:
        infoGathering(player)
    else:
        fire()
