from prepare_img import run as prepare_img
from evaluate import run as evaluate

from flask import Flask, request, jsonify
from models import easy, quality_validator

app = Flask(__name__)


@app.route("/", methods=["POST"])
def upload():
    data = request.get_json() # get Json data with: ("name","id","imgb64")

    #Get Img
    img_b64 = data.get("image")
    #Function input: imgb64 output: binary img with modifications
    img = prepare_img(img_b64)
        
    #Get Name
    input_name = data.get("name")
    
    #Get ID
    input_id = data.get("id")
    
    img_results = quality_validator.run(img)
    
    if img_results["ImgIsOK?"]:
        #Function input: binary-img output: String result of Optical Character Recognition
        result = easy.reader(img)

        #Function input: Lists of result and input Json output: Boolean value if the Lists elements match
        value = evaluate(input_name, input_id, result)

        #Create a object with the finally information to return
        output = {"isOk": value, "imgIsOk": img_results["ImgIsOK?"], "img_reults":img_results, "result": result}

        return jsonify(output)
    else:
        return jsonify(img_results)


if __name__ == "__main__":
    app.run(debug=True, port=2809, host="0.0.0.0")
