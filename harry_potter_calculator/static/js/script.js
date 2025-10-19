document.addEventListener('DOMContentLoaded', () => {
    const display = document.getElementById('display');
    // 오디오 요소 가져오기
    const backgroundMusic = document.getElementById('background-music');
    const spellSound = document.getElementById('spell-sound');

    let currentExpression = '';
    let resultDisplayed = false;

    // 배경 음악 자동 재생 시도 (사용자 상호작용 필요)
    // 브라우저 정책상 사용자 상호작용(클릭 등)이 있어야 오디오가 재생될 수 있습니다.
    // 따라서 페이지 로드 시 바로 재생이 안 될 수 있습니다.
    // body를 클릭하면 음악이 재생되도록 설정합니다.
    backgroundMusic.volume = 0.3; // 볼륨 조절 (0.0 ~ 1.0)
    document.body.addEventListener('click', () => {
        if (backgroundMusic.paused) {
            backgroundMusic.play().catch(e => console.log("배경 음악 재생 실패:", e));
        }
    }, { once: true }); // 한 번만 실행되도록 설정

    window.appendCharacter = (char) => {
        if (resultDisplayed) {
            currentExpression = '';
            resultDisplayed = false;
        }

        // 연산자 중복 입력 방지
        const lastChar = currentExpression.slice(-1);
        const operators = ['+', '-', '*', '/'];
        if (operators.includes(char) && operators.includes(lastChar)) {
            currentExpression = currentExpression.slice(0, -1); // 마지막 연산자 제거
        }

        currentExpression += char;
        display.textContent = currentExpression;

        // 주문 효과음 재생
        if (spellSound) {
            spellSound.currentTime = 0; // 사운드를 처음부터 재생
            spellSound.play().catch(e => console.log("주문 효과음 재생 실패:", e));
        }
    };

    window.clearDisplay = () => {
        currentExpression = '';
        display.textContent = '0';
        resultDisplayed = false;
    };

    window.calculateResult = async () => {
        if (currentExpression === '') return;

        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ expression: currentExpression }),
            });
            const data = await response.json();

            if (data.error) {
                display.textContent = data.result; // "마법이 실패했습니다!" 메시지
                currentExpression = ''; // 에러 발생 시 초기화
            } else {
                display.textContent = data.result;
                currentExpression = data.result;
            }
            resultDisplayed = true;

        } catch (error) {
            console.error('Error:', error);
            display.textContent = '마법 오류!';
            currentExpression = ''; // 에러 발생 시 초기화
            resultDisplayed = true;
        }
    };
});