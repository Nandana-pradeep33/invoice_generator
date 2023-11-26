from flask import Flask, render_template,  request


app = Flask(__name__)
n=''
l=''
@app.route('/', methods=['GET', 'POST'])
def index():
    global n,l

    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        n = name
        l= location
        return render_template('result.html', name=name,location=location)
    
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page2/invoice1')
def invoice1():
    return render_template('lastry.html',name=n,location=l)

if __name__ == '__main__':
    app.run(debug=True)