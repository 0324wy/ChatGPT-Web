from revChatGPT import Chatbot
from flask import Flask, request, jsonify
import json


app = Flask(__name__)


# app.debug = True

@app.route('/http/query/', methods=['post'], strict_slashes=False)
def post_http():
        print(request)
        if not request.get_data():  # 检测是否有数据
                return ('fail')

        request_data = request.get_data().decode('utf-8')

        print(request_data)

        print(type(request_data))

        question = json.loads(request_data)['question']
        print(question)

        with open("../../config.json", "r") as f:
            config = json.load(f)
        chatbot = Chatbot(config)
        if 'session_token' in config:
            chatbot.refresh_session()

        try:
            print("Chatbot: ")
            answer = chatbot.get_chat_response(question)['message']

            print(answer)

            result = {'answer': answer}
            print(type(result))

            return jsonify(result)
        except Exception as e:
            print(e)
            return "error"


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8000)

