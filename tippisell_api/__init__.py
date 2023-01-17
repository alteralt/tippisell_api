from . import exceptions, client

import sys
tippisell_api = sys.modules[__name__]
setattr(tippisell_api, "clients", client)
print("эм")

print(tippisell_api)

sys.modules[__name__] = tippisell_api



clients = type("clients", (object,), {"async_": client})
setattr(tippisell_api, "clients", clients)
print("эм")
sys.modules[__name__] = tippisell_api
