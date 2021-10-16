import player
# import random
# import time

WARNING_DISTANCE = 40

while True:
    # put your code here, to run repeatedly
    enemies = player.get_trigger()
    # enemies = [{'id': '60', 'coordinates': [4.31, 11.4]},
    #            {'id': '61', 'coordinates': [5.31, 11.4]}]

    numberOfEnemies = len(enemies)
    fireRate = 100/(numberOfEnemies+1)
    player.set_fire_rate(.01)
    player.set_turret_velocity(1000)
    # print('Fire rate adjusted based on #' +
    #       str(numberOFEnemies) + ' to ' + str(fireRate))

    # order based on distance

    if numberOfEnemies == 0:
        # print('reloading ammo')
        player.reload()
    else:
        print('numberOFEnemies: ' + str(numberOfEnemies))

    for enemy in enemies:
        enemyCoordinates = enemy['coordinates']
        distanceToEnemy = player.get_distance_to_coord(enemyCoordinates)
        # distanceToEnemy = random.randint(1, 9)
        enemy['distance'] = distanceToEnemy

    # print(enemies)
    # based on distance
    listOfEnemiesBasedOnDistance = list(
        filter(lambda d: d['distance'] < WARNING_DISTANCE, enemies))
    listOfEnemiesBasedOnDistance = sorted(
        listOfEnemiesBasedOnDistance, key=lambda d: d['distance'])

    print(listOfEnemiesBasedOnDistance)

    player.shoot(False)
    for enemy in listOfEnemiesBasedOnDistance:
        if player.get_ammo() <= 1:
            player.reload()
        enemyCoordinates = enemy['coordinates']
        # print('firing at enemy ' + str(enemy['id']) +
        #   ' on coordinates ' + str(enemyCoordinates) + ' at distance ' + str(enemy['distance']))
        player.aim_at_coordinate(enemyCoordinates)
        player.set_turret_velocity(1)
        player.shoot(True)

    print('next loop')
