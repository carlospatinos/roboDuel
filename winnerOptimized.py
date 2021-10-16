import player
# import random
# import time


while True:
    # put your code here, to run repeatedly
    enemies = player.get_trigger()
    # enemies = [{'id': '60', 'coordinates': [4.31, 11.4]},
    #            {'id': '61', 'coordinates': [5.31, 11.4]}]

    numberOfEnemies = len(enemies)
    fireRate = 100/(numberOfEnemies+1)
    player.set_fire_rate(0.01)
    player.set_turret_velocity(1000)
    # print('Fire rate adjusted based on #' +
    #       str(numberOFEnemies) + ' to ' + str(fireRate))

    # order based on distance

    if numberOfEnemies == 0 and player.get_ammo() < 30:
        # print('reloading ammo')
        player.reload()

    for enemy in enemies:
        enemyCoordinates = enemy['coordinates']
        distanceToEnemy = player.get_distance_to_coord(enemyCoordinates)
        # distanceToEnemy = random.randint(1, 9)
        enemy['distance'] = distanceToEnemy

    # print(enemies)
    listOfEnemiesBasedOnDistance = sorted(enemies, key=lambda d: d['distance'])
    # print(listOfEnemiesBasedOnDistance)
    # time.sleep(5)
    player.shoot(False)

    if len(listOfEnemiesBasedOnDistance) == 1:
        player.set_turret_velocity(0)
        player.set_fire_rate(0.01)

    for enemy in listOfEnemiesBasedOnDistance[:3]:
        if player.get_ammo() == 0:
            player.reload()
        enemyCoordinates = enemy['coordinates']
        print('firing at enemy ' + str(enemy['id']) +
              ' on coordinates ' + str(enemyCoordinates) + ' at distance ' + str(enemy['distance']))
        player.aim_at_coordinate(enemyCoordinates)
        player.shoot(True)

    # print('next loop')
