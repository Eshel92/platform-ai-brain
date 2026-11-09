<!-- Converted from sample-data/load-sample-data-local.txt (reStructuredText). Includes are inlined. -->

# Load Sample Data Into A Local Deployment

## About this Task

*Estimated completion time: 5 minutes*

Use this tutorial to load sample data into your self-managed
MongoDB deployment.

## Before You Begin

To utilize the sample data that MongoDB provides, you must first create a
deployment to load data into. To create a self-managed local deployment, see
configuration-file.

To load sample data, you must also have a minimum of 
`readWrite` access to the deployment. For more information on user
administration, see manage-users-and-roles. 

## Steps

To load sample data into your local deployment: 

**Step 1: Download the sample data.**

Run the following command in your terminal to download the sample data:

```
curl  https://atlas-education.s3.amazonaws.com/sampledata.archive -o sampledata.archive
```

**Step 2: Load the data into your deployment.**

Run the following command to load the data into your deployment,
replacing `<port-number>` with the port where you're hosting the 
deployment:

```
mongorestore --archive=sampledata.archive --port=<port-number>
```

## Learn More

      
You can also generate synthetic data that aligns to your real data's
schema. To learn more, see synthetic-data.

To import your own data, see import-strategies.
