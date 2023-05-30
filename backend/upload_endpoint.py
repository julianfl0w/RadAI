from flask import Flask, request, jsonify

app = Flask(__name__)
import secrets
import string
import shutil


def generate_random_string(length=20):
    characters = string.ascii_letters + string.digits
    random_string = "".join(secrets.choice(characters) for _ in range(length))
    return random_string


@app.route("/upload", methods=["POST", "OPTIONS"])
def upload():
    print(request.method)
    if request.method == "OPTIONS":
        # Handle OPTIONS request for cross-origin requests
        response = app.make_default_options_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "POST"
        return response

    if "file" not in request.files:
        return "No file uploaded."

    file = request.files["file"]

    if file.filename == "":
        return "No file selected."

    print("Received")
    # print(request.json())
    file = request.files.get("file")

    if file:
        # Handle the uploaded file here
        # You can save it, process it, etc.
        ret = "File uploaded successfully."
        newFileName = "/mnt/tmpfs/" + generate_random_string()
        # Save the file with the desired name
        file.save(newFileName)
        # with open(newFileName, 'wb+') as f:
        #    shutil.copyfileobj(file, f)

    else:
        ret = "No file uploaded."
    print(ret)
    return ret


if __name__ == "__main__":
    app.run(port=8082)
