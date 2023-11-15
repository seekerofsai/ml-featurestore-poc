from feast import (
    Entity,
    ValueType,
)

lead = Entity(
    name="lead",
    join_keys=["lead_id"],
    description="lead id",
    value_type=ValueType.INT64
)

booking = Entity(
    name="booking",
    join_keys=["booking_id"],
    description="booking id",
    value_type=ValueType.INT64
)


customer = Entity(
    name="customer",
    join_keys=["customer_id"],
    description="customer id",
    value_type=ValueType.INT64
)