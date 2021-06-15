from flask import Flask, jsonify
from fibo import fibo, fi_sum

app = Flask(__name__)


@app.route('/<number>')
def fibonacci(number):
    res = fibo(number)
    res_sum = fi_sum(number)
    return jsonify({"Fibo": res, "Fibo_sum": res_sum})


if __name__ == '__main__':
    app.run()
