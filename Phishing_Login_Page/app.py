from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        return redirect(f"/user={username}&pass={password}")

    return render_template_string('''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
        }
        form {
            width: 300px;
        }
        .fieldLabel {
            font-size: 14px;
            color: #333333;
            margin-bottom: 5px;
        }
        .login_input input {
            width: 100%;
            padding: 10px 0;
            font-size: 14px;
            color: #333333;
            background-color: #f2f2f2;
            border: none;
            outline: none;
            border-bottom: 1px solid #cccccc;
            margin-bottom: 20px;
        }
        .login_input input:focus {
            border-bottom: 1px solid #333333;
        }
        .memberButton {
            width: 100%;
            padding: 10px 0;
            font-size: 14px;
            font-weight: bold;
            color: #ffffff;
            background-color: #333333;
            border: none;
            cursor: pointer;
            text-align: center;
            display: inline-block;
        }
        .memberButton:hover {
            background-color: #555555;
        }
        .marginTop {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <form action="/" method="post">
        <div class="fieldLabel">ID Anggota</div>
        <div class="login_input">
            <input type="text" name="username">
        </div>
        <div class="fieldLabel marginTop">Kata Sandi</div>
        <div class="login_input">
            <input type="password" name="password">
        </div>
        <button type="submit" class="memberButton">Masuk</button>
    </form>
</body>
</html>
    ''')

@app.route('/user=<username>&pass=<password>')
def show_user_pass(username, password):
    return f"User: {username}, Pass: {password}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
