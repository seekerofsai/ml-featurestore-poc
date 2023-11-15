from datetime import timedelta

from feast import (
    FeatureView,
    Field,
)
from feast.types import Float32, Int32, String

from .data_sources import *
from .entities import *
# name used for dyanamodb table name for online store
_v1_daily_view = FeatureView(
    name="_v1_daily_view",
    description=" v1 daily training view",
    entities=[service_request,service_provider],
    ttl=timedelta(days=28),
    online=True,
    source=_v1_training_daily,

    tags={"production": "False"},
    owner="data_science@angi.com",
)




