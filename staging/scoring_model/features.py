from datetime import timedelta

from feast import (
    FeatureView,
    Field,
)
from feast.types import Float32, Int32, String
from .data_sources import *
from .entities import *
# name used for dyanamodb table name for online store
bno_features_view = FeatureView(
    name="bno_features",
    description="bno scores",
    entities=[l],
    ttl=timedelta(days=90),
    schema=[
        Field(name="service_ntv_per_booking", dtype=Float32),
        Field(name="service_nrev_per_booking", dtype=Float32),
        Field(name="service_percent_completed", dtype=Float32),
        Field(name="service_percent_canceled", dtype=Float32),
    ],
    online=True,
    source=lsscoring_bno_features,
    tags={"production": "True"},
    owner="abc@abc.com",
)
# name used for dyanamodb table name for online store
bno_bookings_view = FeatureView(
    name="bno_bookings",
    description="bno scores",
    entities=[customer],
    ttl=timedelta(days=365),
    schema=[
        Field(name="service_ntv_per_booking", dtype=Float32),
        Field(name="service_nrev_per_booking", dtype=Float32),
        Field(name="service_percent_completed", dtype=Float32),
        Field(name="service_percent_canceled", dtype=Float32),
    ],
    online=True,
    source=lsscoring_bno_bookings,
    tags={"production": "True"},
    owner="abc@abc.com",
)
