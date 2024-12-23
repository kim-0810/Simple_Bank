from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

# 은행별 서비스 URL 매핑
BANK_SERVICES = {
    'https://www.kbstar.com/': {
        '돈 확인하기': 'https://www.kbstar.com/inquiry',
        '돈 보내기': 'https://www.kbstar.com/transfer',
        '고객센터': 'https://www.kbstar.com/customer_service',
        '자동 돈 보내기': 'https://www.kbstar.com/auto_transfer'
    },
    'https://www.wooribank.com/': {
        '돈 확인하기': 'https://www.wooribank.com/inquiry',
        '돈 보내기': 'https://www.wooribank.com/transfer',
        '고객센터': 'https://www.wooribank.com/customer_service',
        '자동 돈 보내기': 'https://www.wooribank.com/auto_transfer'
    },
    'https://banking.nonghyup.com/': {
        '돈 확인하기': 'https://banking.nonghyup.com/inquiry',
        '돈 보내기': 'https://banking.nonghyup.com/transfer',
        '고객센터': 'https://banking.nonghyup.com/customer_service',
        '자동 돈 보내기': 'https://banking.nonghyup.com/auto_transfer'
    },
    'https://www.shinhan.com/': {
        '돈 확인하기': 'https://www.shinhan.com/inquiry',
        '돈 보내기': 'https://www.shinhan.com/transfer',
        '고객센터': 'https://www.shinhan.com/customer_service',
        '자동 돈 보내기': 'https://www.shinhan.com/auto_transfer'
    },
    'https://www.kebhana.com/': {
        '돈 확인하기': 'https://www.kebhana.com/inquiry',
        '돈 보내기': 'https://www.kebhana.com/transfer',
        '고객센터': 'https://www.kebhana.com/cont/adm/popup/customer/cust2017_pop10.jsp',
        '자동 돈 보내기': 'https://www.kebhana.com/auto_transfer'
    },
    'https://www.ibk.co.kr/': {
        '돈 확인하기': 'https://www.ibk.co.kr/inquiry',
        '돈 보내기': 'https://www.ibk.co.kr/transfer',
        '고객센터': 'https://www.ibk.co.kr/customer_service',
        '자동 돈 보내기': 'https://www.ibk.co.kr/auto_transfer'
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url', '').strip()
    
    if url in BANK_SERVICES:
        return jsonify({
            'success': True,
            'url': url
        })
    return jsonify({
        'success': False,
        'error': '잘못된 url을 넣으셨습니다'
    })

@app.route('/redirect/<service>')
def redirect_to_service(service):
    url = request.args.get('bank')
    if url in BANK_SERVICES and service in BANK_SERVICES[url]:
        return redirect(BANK_SERVICES[url][service])
    return '잘못된 접근입니다.'

if __name__ == '__main__':
    app.run(debug=True)
