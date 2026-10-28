from flask import Flask, render_template_string, request

app = Flask(__name__)

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("Division by zero is not allowed.")
    return a / b

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Kubernetes Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; background: #f4f4f9; text-align: center; }
        .calc-box { background: white; padding: 30px; border-radius: 10px; display: inline-block; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        input, select, button { margin: 10px; padding: 10px; font-size: 16px; }
        button { background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="calc-box">
        <h2>📊 Menu-Driven Calculator</h2>
        <form method="POST">
            <input type="number" step="any" name="num1" placeholder="First Number" required>
            <select name="operation">
                <option value="1">Addition (+)</option>
                <option value="2">Subtraction (-)</option>
                <option value="3">Multiplication (*)</option>
                <option value="4">Division (/)</option>
            </select>
            <input type="number" step="any" name="num2" placeholder="Second Number" required>
            <br>
            <button type="submit">Calculate</button>
        </form>
        {% if result is not none %}
            <h3>Result: {{ result }}</h3>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["operation"]
            
            if op == "1": result = add(num1, num2)
            elif op == "2": result = subtract(num1, num2)
            elif op == "3": result = multiply(num1, num2)
            elif op == "4": result = divide(num1, num2)
        except Exception as e:
            result = str(e)
            
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    # Runs the web app on port 8080 across all available network interfaces
    app.run(host="0.0.0.0", port=8080)
