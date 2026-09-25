from flask import Flask,  render_template

app= flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',name="your name")

@app.route('/about')
def about():
    return render_template('about html')

@app.route('/project')
def project():
    my_projects =[
        {"title": "qr code generator","desc": "python app that makes qr code with logos"},
        {"title": "todo app","desc":"coming soon..."}
        ]
    return render_template('project.html', project=my_projects)

if __name__=='__main__':
    app.run(debuge=true)

