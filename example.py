import asyncio
import aiohttp
import os
from dotenv import load_dotenv

from vicare_energy_api_lib.auth import Auth

load_dotenv()  # Load variables from .env

async def main():
    access_token = os.environ["ACCESS_TOKEN"]
    gateway_id = os.environ["GATEWAY_ID"]
    device_id = os.environ["DEVICE_ID"]
    async with aiohttp.ClientSession() as session:
        auth = Auth(
            session,
            "https://api.viessmann.com/iot/v1/analytics-api/dataLake/chronos/v0",
            access_token,
        )
        payload = {
            "gateway_id": gateway_id,
            "device_id": device_id,
            "start_datetime": "2025-02-05T00:00:00",
            "end_datetime": "2025-02-06T00:00:00",
            "properties": [
                "heating.power.consumption.total",
                "heating.power.consumption.heating",
                "heating.power.consumption.dhw"
            ],
            "resolution": "1d"
        }
        resp = await auth.request("post", "thermal_energy", json=payload)
        print("HTTP response status code", resp.status)
        print("HTTP response JSON content", await resp.json())

asyncio.run(main())