# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import datetime
import logging
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    logging.info(f"ORCHESTRATOR Starttime: {datetime.datetime.now()}")
    result1 = yield context.call_activity('TestFunction', "Test")
    logging.info(f"ORCHESTRATOR Endtime: {datetime.datetime.now()}")
    return [result1]

main = df.Orchestrator.create(orchestrator_function)