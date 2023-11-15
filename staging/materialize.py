import sys
import argparse
from feast import FeatureStore
from datetime import datetime, timedelta
import pendulum
import pytz


logger = get_logger(__name__)

parser = argparse.ArgumentParser(
    description="Feature materialization driver",
    prog=""
)

parser.add_argument(
    '-feature_view', type=str, help='feature view to materialize',
    dest = "feature_view",
    default = ""
)

parser.add_argument(
    '-env', type=str,
    help="Environment job is running on",
    dest="env",
    default='staging'
)

parser.add_argument(
    '-start_datetime', type='str',
    help="start time",
    dest="start_datetime",
    default=""
)

parser.add_argument(
    '-end_datetime', type='str',
    help="end time",
    dest="end_datetime",
    default=""
)

parser.add_argument(
    '--incremental', action='store_true',
    help="specify materialization is incremental",
    dest="incremental",
    default=False

)


def materialize(data_interval_start: object = None, data_interval_end: object = None, view_name: object = None, incremental: object = False) -> object:
    store = FeatureStore(repo_path=".")
    if view_name:
        if incremental:
            store.materialize_incremental(datetime.datetime.now(), feature_views=[view_name])
        else:
            store.materialize(data_interval_start,data_interval_end, feature_views=[view_name])
    else:
        if incremental:
            store.materialize_incremental(datetime.datetime.now())
        else:
            store.materialize(data_interval_start,data_interval_end)




if __name__ == '__main__':
    args = parser.parse_args()
    logger.info(f"Materialize with env: {args.env} and view name: {args.feature_view}")
    start_interval = pendulum.parse(start_datetime)
    end_interval = pendulum.parse(end_datetime)

    try:
        materialize(start_interval, end_interval, feature_view, incremental )
        logger.info(f"Completed Materialize with env: {args.env} and view name: {args.feature_view}")
    except Exception as e:
        logger.error(e)
        sys.exit(1)
