from distutils.log import debug
from flask import Flask, render_template, request
from aes import encrypt_result, decrypt_result
from sha512hash import hash_it

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/encrypt", methods=['POST', 'GET'])
def encrypt():
    output = request.form.to_dict()
    plaintext = output["plaintext"]  # name attribute: value
    key = hash_it(output["key"])

    ans = encrypt_result(plaintext, key)
    no_of_rounds = ans["no_of_rounds"]

    cipher = ""
    for i in range(len(ans["blocks"])):
        cipher = cipher + ans[i]["cipher"]

    return render_template("result.html", ans=ans, blocks=len(ans["blocks"]), cipher=cipher, no_of_rounds=no_of_rounds)


@app.route("/decrypt", methods=['POST', 'GET'])
def decrypt():
    output = request.form.to_dict()
    plaintext = output["plaintext"]  # name attribute: value

    key = hash_it(output["key"])

    ans = decrypt_result(plaintext, key)
    no_of_rounds = ans["no_of_rounds"]

    plaintext = ""
    for i in range(len(ans["blocks"])):
        plaintext = plaintext + ans[i]["plaintext"]

    return render_template("result.html", ans=ans, blocks=len(ans["blocks"]), plaintext=plaintext, no_of_rounds=no_of_rounds)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
