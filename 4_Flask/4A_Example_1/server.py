from flask import Flask  # Import Flask to allow us to create our app
from flask import render_template #adds render template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World! How is it hanging go"/home"?'  # Return the string 'Hello World!' as a response

@app.route('/templates')
def template():
    return render_template("index.html")
@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<phrase>/<int:value>') #Specifying int here means that the route only pushes through if value is an int. otherwise does not recognize route
def profile(phrase,value):
    str(phrase)         #Parse str
    int(value)          #Parse int
    print(phrase)
    request= (phrase *value)
    return request

@app.route('/say/<name>')
def hello(name):
    str(name)
    return "Hello"+name


@app.route('/math/<int:value>/<int:value2>')
def math(value,value2):
    sum=value+value2
    return str(sum)

@app.route('/<path:fail>')
def nope(fail):
    return "Nope"
# @app.route('/repeat/<int:number>/<phrase>')







# @app.route('/home')
# def tester():
#     #database calls will exist at some point
#     friend= "You!!"
#     friends=['One','Two','Three','Four','Five','Six']
#     return render_template('index.html', friend1=friend, friends=friends)

# # import statements, maybe some other routes
    
# @app.route('/dojo')
# def success():
#     return "success"
    




# @app.route('/home/<name>')
# def named_title(name):
#     print(name)
#     return render_template('index.html',friend1=name,friends=['one','two'])

# @app.route('/home/<name>/<int:age>')
# def aged_dashboard(name,age):
#     print(name,age)
#     return render_template('index.html',friend1=name,friends=[])
    

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


