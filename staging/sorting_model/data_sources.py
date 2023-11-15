from feast import PushSource, SnowflakeSource
import yaml



_v1_training_daily  = SnowflakeSource(
    name="_v1_training_daily",
    database="DATAFEED_DEV",
    table="DAILY__V1_TRAINING_DAILY",
    schema="S3_BUCKET",
    timestamp_field="create_datetime",
)



 