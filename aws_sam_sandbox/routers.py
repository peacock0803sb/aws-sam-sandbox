from aws_sam_sandbox import app


@app.route("/", methods=["GET"])
def root():
    return {"message": "Hello!"}
