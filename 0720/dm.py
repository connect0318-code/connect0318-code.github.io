from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def draco_malfoy_page():
    # 드레이코 말포이에 대한 정보를 딕셔너리 형태로 준비합니다.
    draco_info = {
        'name': '드레이코 말포이 (Draco Malfoy)',
        'house': '슬리데린',
        'family': '말포이 가문 (순수 혈통)',
        'description': '드레이코 말포이는 해리 포터 시리즈의 주요 안타고니스트 중 한 명입니다. '
        '그는 호그와트의 슬리데린 기숙사 학생이며, 순수 혈통주의를 맹신하는 부유한 마법사 가문인 말포이 가문의 외아들입니다. '
        '초기에는 해리 포터와 적대적인 관계였으나, 시리즈 후반으로 갈수록 내면적인 갈등을 겪으며 복잡한 인물로 성장합니다.',
        'key_events': [
            '호그와트 입학 후 해리 포터와 지속적인 갈등',
            '엄브릿지 교수 휘하에서 심문관으로 활동',
            '죽음을 먹는 자가 되어 볼드모트의 임무 수행 (덤블도어 살해 지시)',
            '말포이 저택에서 해리 일행의 정체 숨겨줌',
            '호그와트 전투에서 망설이는 모습',
            '전쟁 후 아스토리아 그린그래스와 결혼 및 스코피어스 말포이 출산']
        ,
        'image_url': 'https://mblogthumb-phinf.pstatic.net/MjAyMTAxMTNfMjc0/MDAxNjEwNTEyODc1MTg2.cR2Yk0S4mfe8SN7kfWzklLRPvT-S5v6PdmO7gOJP0wog.zcqHRTwMrEdImviPgvzO2YCY9LJOjUqkl_8bKG1yuogg.GIF.tjdusdn33/image_632134750.gif?type=w800'
        }
    return render_template('draco_malfoy.html', draco=draco_info)

if __name__ == '__main__':
    app.run(debug=True)