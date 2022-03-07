### Wake on LAN:

- It is nessesary to enable WoL function in your BIOS and OS settings.
- File is in the turn_on_pc folder.
- You need to provide wol_adresses.json file with your broadcast IP and MAC addresses, formated like this:

```json
{
  "broadcast_ip": "ip",
  "macs": {
    "name": "mac"
  }
}
```

For reference you can see wol_adresses.json in the json folder.
