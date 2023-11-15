from feast import PushSource, SnowflakeSource
import yaml



psm_v1_training_daily  = SnowflakeSource(
    name="psm_v1_training_daily",
    database="DATAFEED_DEV",
    table="PSMDAILY_PSM_V1_TRAINING_DAILY",
    schema="S3_BUCKET",
    timestamp_field="create_datetime",
)



 