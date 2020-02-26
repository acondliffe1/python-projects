from pynetgear import Netgear
import config as cfg

netgear = Netgear(host=cfg.host, password=cfg.password)

ignore_devices = cfg.ignore_devices
user_devices = []

attached_devices = netgear.get_attached_devices()

for device in attached_devices:
    if device.mac not in ignore_devices:
        user_devices.append(device.mac)

print(user_devices)
