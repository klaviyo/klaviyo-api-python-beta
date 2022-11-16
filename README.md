# Python SDK for Klaviyo's Beta API

- SDK version: 1.0.0
- API revision: 2022-11-14.pre

## Helpful Resources

- [Beta API Reference](https://developers.klaviyo.com/en/v2022-11-14.pre/reference)
- [Latest API Guides](https://developers.klaviyo.com/en/docs)
- [Postman Workspace](https://www.postman.com/klaviyo/workspace/klaviyo-developers)
- [Interactive Guide (Jupyter Notebook)](https://github.com/klaviyo-labs/klaviyo-api-guides)

## Design & Approach

NOTE: This SDK only reflects the endpoints currently in Beta. Once endpoints are promoted from Beta to General Availability (GA), they will be removed from the next version of this SDK, and the version of this SDK corresponding to that Beta release will be deprecated.

This SDK is a thin wrapper around our current Beta API. See our API Reference for full documentation on behavior.

This SDK exactly mirrors the organization and naming convention of the above language-agnostic resources, with a few namespace changes to make it Pythonic (details in Appendix).

## Organization

This SDK is organized into the following resources:



- Data_Privacy



- Flows



- Lists



- Segments



- Tags



## Installation

You can install this library using [our pip package here](https://pypi.org/project/klaviyo-api-beta/).

Depending on your system configuration, you will need to run *one* of the following shell commands:

```bash
pip install klaviyo-api-beta
```

OR 

```bash
pip3 install klaviyo-api-beta
```

## Usage Example

### To instantiate the client

NOTE: 
* The SDK retries on resolvable errors, namely: rate limits (common) and server errors (rare).
* The keyword arguments define some advanced settings; the example is populated with the default values.
* `max_delay` denotes total delay (in seconds) across all attempts.

```python
from klaviyo_api_beta import KlaviyoAPIBeta

klaviyo_beta = KlaviyoAPIBeta("YOUR API KEY HERE", max_delay=60, max_retries=3, test_host=None)
```

### Example request

```python
klaviyo_beta.Tags.get_tags() 
```

## Error Handling

This SDK throws an `ApiException` error when the server returns a non-`2XX` response. 

An `ApiException` consists of the following attributes:

* `status` : `int`
* `reason` : `str`
* `body` : `bytes`
    * this can be decoded into a native python dictionary as follows:
        ```python
        # to decode to a dictionary
        import json
        BODY_DICT = json.loads(YOUR_EXCEPTION.body)

        # to decode to a string
        BODY_STRING = YOUR_EXCEPTION.body.decode('utf-8')
        ```
* `headers` : [class 'urllib3._collections.HTTPHeaderDict'](https://urllib3.readthedocs.io/en/stable/user-guide.html?highlight=httpheaderdict#response-content)
    * This can be interacted with as a normal dictionary:
        * ex:
            ```
            date = YOUR_EXCEPTION.headers['Date']
            keys = YOUR_EXCEPTION.headers.keys()
            values = YOUR_EXCEPTION.headers.values()
            ```

## Important Notes

- The main difference between this SDK and the language-agnostic API Docs that the below endpoints link to is that this SDK automatically adds the `revision` header corresponding to the SDK version.
- Organization: Resource groups and operation_ids are listed below in alphabetical order, first by Resource name, then by **OpenAPI Summary**. Operation summaries are those listed in the right side bar of the [API Reference](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/get_events).
- For example values / data types, as well as whether parameters are required/optional, please reference the corresponding API Reference link.
- Some keyword args may potentially be required for the API call to succeed, the linked API docs are the source of truth regarding which keyword params are required.
- JSON payloads should be passed in as native python dictionaries.
- You can override the client private key by passing in an optional `api_key` keyword arg to any API call that takes a private key. As a reminder: do NOT do this client-side/onsite.

# Comprehensive list of Operations & Parameters





## Data_Privacy

#### [Create Data Privacy Deletion Job](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/create_data_privacy_deletion_job)

```python
## Positional Arguments

# body | dict

klaviyo_beta.Data_Privacy.create_data_privacy_deletion_job(body);
```






## Flows

#### [Get Flow Tags](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/get_flow_tags)

```python
## Positional Arguments

# flow_id | str

## Keyword Arguments

# fields_tag | [str]

klaviyo_beta.Flows.get_flow_tags(flow_id, fields_tag=fields_tag);
```






## Lists

#### [Get List Tags](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/get_list_tags)

```python
## Positional Arguments

# list_id | str

## Keyword Arguments

# fields_tag | [str]

klaviyo_beta.Lists.get_list_tags(list_id, fields_tag=fields_tag);
```






## Segments

#### [Get Segment Tags](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/get_segment_tags)

```python
## Positional Arguments

# segment_id | str

## Keyword Arguments

# fields_tag | [str]

klaviyo_beta.Segments.get_segment_tags(segment_id, fields_tag=fields_tag);
```






## Tags

#### [Create Tag](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/create_tag)

```python
## Positional Arguments

# body | dict

klaviyo_beta.Tags.create_tag(body);
```




#### [Create Tag Group](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/create_tag_group)

```python
## Positional Arguments

# body | dict

klaviyo_beta.Tags.create_tag_group(body);
```




#### [Create Tag Relationships](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/create_tag_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str
# body | dict

klaviyo_beta.Tags.create_tag_relationships(id, related_resource, body);
```




#### [Delete Tag](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/delete_tag)

```python
## Positional Arguments

# id | str

klaviyo_beta.Tags.delete_tag(id);
```




#### [Delete Tag Group](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/delete_tag_group)

```python
## Positional Arguments

# id | str

klaviyo_beta.Tags.delete_tag_group(id);
```




#### [Delete Tag Relationships](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/delete_tag_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str
# body | dict

klaviyo_beta.Tags.delete_tag_relationships(id, related_resource, body);
```




#### [Get Tag](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/get_tag)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_tag | [str]

klaviyo_beta.Tags.get_tag(id, fields_tag=fields_tag);
```




#### [Get Tag Group](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/get_tag_group)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_tag_group | [str]

klaviyo_beta.Tags.get_tag_group(id, fields_tag_group=fields_tag_group);
```




#### [Get Tag Group Relationships](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/get_tag_group_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str

klaviyo_beta.Tags.get_tag_group_relationships(id, related_resource);
```




#### [Get Tag Groups](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/get_tag_groups)

```python

## Keyword Arguments

# fields_tag_group | [str]
# filter | str
# page_cursor | str
# sort | str

klaviyo_beta.Tags.get_tag_groups(fields_tag_group=fields_tag_group, filter=filter, page_cursor=page_cursor, sort=sort);
```




#### [Get Tag Relationships](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/get_tag_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str

klaviyo_beta.Tags.get_tag_relationships(id, related_resource);
```




#### [Get Tags](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/get_tags)

```python

## Keyword Arguments

# fields_tag | [str]
# filter | str
# page_cursor | str
# sort | str

klaviyo_beta.Tags.get_tags(fields_tag=fields_tag, filter=filter, page_cursor=page_cursor, sort=sort);
```




#### [Update Tag](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/update_tag)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo_beta.Tags.update_tag(id, body);
```




#### [Update Tag Group](https://developers.klaviyo.com/en/v2022-11-14.pre/reference/update_tag_group)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo_beta.Tags.update_tag_group(id, body);
```




# Appendix

## Global Keyword Args

NOTE: These are arguments that you can apply to any endpoint call, and which are unique to the SDK

We currently support the following global keyword args:
- `api_key` : use this to override the client-level api_key which you define upon client instantiation

## Refresher on catching exceptions:

```python
try:
    YOUR_CALL
except Exception as e:
    print(e.status)
    print(e.reason)
    print(e.body)
    print(e.headers)
```

## Parameters & Arguments

The parameters follow the same naming conventions as the resource groups and operations.

We stick to the following convention for parameters/arguments

1. All parameters are passed as function args.
2. All query and path params that are tagged as `required` in the docs are passed as positional args.
3. All optional query params are passed as keyword args.
4. Where applicable, the `body` param is passed in as a positional arg, and is expected to be a native python dictionary. Within that dictionary, refer to the API docs to see which fields are required/optional, along with valid values.
4. There is no need to pass in your private `api_key` for any operations, as it is defined upon client instantiation; public key is still required where applicable. However, you can pass in an optional `api_key` kwarg to override the client private key for a specific call (REMINDER: don't do this client-side).

## Namespace

In the interest of making the SDK Pythonic, we made the following namespace changes *relative* to the language agnostic resources up top (API Docs, Guides, etc).

- Resource names use Title + Snake Casing, (e.g. `Data_Privacy`)
- function names and parameter names remain unchanged and use snake case (e.g. `get_metrics`, and `profile_id`)