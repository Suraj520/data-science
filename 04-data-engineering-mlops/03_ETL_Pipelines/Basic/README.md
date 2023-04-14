# About
Basic ETL Pipeline using Google Data Fusion.

# Brief Intro

ETL stands for Extract,Transform and load. Data scientists prefer to use ELT mostly where the data is extracted from various sources like CSVs, Jsons, Webhooks, APIs and is being loaded into a data-lake from where the data-scientist fetches the data and transforms it as per his need.

Google Data Fusion is a nocode platform used to make batch pipelines. Batch ETL means data is extracted, transformed and loaded in batches. 

1. Pipeline Studio in Cloud Data Fusion is used to build a data pipeline.
2. Wrangler plugin is used to build an apply transformations to the data that goes in pipeline.
3. The output will be written to big query table.

The steps are described below :

a. First, Login  to the Google account and then activate Cloud Shell by Google Console.
b. Load the data from CSV source after checking project permissions for cloud data fusion instance.
c. Ensure service account user permission exists.
d. Build a batch pipeline which can then be configured, tested and deployed to view the results.