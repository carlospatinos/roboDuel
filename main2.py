# optimizaion de mmnia distancia para recargar

import player
# import random
# import time

SAFE_DISTANCE = 40
while True:
    # put your code here, to run repeatedly
    enemies = player.get_trigger()
    # enemies = [{'id': '60', 'coordinates': [4.31, 11.4]},
    #            {'id': '61', 'coordinates': [5.31, 11.4]}]

    numberOfEnemies = len(enemies)
    bullets = player.get_ammo()
    fireRate = 100/(numberOfEnemies+1)
    player.set_fire_rate(fireRate)
    player.set_turret_velocity(1000)
    # print('Fire rate adjusted based on #' +
    #       str(numberOFEnemies) + ' to ' + str(fireRate))

    minDistance = 1000
    for enemy in enemies:
        enemyCoordinates = enemy['coordinates']
        distanceToEnemy = player.get_distance_to_coord(enemyCoordinates)
        # distanceToEnemy = random.randint(1, 9)
        enemy['distance'] = distanceToEnemy
        if distanceToEnemy < minDistance:
            minDistance = distanceToEnemy

    print('bullets:' + str(bullets) + ' numberOfEnemies:' +
          str(numberOfEnemies) + ' minDistance: ' + str(minDistance))
    if (bullets < 30 and (numberOfEnemies == 0 or minDistance >= SAFE_DISTANCE)):
        print('reloading ammo')
        player.reload()
    # else:
    #     print('numberOFEnemies: ' + str(numberOfEnemies))

    # print(enemies)
        # TODO create a list with the closest enemies? less than 20 ?
    listOfEnemiesBasedOnDistance = sorted(enemies, key=lambda d: d['distance'])
    # print(listOfEnemiesBasedOnDistance)
    # time.sleep(5)
    player.shoot(False)
    for enemy in listOfEnemiesBasedOnDistance[:3]:
        if bullets <= 1:
            player.reload()
        enemyCoordinates = enemy['coordinates']
        print('firing at enemy ' + str(enemy['id']) +
              ' on coordinates ' + str(enemyCoordinates) + ' at distance ' + str(enemy['distance']))
        player.aim_at_coordinate(enemyCoordinates)
        player.shoot(True)

    # print('next loop')
