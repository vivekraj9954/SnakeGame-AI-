import urllib
import urllib.request
import numpy as np
import json

def Pre_Sugg_Direction(Left_B,Front_B,Right_B,Cosine_Angle,Collision,Food_x,Food_y,Head_x,Head_y):

    inputVal = ([Left_B, Front_B, Right_B, Cosine_Angle, Collision, Food_x, Food_y, Head_x, Head_y])

    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["Left_B", "Front_B", "Right_B", "Cosine_Angle", "Collision", "Head_x", "Head_y", "Food_x", "Food_y"],
                        "Values": [inputVal]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/5c2c5e3160674c0792f3ab68232b292a/services/9baa3d14fbd1449cacd3951244b4c895/execute?api-version=2.0&details=true'
    api_key = 'sKFeEsFrUpZYH/TlO8TeNP8Nk+rBiseBQXJ15JLgMNpKq6h0CVUoWD0WKbhA9jX3NSqM+2VIDrcAmLoIHNnxxw=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()

        resp_dict = json.loads(result.decode('utf-8'))

        get_score = resp_dict['Results']['output1']['value']['Values']
        score = get_score[0][0]
        score = int(score)

        return(score)

    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read()))


print(Pre_Sugg_Direction(0, 0, 0, 0, 1, 200, 40, 360, 40))




