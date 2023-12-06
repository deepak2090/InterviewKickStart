import azure.functions as func
import logging
import asyncio

app = func.FunctionApp()

async def xyz(a, b):
    # Your custom function implementation goes here
    # This function can perform any logic you need with parameters a and b
    result = a + b
    await asyncio.sleep(5)  # Use asyncio.sleep for asynchronous delay
    logging.info('The delay function is running')
    print("the delay is running")
    return result

@app.function_name(name="HttpTrigger1")
@app.route(route="hello")
async def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = await req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        # Use asyncio.create_task to run the asynchronous function in the background
        task = asyncio.create_task(xyz(10, 30))  # Example: Pass 10 and 30 as parameters

        # Placeholder response message
        response_message = f"Hello async, {name}. This HTTP triggered function is processing the request."

        # Immediately return the response without waiting for the task to complete
        return func.HttpResponse(response_message)
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
