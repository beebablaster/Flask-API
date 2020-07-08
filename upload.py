from flask import Flask, request, render_template
import boto3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['user_file']
    s3 = boto3.resource('s3',aws_access_key_id = 'AKIAJDJEGHMZU7W2SHKQ',aws_secret_access_key = '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')

    s3.Bucket('beebablaster').put_object(Key=f.filename, Body=request.files['user_file'])

    return '<h1>File saved to S3</h1>'

if __name__ == '__main__':
    app.run(debug=True)
