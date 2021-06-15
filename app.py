from flask import Flask, jsonify
from fibo import fibo, fi_sum

app = Flask(__name__)


@app.route('/fibonacci/<number>')
def fibonacci(number):
    res = fibo(number)
    return jsonify({"Fibonacci": res})


@app.route('/sum/<number>')
def fibonacci_sum(number):
    res_sum = fi_sum(number)
    return jsonify({"Fibonacci_sum": res_sum})


if __name__ == '__main__':
    app.run()
