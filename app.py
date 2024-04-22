# 깃으로 먼저 등록을 한다
print("Hello World!!")

from flask import Flask

app = Flask(__name__)##내장변수를 넣고 
if __name__=="__main__":## app을 전달받은 다음 
    app.run() ##실행시켜보자
