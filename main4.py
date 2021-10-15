import player
# import random
# import time


while True:
    minDistance = 1000
    # put your code here, to run repeatedly
    enemies = player.get_trigger()
    bullets = player.get_ammo()
    numberOfEnemies = len(enemies)
    fireRate = 1  # 100/(numberOfEnemies+1)
    player.set_fire_rate(fireRate)
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
        rayDistance = player.get_ray_distance(enemy['id'])
        enemyCoordinates = enemy['coordinates']
        distanceToEnemy = player.get_distance_to_coord(enemyCoordinates)
        # distanceToEnemy = random.randint(1, 9)
        enemy['distance'] = distanceToEnemy
        if distanceToEnemy < minDistance:
            minDistance = distanceToEnemy
        enemy['rayDistance'] = rayDistance

    if minDistance > 45:
        continue

    listOfEnemiesBasedOnDistance = sorted(enemies, key=lambda d: d['distance'])
    print(enemies)
    print('bullets:' + str(bullets) + ' numberOfEnemies:' +
          str(numberOfEnemies) + ' minDistance: ' + str(minDistance))

    player.shoot(False)
    for enemy in listOfEnemiesBasedOnDistance[:3]:
        if player.get_ammo() <= 1:
            player.reload()
        enemyCoordinates = enemy['coordinates']
        print('firing at enemy ' + str(enemy['id']) +
              ' on coordinates ' + str(enemyCoordinates) + ' at distance ' + str(enemy['distance']) + ' at ray distance rayDistance ' + str(enemy['rayDistance']))
        player.aim_at_coordinate(enemyCoordinates)
        player.shoot(True)

    print('next loop')
