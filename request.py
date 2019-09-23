import requests
import json

# URL
url = 'zmahsyari.pythonanywhere.com/api'

# Change the value of experience that you want to test
r=requests.post(url,json=[{"PAY_1":2,"PAY_2":2,"LIMIT_BAL":20000},
                            {"PAY_1":1,"PAY_2":0,"LIMIT_BAL":30000},
                            {"PAY_1":0,"PAY_2":0,"LIMIT_BAL":40000},
                            {"PAY_1":1,"PAY_2":0,"LIMIT_BAL":70000},
                            {"PAY_1":1,"PAY_2":0,"LIMIT_BAL":180000},
                            {"PAY_1":1,"PAY_2":1,"LIMIT_BAL":30000},
                            {"PAY_1":2,"PAY_2":1,"LIMIT_BAL":25000},
                            {"PAY_1":1,"PAY_2":3,"LIMIT_BAL":47000},
                            {"PAY_1":1,"PAY_2":2,"LIMIT_BAL":60900},
                            {"PAY_1":0,"PAY_2":1,"LIMIT_BAL":70000}])
print(r.json())