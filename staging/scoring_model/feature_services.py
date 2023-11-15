from feast import FeatureService
from .features import *

feature_service = FeatureService(
    name="lscoring_model_v1",
    features=[bno_features_view],
    owner="abc@abc.com",
)

feature_service_2 = FeatureService(
    name="lscoring_model_v2",
    features=[bno_features_view, bno_bookings_view],
    owner="abc@abc.com",
)