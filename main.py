from flask import Flask, render_template
import requests

app = Flask(__name__)

BLOG_ENDPOINT = "https://api.npoint.io/6436b195c044c6b335c9"
api_response = requests.get(url=BLOG_ENDPOINT).json()

@app.route('/')
def home():
    return render_template('/index.html', posts=api_response)


@app.route('/about')
def about():
    return render_template('/about.html')


@app.route('/contact')
def contact():
    return render_template('/contact.html')


@app.route('/post/<nb>')
def post(nb):
    return render_template('/post.html', posts=api_response, num=nb)




if __name__ == "__main__":
    app.run(debug=True)
