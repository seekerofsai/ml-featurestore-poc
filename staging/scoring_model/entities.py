from feast import (
    Entity,
    ValueType,
)

l = Entity(
    name="l",
    join_keys=["l_id"],
    description="l id",
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