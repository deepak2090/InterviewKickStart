from flask import Flask, render_template, request
import concurrent.futures

app = Flask(__name__)


def long_running_task(selected_resource, input_value):
    import time
    time.sleep(10)
    return f"Received parameters: resource={selected_resource}, input_value={input_value}"


@app.route('/', methods=['GET', 'POST'])
def index():
    feedback_message = None

    # Extract parameters from the URL
    selected_resource = request.args.get('resource')
    input_value = request.args.get('input_value')

    if selected_resource and input_value:
        import time
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(long_running_task, selected_resource, input_value)
            # Respond immediately
        feedback_message = f"Received parameters: resource={selected_resource}, input_value={input_value}"
        # You can perform other actions or logging as needed

    return render_template('index.html', feedback_message=feedback_message)

@app.route('/<resource>', methods=['GET'])
def resource_page(resource):
    # Use the 'resource' parameter here for further processing
    return f"Welcome to the {resource} page!"

if __name__ == '__main__':
    app.run(debug=True)
