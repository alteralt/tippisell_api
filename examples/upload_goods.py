import asyncio

import tippisell_api

shop_id = 1
api_key = "api_key"
product_id = 1


async def main():
    client = tippisell_api.Client(shop_id, api_key)
    await client.upload_goods(product_id, ["test", "test", "test"])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
