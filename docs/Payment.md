# Payment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Payment identifier | 
**account_id** | **int** | Identifier of the account to which this payment relates | 
**request_date** | **str** | Time of when this payment was requested, in the format &#39;YYYY-MM-DD HH:MM:SS.SSS&#39; (german time) | 
**execution_date** | **str** | Time of when this payment was executed, in the format &#39;YYYY-MM-DD HH:MM:SS.SSS&#39; (german time) | [optional] 
**type** | **str** | Payment type | 
**status** | **str** | Current payment status:&lt;br/&gt; &amp;bull; PENDING: means that this payment has been requested, but not yet executed.&lt;br/&gt; &amp;bull; SUCCESSFUL: means that this payment has been successfully executed.&lt;br/&gt; &amp;bull; NOT_SUCCESSFUL: means that this payment could not be executed successfully.&lt;br/&gt; &amp;bull; DISCARDED: means that this payment was discarded because another payment was requested for the same account before this payment was executed. | 
**bank_message** | **str** | Contains the bank&#39;s response to the execution of this payment. This field is not set until the payment gets executed. Note that even after the execution of the payment, the field might still not be set, if the bank did not send any response message. | [optional] 
**amount** | **float** | Total money amount of the payment order(s), as absolute value | 
**order_count** | **int** | Total count of orders included in this payment | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


