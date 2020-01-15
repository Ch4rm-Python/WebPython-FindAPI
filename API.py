import requests
import os
import json
import random
APICode = '''
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>API Arcive</title>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
</head>
<body>

'''
CodeEnd = '''
</body>
</html>
'''

base = 'http://pokeapi.co/api/v2/pokemon/' #Site Used for testing. Can be changed to fit needs
InsertCode = ""
numblock = []
for i in range(9):#the inside of this loop can be changed to find different sublinks 
    num = str(random.randint(1, 9))
    while True:
        if num in numblock:
            num = str(random.randint(1, 9)) 
        else:
            break
    link = base + num +'/'
    req = requests.get(link)
    print(num)
    numblock.append(num)
    json_response = json.loads(req.content) #loading json to get specific bits of json data. req.content is just raw html in bytes. req.text decodes it to a string
    InsertCode = InsertCode + '<a href ="' + link + '">' + str(json_response['name']) + '</a><br>\n' 
homehtml = open("final.html", "w")
homehtml.write(APICode + InsertCode + CodeEnd)
homehtml.close()
    
