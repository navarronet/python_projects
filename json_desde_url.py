import urllib.request, json

with urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts") as json_url:
    datos = json.loads(json_url.read().decode())
    # print(datos)
    print(json.dumps(datos, indent=4, sort_keys=True))