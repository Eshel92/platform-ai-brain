<!-- Converted from administration/free-monitoring.txt (reStructuredText). Includes are inlined. -->

:orphan:

# Free Monitoring

**Warning:** Free monitoring is decommissioned.

Free monitoring was decommissioned in August 2023. 

Beginning in April 2023, you cannot enable free monitoring on MongoDB
Community instances.

The following list shows monitoring options for your deployment:

- **Deploy a MongoDB Atlas dedicated cluster**. Migrate your
  data to a MongoDB Atlas dedicated cluster sized M10 or greater,
  which includes several advanced monitoring and alerting features:

  - Query Profiler
  - Performance Advisor
  - Real-Time Performance Panel

- **Deploy a MongoDB Atlas free cluster**. A free Atlas cluster includes
  basic monitoring and alerting capabilities. After you
  create a free cluster, use `mongodump` and
  `mongorestore` to manually create a backup of your database
  and import your data from your MongoDB Community instance.

- **Use MongoDB Cloud Manager**. The [MongoDB Cloud Manager](https://docs.cloudmanager.mongodb.com/) free tier includes basic
  monitoring capabilities.
