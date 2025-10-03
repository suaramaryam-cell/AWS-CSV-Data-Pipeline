import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## get job arguments
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

## initialize Glue job
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

## READ: load CSV from S3
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://aws-s3-bucket-glue/input/coffee_sales.csv"]},  # change to your real file path
    format="csv",
    format_options={"withHeader": True}
)

## TRANSFORM: select only coffee_name and money
transformed = datasource.select_fields(["coffee_name", "money"])

## WRITE: save output to S3 as CSV
glueContext.write_dynamic_frame.from_options(
    frame=transformed,
    connection_type="s3",
    connection_options={"path": "s3://aws-s3-bucket-glue/output/"},
    format="csv"
)

job.commit()
