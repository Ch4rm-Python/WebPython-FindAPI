import requests
import numpy
import os
import json
import random
APICode = '''
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Google Docs Arcive</title>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
</head>
<body>

'''
CodeEnd = '''
</body>
</html>
'''
base = 'http://pokeapi.co/api/v2/pokemon/'
APCode = ""
numblock = []
for i in range(9):  
    num = str(random.randint(1, 9))
    while True:
        if num in numblock:
            num = str(random.randint(1, 9))
        else:
            break
    link = 'http://pokeapi.co/api/v2/pokemon/' + num +'/'
    req = requests.get(link)
    print(num)
    numblock.append(num)
    json_response = json.loads(req.content)
    APCode = APCode + '<a href ="' + link + '">' + str(json_response['name']) + '</a><br>\n'
homehtml = open("final.html", "w")
homehtml.write(APICode + APCode + CodeEnd)
homehtml.close()
    
