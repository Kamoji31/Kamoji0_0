import sys
import io
import contextlib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to execute Python code and capture output
def execute_python_code(code):
    # Redirect stdout to capture print statements
    output = io.StringIO()
    sys.stdout = output
    
    try:
        # Execute the provided Python code
        exec(code)
    except Exception as e:
        return str(e)
    
    # Return the captured output
    return output.getvalue()

@app.route('/')
def index():
    return 'Python Code Execution Service Running'

@app.route('/run_python_code', methods=['POST'])
def run_python_code():
    try:
        data = request.get_json()  # Get the code from the frontend
        code = data['code']
        
        # Execute the Python code and capture the result
        result = execute_python_code(code)
        
        return jsonify({"output": result})
    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
