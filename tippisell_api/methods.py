import typing
import contextlib


class BaseMethod:
    http_method: typing.Literal["get", "post", "put", "delete"] = None
    path: str = None
    params: list = None

    def __init__(self, **kwargs):
        self.kwargs = kwargs

        self._api_key = None

    def prepare_api_key(self, api_key: str):
        self._api_key = api_key
        return self

    def prepare_shop_id(self, shop_id: int):
        self.kwargs["shop_id"] = shop_id
        return self

    def get_params(self) -> dict:
        params = {}

        for key in self.params or []:
            with contextlib.suppress(KeyError):
                value = self.kwargs.pop(key)
                if value is not None:
                    params[key] = value

        return params

    def get_headers(self) -> dict:
        return {"api-key": self._api_key}

    def validate(self):
        pass


class GetUser(BaseMethod):
    http_method = "get"
    path = "/v2/user/"
    params = ["user_id", "telegram_id", "shop_id"]

    def validate(self):
        assert 1 < len(self.get_params())
