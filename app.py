from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "Home Page"

    text = "Revisiting the fizzbuzz challenge :)"

    return render_template('home.html', title=title, text=text)

@app.route('/fizzbuzz/<int:n>')
def fizzbuzz(n):

    title = "FizzBuzzing " + str(n)

    fizzbuzz_list=[]

    for number in range(1, n+1):
        fizzbuzz = ""
        if number % 3 == 0:
            fizzbuzz += "Fizz"
        if number % 5 == 0:
            fizzbuzz += "Buzz"
        
        output = fizzbuzz or number
        fizzbuzz_list.append(output)

    return render_template('fizzbuzz.html', title=title, fizzbuzz_list=fizzbuzz_list)


