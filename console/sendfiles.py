from pip._vendor import requests

try:
    while True:
        s = input("Do you want to send file to server? y / n: ")
    
        if(s == "n"):
            print("Exiting...")
            break
        if(s != "y"):
            print("Sorry, try again!")
            continue
    
        full_filepath = input("Insert file path: ")

        url = 'http://localhost:8000/uploadArticle/'
        files = {'file': open(full_filepath, 'rb')}
        r = requests.post(url, files=files)
except Exception as e:
    print(e)