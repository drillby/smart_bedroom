from turn_pc_on import face_recognition_, wake_on_lan
import json

with open("wol_adresses.json", "r") as file:
    data = json.load(file)

if face_recognition_.recognize():
    wake_on_lan.wol(data["macs"]["ja"], data["broadcast_ip"])
