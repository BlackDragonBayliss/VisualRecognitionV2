from flask import Flask, jsonify, request
from automationManager import AutomationManager
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    content = request.get_json()
    return_value = 'pass'
    # print(str(content))
    response = "success"
    for key, value in content.items():
        if key == 'requestType':
            if value == "op1":
                automationManager = AutomationManager()
                # automationManager.operationStartCMDClickCenter()
                return "success"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=4470)