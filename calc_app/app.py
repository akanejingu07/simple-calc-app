from flask import Flask, render_template, request
# Flask 本体、画面表示用の render_template、
# フォームデータを受け取る request を読み込む

app = Flask(__name__)
# Flask アプリを作るおまじない

@app.route("/", methods=["GET", "POST"])
# "/"（トップページ）で GET/POST の両方を受け取る

def index():
    result = None  # 最初は計算結果なし

    if request.method == "POST":
        # ボタンが押されて POST されたとき

        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        # フォームから受け取った文字を数値に変換

        operator = request.form["operator"]
        # どの演算子（＋ ー × ÷）が選ばれたか取得

        if operator == "add":
            result = num1 + num2
        elif operator == "sub":
            result = num1 - num2
        elif operator == "mul":
            result = num1 * num2
        elif operator == "div":
            # 0で割られた場合をエラー防止
            result = "エラー:0で割ることはできません" if num2 == 0 else num1 / num2

    return render_template("index.html", result=result)
    # HTML に結果を渡して表示する