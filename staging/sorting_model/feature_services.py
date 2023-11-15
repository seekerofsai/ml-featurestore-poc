from feast import FeatureService
from .features import *

feature_service = FeatureService(
    name="_model_v1",
    features=[_v1_daily_view],
    owner="abc@abc.com",
)
