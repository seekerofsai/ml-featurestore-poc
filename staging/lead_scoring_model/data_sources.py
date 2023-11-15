from feast import PushSource, SnowflakeSource
import yaml

# Feast also supports pulling data from data warehouses like BigQuery, Snowflake, Redshift and data lakes (e.g. via
# Redshift Spectrum, Trino, Spark)

leadsscoring_bno_features = SnowflakeSource(
    name="leadsscoring_bno_features",
    database=yaml.safe_load(open("feature_store.yaml"))["offline_store"]["database"],
    table="LEADSSCORING_BNO_FEATURE_SET_TRAIN",
    schema="S3_BUCKET",
    timestamp_field="lead_create_datetime",
)

leadsscoring_bno_bookings = SnowflakeSource(
    name="leadsscoring_bno_bookings",
    database=yaml.safe_load(open("feature_store.yaml"))["offline_store"]["database"],
    table="LEADSSCORING_BNO_BOOKINGS_TRAIN",
    schema="S3_BUCKET",
    timestamp_field="original_added_date",
)