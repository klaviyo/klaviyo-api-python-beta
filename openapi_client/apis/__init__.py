
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from openapi_client.api.campaigns_api import CampaignsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openapi_client.api.campaigns_api import CampaignsApi
from openapi_client.api.data_privacy_api import DataPrivacyApi
from openapi_client.api.flows_api import FlowsApi
from openapi_client.api.lists_api import ListsApi
from openapi_client.api.segments_api import SegmentsApi
from openapi_client.api.tags_api import TagsApi
