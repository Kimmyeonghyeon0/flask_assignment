from flask import Flask, request, Response
import test

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is Main Page!"

# Alt + shift + 화살표 위/아래
@app.route('/about')
def about():
    return "This is the about page!"

#동적으로 URL 파라미터 값을 받아서 처리해준다
@app.route('/user/<username>')
def user_profile(username):
    return f'UserName : {username}'

@app.route('/number/<int:number>')
def numbers(number):
    return f'Number : {number}'

#post 요청 날리는 방법
# (1) postman
# (2) requests
import requests #pip install requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)

    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELEATE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")

    if request.method == 'POST':
        print("***POST method***", request.data)

    return Response("Sucessfully submitted", status=200)

if __name__ == "__main__":
    app.run()
