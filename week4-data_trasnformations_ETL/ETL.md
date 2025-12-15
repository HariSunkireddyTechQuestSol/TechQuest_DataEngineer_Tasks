ETL - Extarct, Transform, Load 

ETL is a part of data engineering. Where we extract the raw data from multiple sources and perform the transformations on that extracted raw data as per business requirements, then will load that transformed data to the traget location from where it is utilized for data analysis for creating insights for business needs. 

Here are the three main steps in ETL:

1. Extract - It is a process of getting the data that is stored in multiple locations. For example, if we take health care domain, the data is stored across multiple location like EHR Systems, On-prem servers, SQL servers and also in cloud storage locations (AWS, Azure, Snowflake, GCP and etc..) and in different formats (HL7, FHIR, Avro, Parquet, ORC), so all this data from multiple sources will be pulled and loaded to a cloud loaction from where it will be used further in ETL process. 

2. Transfromation - It is process of cleaning and making the raw data cleaned. For example, transforming data means, lets take the same example of heathcare domain, where the raw data which is pulled from multiple storage locations would be in different formats, so first we need to make that normalize, then we need to clean the data, which means removing duplicates and filling null values or removing them as per business requirements. And perfroming aggregations like grouping as per business needs. So then after all this, this tansformed data is again stored to one particular loaction. 

3. Loading - It is process of putting the transformed data in to target location from where the analytics team or business user will be using for analytics or day to day tasks. 
