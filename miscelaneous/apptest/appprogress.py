from flask import Flask, render_template, Response
import asyncio
import json
import aiohttp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

async def run_pytest(progress_callback):
    total_steps = 10  # Total steps in running PyTest

    for step in range(total_steps + 1):
        await asyncio.sleep(3)  # Simulate a step in running PyTest
        progress_callback(step * 100 / total_steps)

    # Replace this section with your actual PyTest framework code
    # and capture the responses in JSON format
    pytest_responses = [
        {"status": "pass", "message": "Test 1 passed"},
        {"status": "pass", "message": "Test 2 passed"},
        {"status": "fail", "message": "Test 3 failed"},
        # ...
    ]
    
    return pytest_responses

@app.route('/run_pytest')
def run_pytest_route():
    def generate():
        async def progress_callback(percentage):
            yield f"data: {json.dumps({'progress': percentage})}\n\n"

        async def run_task():
            async with aiohttp.ClientSession() as session:
                pytest_responses = await run_pytest(progress_callback)
                yield f"data: {json.dumps({'result': pytest_responses})}\n\n"
                yield "event: close\ndata: Task Complete\n\n"

        asyncio.run(run_task())

    return app.response_class(generate(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
