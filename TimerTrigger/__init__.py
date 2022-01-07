import datetime
import logging

import azure.functions as func
import azure.durable_functions as df

async def main(mytimer: func.TimerRequest, starter) -> None:
    logging.info(f"TRIGGER Starttime: {datetime.datetime.now()}")
    client = df.DurableOrchestrationClient(starter)
    instance_id = await client.start_new("TestDurableFunctionsOrchestrator", None,starter)
    logging.info(f"Started orchestration for NAR with ID = '{instance_id}")