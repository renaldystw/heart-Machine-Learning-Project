import pickle
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/heart")
def iris():
    return render_template("heart.html")


@app.route("/klasifikasi", methods=["POST", "GET"])
def hasil():
    if request.method == "POST":
        input = request.form
        age = float(input["age"])
        sex = float(input["sex"])
        cp = float(input["cp"])
        chol = float(input["chol"])
        fbs = float(input["fbs"])
        restecg = float(input["restecg"])
        thalach = float(input["thalach"])
        exang = float(input["exang"])
        oldpeak = float(input["oldpeak"])
        slope = float(input["slope"])
        ca = float(input["ca"])
        thal = float(input["thal"])
        pred = Model.predict(
            [
                [
                    age,
                    sex,
                    cp,
                    chol,
                    fbs,
                    restecg,
                    thalach,
                    exang,
                    oldpeak,
                    slope,
                    ca,
                    thal,
                ]
            ]
        )[0]
        return render_template("hasil.html", data=input, prediksi=pred)


if __name__ == "__main__":
    with open("heartsModel", "rb") as model:
        Model = pickle.load(model)
    app.run(debug=True)


# with open('irisModel','rb') as model:
#     Model = pickle.load(model)

