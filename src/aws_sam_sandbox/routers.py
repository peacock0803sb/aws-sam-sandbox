from aws_sam_sandbox.initilizer import app


@app.route("/", methods=["GET"])
def root():
    return {"message": "Hello!"}
