from feast import FeatureService
from .features import *

feature_service = FeatureService(
    name="leadscoring_model_v1",
    features=[bno_features_view],
    owner="bhanu.neti@angi.com",
)

feature_service_2 = FeatureService(
    name="leadscoring_model_v2",
    features=[bno_features_view, bno_bookings_view],
    owner="bhanu.neti@angi.com",
)