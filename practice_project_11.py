from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/armastrong/<int:n>")
def armstrong_no(n):
    sum = 0
    order = len(str(n))
    count_n = n
    while(n>0):
        digit = n%10
        sum += digit ** order
        n = n//10
    if (sum == count_n):
        print(f"{count_n} id an armstrong number")
        result = {
            "Number": count_n,
            "Armstrong":True,
            "IP_adrres":"225,224,226,78",
        }
    else:
        print(f"{count_n} id not an armstrong number")
        result = {
            "Number": count_n,
            "Armstrong": False,
            "IP_adrres": "225,224,226,78",
        }
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True)