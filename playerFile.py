
debug = False


class playerClass:
    ammo = 30

    def get_turret_heading(self):
        return 0

    def get_trigger(self):
        if debug:
            print("get trigger")
        return [{'id': '60', 'coordinates': [4.31, 11.4]}, {'id': '61', 'coordinates': [5.31, 11.4]}]

    def reload(self):
        if debug:
            print('reloading ammo')
        ammo = 30

    def shoot(self):
        ammo = ammo - 1
