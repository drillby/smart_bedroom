import json

from face_recog import face_recognition_
from wake_on_lan.wol import WakeOnLAN

with open("json/wol_adresses.json", "r") as file:
    data = json.load(file)

if face_recognition_.recognize():
    WakeOnLAN.send_magic_packet(data["macs"]["ja"])
