from flask import Flask

app = Flask(__name__) # 언더바 2개 입니다.

@app.route('/')
def main():
    return '<h1>Hello Flask</h1>'

if __name__ == '__main__': # 언더바 2개 입니다.
    app.run()
