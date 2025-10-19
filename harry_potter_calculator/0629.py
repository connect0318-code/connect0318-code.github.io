from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    result = ''
    error = False

    try:
        # 보안을 위해 eval 대신 ast.literal_eval을 사용하거나 직접 파싱하는 것이 좋지만,
        # 간단한 계산기 예제에서는 eval을 사용합니다.
        # 실제 서비스에서는 eval 사용에 주의해야 합니다.
        result = str(eval(expression))
    except Exception as e:
        result = "The magic had failed"
        error = True
        print(f"Error evaluating expression: {e}")

    return jsonify({'result': result, 'error': error})

if __name__ == '__main__':
    app.run(debug=True)