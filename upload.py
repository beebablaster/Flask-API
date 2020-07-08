from flask import Flask, request, render_template
import boto3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['user_file']
    s3 = boto3.resource('s3',aws_access_key_id = 'your access key id',aws_secret_access_key ='your secret access key')

    s3.Bucket('your bucket').put_object(Key=f.filename, Body=request.files['user_file'])

    return '<h1>File saved to S3</h1>'

if __name__ == '__main__':
    app.run(debug=True)
