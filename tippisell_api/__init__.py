import importlib.util
import sys

# noinspection PyUnresolvedReferences
from tippisell_api import exceptions
from tippisell_api.client import Client

# For save reverse compatibility
# noinspection PyUnresolvedReferences
spec = importlib.util.spec_from_loader(client.__name__, client.__loader__)
clients_module = importlib.util.module_from_spec(spec)
async_model = importlib.util.module_from_spec(spec)
async_model.Client = Client

sys.modules["tippisell_api.clients"] = clients_module
sys.modules["tippisell_api.clients.async_"] = async_model
# ---------------------------------
