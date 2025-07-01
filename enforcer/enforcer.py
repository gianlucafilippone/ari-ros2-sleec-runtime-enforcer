import asyncio
import httpx

async def enforcer_loop():
    try:
        async with httpx.AsyncClient() as client:
            probe_response = await client.get("http://localhost:8000/probe/latest_data")
            probe_data_json = probe_response.json()

            print(f"Probe data: {probe_data_json}")

            probe_data = probe_data_json.get("latest_data")
            if probe_data is None:
                print("No probe data")
                return

            # Data analysis, then when done and if needed
            task = "example_task"

            obligation_response = await client.post(
                "http://localhost:8001/obligation/execute",
                json={"task": task}
            )
            obligation_response_json = obligation_response.json()

            print(f"Obligation service response: {obligation_response_json}")

    except Exception as e:
        print(f"Error in REST call: {e}")


async def main():
    while True:
        await enforcer_loop()
        await asyncio.sleep(5.0)

if __name__ == "__main__":
    asyncio.run(main())