# finapi.WebFormsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_web_form**](WebFormsApi.md#get_web_form) | **GET** /api/v1/webForms/{id} | Get a web form


# **get_web_form**
> WebForm get_web_form(id)

Get a web form

Get a web form of the user that is authorized by the access_token. Must pass the web form's identifier and the user's access_token. <br/><br/>Note that every web form resource is automatically removed from the finAPI system after 24 hours after its creation.

### Example
```python
from __future__ import print_function
import time
import finapi
from finapi.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: finapi_auth
configuration = finapi.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = finapi.WebFormsApi(finapi.ApiClient(configuration))
id = 789 # int | Identifier of web form

try:
    # Get a web form
    api_response = api_instance.get_web_form(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebFormsApi->get_web_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of web form | 

### Return type

[**WebForm**](WebForm.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

