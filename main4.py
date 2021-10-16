import player


while True:
    # put your code here, to run repeatedly
    enemies = player.get_trigger()

    numberOfEnemies = len(enemies)
    fireRate = 100/(numberOfEnemies+1)
    player.set_fire_rate(fireRate)
    player.set_turret_velocity(1000)
    # print('Fire rate adjusted based on #' +
    #       str(numberOFEnemies) + ' to ' + str(fireRate))

    # order based on distance

    if numberOfEnemies == 0:
        print('reloading ammo')
        player.reload()
    else:
        print('numberOFEnemies: ' + str(numberOfEnemies))

    for enemy in enemies:
        enemyCoordinates = enemy['coordinates']
        distanceToEnemy = player.get_distance_to_coord(enemyCoordinates)
        rayDistance = player.get_ray_distance(enemy['id'])
        enemy['distance'] = distanceToEnemy
        enemy['rayDistance'] = rayDistance

    # print(enemies)
    listOfEnemiesBasedOnDistance = sorted(enemies, key=lambda d: d['distance'])
    print(listOfEnemiesBasedOnDistance)
    # time.sleep(5)
    # player.shoot(False)
    # for enemy in listOfEnemiesBasedOnDistance[:3]:
    #     if player.get_ammo() <= 1:
    #         player.reload()
    #     enemyCoordinates = enemy['coordinates']
    #     print('firing at enemy ' + str(enemy['id']) +
    #           ' on coordinates ' + str(enemyCoordinates) + ' at distance ' + str(enemy['distance']))
    #     player.aim_at_coordinate(enemyCoordinates)
    #     player.shoot(True)

    # print('next loop')
