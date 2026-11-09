<!-- Converted from sample-data.txt (reStructuredText). Includes are inlined. -->

# Sample Datasets

MongoDB provides sample data you can load into your deployments. You can use
this data to quickly get started experimenting with data in MongoDB and using
tools such as the Atlas UI and `MongoDB Charts`.

## Available Sample Datasets

The following table shows the sample datasets available. Click a sample dataset
to learn more about it.

For instructions on loading this sample data into your deployment , see
load-sample-data-local or load-sample-data.

| Dataset Name | Description |
|---|---|
| sample-airbnb | Contains details on [AirBnB](https://www.airbnb.com) listings. |
| sample-analytics | Contains training data for a mock financial services application. |
| sample-geospatial | Contains shipwreck data. |
| sample-guides | Contains planet data. |
| sample-mflix | Contains movie data. Includes vector embeddings. |
| sample-restaurants | Contains restaurant data. |
| sample-supplies | Contains data from a mock office supply store. |
| sample-training | Contains MongoDB training services dataset. |
| sample-weather | Contains detailed weather reports. |

## Sample Data Namespaces

When you load the sample data, MongoDB creates the following
namespaces on your deployment:

**Warning:**

If any of these namespaces already exist on your 
cluster when you attempt to load the sample data, 
the operation will fail and no sample data will be loaded into your 
cluster.

| Database | Collection |
|---|---|
| `sample_airbnb` | `listingsAndReviews` |
| `sample_analytics` | `accounts` |
| `sample_analytics` | `customers` |
| `sample_analytics` | `transactions` |
| `sample_geospatial` | `shipwrecks` |
| `sample_guides` | `planets` |
| `sample_mflix` | `comments` |
| `sample_mflix` | `embedded_movies` |
| `sample_mflix` | `movies` |
| `sample_mflix` | `theaters` |
| `sample_mflix` | `users` |
| `sample_supplies` | `sales` |
| `sample_training` | `companies` |
| `sample_training` | `grades` |
| `sample_training` | `inspections` |
| `sample_training` | `posts` |
| `sample_training` | `routes` |
| `sample_training` | `trips` |
| `sample_training` | `zips` |
| `sample_weatherdata` | `data` |

## MongoDB Courses that Use Sample Data

[Instructor-led Training](https://www.mongodb.com/services/training)
   Get quickly ramped on MongoDB with comprehensive private training
   programs for developers and operations teams.
