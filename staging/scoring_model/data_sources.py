from feast import PushSource, SnowflakeSource
import yaml

# Feast also supports pulling data from data warehouses like BigQuery, Snowflake, Redshift and data lakes (e.g. via
# Redshift Spectrum, Trino, Spark)

lsscoring_bno_features = SnowflakeSource(
    name="lsscoring_bno_features",
    database=yaml.safe_load(open("feature_store.yaml"))["offline_store"]["database"],
    table="lSSCORING_BNO_FEATURE_SET_TRAIN",
    schema="S3_BUCKET",
    timestamp_field="l_create_datetime",
)

lsscoring_bno_bookings = SnowflakeSource(
    name="lsscoring_bno_bookings",
    database=yaml.safe_load(open("feature_store.yaml"))["offline_store"]["database"],
    table="lSSCORING_BNO_BOOKINGS_TRAIN",
    schema="S3_BUCKET",
    timestamp_field="original_added_date",
)