from flask import Flask,request

app = Flask(__name__)

@app.route('/BMI', methods=['POST'])
def BMI():
    req = request.json
    height = float(request.form.get("height"))
    weight = float(request.form.get("weight"))

    BMI = weight / (height/100)**2
    if BMI <= 18.5:
        hasil = "KURUS"
    elif BMI <= 25:
        hasil = "SEHAT"
    elif BMI <= 40:
        hasil = "BERLEBIHAN"
    else:
        hasil = "OBESITAS"
    data = {'Score BMI': BMI,'Tergolong': hasil}
    return data

if __name__ == '__main__':
    app.run(debug=True, port=4000)
