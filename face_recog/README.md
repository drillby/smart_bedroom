### Face recognition:

- Only usable on Linux machines.
- You need to update turn_on_pc/wol_adresses.json based on your mac address and broadcast IP.
- Also you need to provide your pictures to the turn_on_pc/images folder.
- Run by running the main.py file in turn_pc_on folder.
- You need to provide faces.json file with relative path to img and name of person on the img, formated like this:

```json
{
  "path": ["path1", "path2"],
  "name": ["person1", "person2"]
}
```

For reference you can see faces.json in the json folder.
