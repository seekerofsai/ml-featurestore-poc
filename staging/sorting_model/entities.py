from feast import (
    Entity,
)

service_request = Entity(
    name="service_request",
    join_keys=["sr_oid"],
    description="service request id",
)

service_provider = Entity(
    name="service_provider",
    join_keys=["sp_id"],
    description="service request id",
)

task = Entity(
    name="task",
    join_keys=["task_oid"],
    description="Task id",
)

zipcode = Entity(
    name="zipcode",
    join_keys=["zip_code"],
    description="zipcode",
)