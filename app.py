from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').lower()
    
    response = {
        'hi': '',
        'book': 'this need to be added later',
        'hours': '',
        'bye': 'goodbye'
    }
    reply = response.get(user_message, 'only hi, book, hour and bye work')
    
    return jsonify({'message': reply})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
    