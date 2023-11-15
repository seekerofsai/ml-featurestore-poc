from feast import FeatureService
from .features import *

feature_service = FeatureService(
    name="psm_model_v1",
    features=[psm_v1_daily_view],
    owner="bhanu.neti@angi.com",
)
