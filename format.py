import player
# import random
# import time

numberOfSpins = 0
toggle10Degrees = False
toggle350Degrees = False
WARNING_DISTANCE = 40


def resetSpin():
    global toggle10Degrees, toggle350Degrees
    toggle10Degrees = False
    toggle350Degrees = False


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


while True:
    # put your code here, to run repeatedly
    getNumberOfSpins(player)

    enemies = player.get_trigger()

    numberOfEnemies = len(enemies)
    fireRate = 100/(numberOfEnemies+1)
    player.set_fire_rate(0.01)
    player.set_turret_velocity(-1000)
    # print('Fire rate adjusted based on #' +
    #       str(numberOFEnemies) + ' to ' + str(fireRate))

    # order based on distance

    if player.get_ammo() < 30 and player.get_turret_heading() > 160 and player.get_turret_heading() < 220:
        # print('reloading ammo')
        player.reload()

    for enemy in enemies:
        enemyCoordinates = enemy['coordinates']
        distanceToEnemy = player.get_distance_to_coord(enemyCoordinates)
        # distanceToEnemy = random.randint(1, 9)
        enemy['distance'] = distanceToEnemy

    # print(enemies)

    if numberOfSpins > 30:
        listOfEnemiesBasedOnDistance = list(
            filter(lambda d: d['distance'] < WARNING_DISTANCE, enemies))
    else:
        listOfEnemiesBasedOnDistance = sorted(
            enemies, key=lambda d: d['distance'])

    # print(listOfEnemiesBasedOnDistance)
    # time.sleep(5)
    player.shoot(False)

    if len(listOfEnemiesBasedOnDistance) == 1:
        player.set_turret_velocity(0)
        player.set_fire_rate(0.01)

    for enemy in listOfEnemiesBasedOnDistance[:3]:
        player.set_turret_velocity(2)
        if player.get_ammo() == 0:
            player.reload()
        enemyCoordinates = enemy['coordinates']
        # print('firing at enemy ' + str(enemy['id']) +
        #       ' on coordinates ' + str(enemyCoordinates) + ' at distance ' + str(enemy['distance']))
        player.aim_at_coordinate(enemyCoordinates)
        player.shoot(True)

    # print('next loop')
