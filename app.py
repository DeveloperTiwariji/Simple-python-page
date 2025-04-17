from flask import Flask, render_template_string

app = Flak(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Radhe Radhe</title>
    <style>
        body {
            background: linear-gradient(to right, #ffecd2, #fcb69f);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        h1 {
            color: #d6336c;
            font-size: 4rem;
            text-shadow: 2px 2px #fff;
        }
    </style>
</head>
<body>
    <h1>🙏 Radhe Radhe 🙏</h1>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True)
