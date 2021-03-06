# KeywordRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rule identifier | 
**category** | [**Category**](Category.md) | The category that this rule assigns to the transactions that it matches | 
**direction** | **str** | Direction for the rule. &#39;Income&#39; means that the rule applies to transactions with a positive amount only, &#39;Spending&#39; means it applies to transactions with a negative amount only. | 
**creation_date** | **str** | Timestamp of when the rule was created, in the format &#39;YYYY-MM-DD HH:MM:SS.SSS&#39; (german time) | 
**keywords** | **list[str]** | Set of keywords that this rule defines. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


