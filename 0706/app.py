from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_super_secret_key' # 실제 운영 환경에서는 더 복잡한 키를 사용하세요.

# 간단한 사용자 ID/PW (실제로는 데이터베이스를 사용해야 합니다)
USERS = {
    "harry": "potter",
    "hermione": "granger"
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS and USERS[username] == password:
            flash(f"Welcome to Hogwarts, {username.capitalize()}!", 'success')
            return redirect(url_for('magic_world'))
        else:
            flash('Incorrect username or password. Try again!', 'danger')
    return render_template('login.html')

@app.route('/magic_world')
def magic_world():
    # 로그인이 성공했을 때 보여줄 페이지입니다.
    # 이 페이지는 단순히 환영 메시지를 보여줍니다.
    return render_template('hello.html') # 이 파일도 필요하다면 만들어 드립니다.

@app.route('/logout')
def logout():
    flash('You have left the magic world.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True) # 개발 중에는 debug=True로 설정하여 코드 변경 시 자동 재시작되게 합니다.