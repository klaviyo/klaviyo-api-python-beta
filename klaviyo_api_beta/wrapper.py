from __future__ import absolute_import

from __future__ import print_function
import tenacity
import openapi_client
import klaviyo_api_beta.custom_retry as custom_retry
from dataclasses import dataclass
from typing import Callable, ClassVar
from openapi_client.api import campaigns_api
from openapi_client.api import data_privacy_api
from openapi_client.api import flows_api
from openapi_client.api import lists_api
from openapi_client.api import segments_api
from openapi_client.api import tags_api


@dataclass
class KlaviyoAPIBeta:

    api_key: str
    max_delay: int = 60
    max_retries: int = 3
    test_host: str = ''

    _REVISION = "2022-12-15.pre"

    _STATUS_CODE_TOO_MANY_REQUESTS = 429
    _STATUS_CODE_SERVICE_UNAVAILABLE = 503
    _STATUS_CODE_GATEWAY_TIMEOUT = 504
    _STATUS_CODE_A_TIMEOUT_OCCURED = 524

    _RETRY_CODES = {
        _STATUS_CODE_TOO_MANY_REQUESTS,
        _STATUS_CODE_SERVICE_UNAVAILABLE,
        _STATUS_CODE_GATEWAY_TIMEOUT,
        _STATUS_CODE_A_TIMEOUT_OCCURED
        }

    _CURSOR_SEARCH_TOKENS = ['page%5Bcursor%5D','page[cursor]']

    def __post_init__(self):

        self.configuration = openapi_client.Configuration(
            api_key={'Klaviyo-API-Key':f'Klaviyo-API-Key {self.api_key}'}
            )

        if self.test_host:
            self.configuration.host = self.test_host

        self.api_client = openapi_client.ApiClient(self.configuration)

        self.api_client.default_headers['revision'] = self._REVISION
        
        if self.max_retries <= 0:
            self.max_wait = .1
        else:
            self.max_wait = self.max_delay/self.max_retries


        self.retry_logic = tenacity.retry(
            reraise=True,
            retry=custom_retry.retry_if_qualifies(self._RETRY_CODES),
            wait=tenacity.wait.wait_random_exponential(multiplier = 1, max = self.max_wait),
            stop=tenacity.stop.stop_after_attempt(self.max_retries)
        )

        
        ## Adding Campaigns to Client
        self.Campaigns=campaigns_api.CampaignsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Campaigns
        self.Campaigns.assign_campaign_message_template=self._page_cursor_update(self.retry_logic(self.Campaigns.assign_campaign_message_template))
        self.Campaigns.create_campaign=self._page_cursor_update(self.retry_logic(self.Campaigns.create_campaign))
        self.Campaigns.create_campaign_clone=self._page_cursor_update(self.retry_logic(self.Campaigns.create_campaign_clone))
        self.Campaigns.create_campaign_send_job=self._page_cursor_update(self.retry_logic(self.Campaigns.create_campaign_send_job))
        self.Campaigns.delete_campaign=self._page_cursor_update(self.retry_logic(self.Campaigns.delete_campaign))
        self.Campaigns.get_campaign=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign))
        self.Campaigns.get_campaign_message=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_message))
        self.Campaigns.get_campaign_relationships=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_relationships))
        self.Campaigns.get_campaign_send_job=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_send_job))
        self.Campaigns.get_campaign_tags=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_tags))
        self.Campaigns.get_campaigns=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaigns))
        self.Campaigns.update_campaign=self._page_cursor_update(self.retry_logic(self.Campaigns.update_campaign))
        self.Campaigns.update_campaign_message=self._page_cursor_update(self.retry_logic(self.Campaigns.update_campaign_message))
        self.Campaigns.update_campaign_send_job=self._page_cursor_update(self.retry_logic(self.Campaigns.update_campaign_send_job))
        
        
        ## Adding Data_Privacy to Client
        self.Data_Privacy=data_privacy_api.DataPrivacyApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Data_Privacy
        self.Data_Privacy.request_profile_deletion=self._page_cursor_update(self.retry_logic(self.Data_Privacy.request_profile_deletion))
        
        
        ## Adding Flows to Client
        self.Flows=flows_api.FlowsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Flows
        self.Flows.get_flow_tags=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_tags))
        
        
        ## Adding Lists to Client
        self.Lists=lists_api.ListsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Lists
        self.Lists.get_list_tags=self._page_cursor_update(self.retry_logic(self.Lists.get_list_tags))
        
        
        ## Adding Segments to Client
        self.Segments=segments_api.SegmentsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Segments
        self.Segments.get_segment_tags=self._page_cursor_update(self.retry_logic(self.Segments.get_segment_tags))
        
        
        ## Adding Tags to Client
        self.Tags=tags_api.TagsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Tags
        self.Tags.create_tag=self._page_cursor_update(self.retry_logic(self.Tags.create_tag))
        self.Tags.create_tag_group=self._page_cursor_update(self.retry_logic(self.Tags.create_tag_group))
        self.Tags.create_tag_relationships=self._page_cursor_update(self.retry_logic(self.Tags.create_tag_relationships))
        self.Tags.delete_tag=self._page_cursor_update(self.retry_logic(self.Tags.delete_tag))
        self.Tags.delete_tag_group=self._page_cursor_update(self.retry_logic(self.Tags.delete_tag_group))
        self.Tags.delete_tag_relationships=self._page_cursor_update(self.retry_logic(self.Tags.delete_tag_relationships))
        self.Tags.get_tag=self._page_cursor_update(self.retry_logic(self.Tags.get_tag))
        self.Tags.get_tag_group=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_group))
        self.Tags.get_tag_group_relationships=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_group_relationships))
        self.Tags.get_tag_groups=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_groups))
        self.Tags.get_tag_relationships=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_relationships))
        self.Tags.get_tags=self._page_cursor_update(self.retry_logic(self.Tags.get_tags))
        self.Tags.update_tag=self._page_cursor_update(self.retry_logic(self.Tags.update_tag))
        self.Tags.update_tag_group=self._page_cursor_update(self.retry_logic(self.Tags.update_tag_group))
        
        

    @classmethod
    def _page_cursor_update(cls, func: Callable, *args, **kwargs) -> Callable: 
        def _wrapped_func(*args, **kwargs):
            if 'page_cursor' in kwargs:
                page_cursor = kwargs['page_cursor']+'&'
                if page_cursor:
                    if isinstance(page_cursor,str):
                        if 'https://' in page_cursor:

                            search_tokens = cls._CURSOR_SEARCH_TOKENS
                            found_token = None
                            for token in search_tokens:
                                if token in page_cursor:
                                    found_token = token
                                    break
                            if found_token:
                                start = page_cursor.find(found_token)+len(found_token)+1
                                end = page_cursor[start:].find('&')
                                kwargs['page_cursor'] = page_cursor[start:start+end]
            return func(*args,**kwargs)
        return _wrapped_func