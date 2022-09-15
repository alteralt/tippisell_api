import random
import typing
from aiohttp import web
from tippisell_api import webhook, models


class WebhookRequestHandler(webhook.WebhookRequestHandler):
    async def validate_sale(
            self, user: models.User, product: models.Product, data: typing.List[str]) -> typing.List[dict]:
        response = bool(random.randint(0, 1))
        print(response)
        return [{"is_valid": response, "data": line} for line in data]


routes = [
    web.post("/", WebhookRequestHandler)
]


app = web.Application()
app.add_routes(routes)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=5000)
