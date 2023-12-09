import time
import azure.functions as func
import azure.durable_functions as df

myApp = df.DFApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# An HTTP-Triggered Function with a Durable Functions Client binding
@myApp.route(route="orchestrators/{functionName}")
@myApp.durable_client_input(client_name="client")
async def http_start(req: func.HttpRequest, client):
    function_name = req.route_params.get('functionName')

    valid_function_names = ["hello_orchestrator"]  # Add valid function names as needed
    if function_name not in valid_function_names:
        return func.HttpResponse(f"Invalid function name: {function_name}", status_code=400)

    instance_id = await client.start_new(function_name)
    response = client.create_check_status_response(req, instance_id)
    return response

# Orchestrator
@myApp.orchestration_trigger(context_name="context")
def hello_orchestrator(context):
    result1 = yield context.call_activity("hello_deepak", "Seattle")
    result2 = yield context.call_activity("hello_deepak", "Tokyo")
    result3 = yield context.call_activity("hello_deepak", "London")

    return [result1, result2, result3]

# Activity
@myApp.activity_trigger(input_name="city")
def hello_deepak(city: str):
    #time.sleep(200)
    return "Hello " + city