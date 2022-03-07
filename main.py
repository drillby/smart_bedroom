import json

from face_recog import face_recognition_
from turn_pc_on import wake_on_lan

with open("json/wol_adresses.json", "r") as file:
    data = json.load(file)

if face_recognition_.recognize():
    wake_on_lan.wol(data["macs"]["ja"], data["broadcast_ip"])
