<!-- Converted from mongoimport/mongoimport-guide.txt (reStructuredText). Includes are inlined. -->

# mongoimport Example Guide

MongoDB provides the `mongoimport` tool to import JSON and CSV
files into your main dataset. This guide explains how to effectively use
`mongoimport` to move your data into your MongoDB database.

## Before You Begin

- Get Started With a MongoDB Deployment.

- Follow the Database Tools Installation Guide to install `mongoimport`.

- Create the example files.

  tabs:
    - id: macos
      content: |

        **Step 1: Create and Move to the `test-datasets` Directory**

        ```sh
        mkdir test-datasets

        cd test-datasets
        ```

        **Step 2: Create `.json` Example Files**

        ```sh
        echo '{
            "tripduration": 602,
            "starttime": "2019-12-01 00:00:05.5640",
            "stoptime": "2019-12-01 00:10:07.8180",
            "start station id": 3382,
            "start station name": "Carroll St & Smith St",
            "start station latitude": 40.680611,
            "start station longitude": -73.99475825,
            "end station id": 3304,
            "end station name": "6 Ave & 9 St",
            "end station latitude": 40.668127,
            "end station longitude": -73.98377641,
            "bikeid": 41932,
            "usertype": "Subscriber",
            "birth year": 1970,
            "gender": "male"
        }' > ride_01.json

        echo '{
            "tripduration": 1206,
            "starttime": "2019-12-01 00:00:10.9630",
            "stoptime": "2019-12-01 00:20:17.8820",
            "start station id": 362,
            "start station name": "Broadway & W 37 St",
            "start station latitude": 40.75172632,
            "start station longitude": -73.98753523,
            "end station id": 500,
            "end station name": "Broadway & W 51 St",
            "end station latitude": 40.76228826,
            "end station longitude": -73.98336183,
            "bikeid": 18869,
            "usertype": "Customer",
            "birth year": 1999,
            "gender": "male"
        }' > ride_02.json

        echo '{
            "tripduration": 723,
            "starttime": "2019-12-01 00:00:11.8180",
            "stoptime": "2019-12-01 00:12:14.8310",
            "start station id": 146,
            "start station name": "Hudson St & Reade St",
            "start station latitude": 40.71625008,
            "start station longitude": -74.0091059,
            "end station id": 238,
            "end station name": "Bank St & Washington St",
            "end station latitude": 40.7361967,
            "end station longitude": -74.00859207,
            "bikeid": 15334,
            "usertype": "Subscriber",
            "birth year": 1997,
            "gender": "male"
        }' > ride_03.json

        echo '[
            {
               "tripduration": 602,
               "starttime": "2019-12-01 00:00:05.5640",
               "stoptime": "2019-12-01 00:10:07.8180",
               "start station id": 3382,
               "start station name": "Carroll St & Smith St",
               "start station latitude": 40.680611,
               "start station longitude": -73.99475825,
               "end station id": 3304,
               "end station name": "6 Ave & 9 St",
               "end station latitude": 40.668127,
               "end station longitude": -73.98377641,
               "bikeid": 41932,
               "usertype": "Subscriber",
               "birth year": 1970,
               "gender": "male"
            },

            {
               "tripduration": 1206,
               "starttime": "2019-12-01 00:00:10.9630",
               "stoptime": "2019-12-01 00:20:17.8820",
               "start station id": 362,
               "start station name": "Broadway & W 37 St",
               "start station latitude": 40.75172632,
               "start station longitude": -73.98753523,
               "end station id": 500,
               "end station name": "Broadway & W 51 St",
               "end station latitude": 40.76228826,
               "end station longitude": -73.98336183,
               "bikeid": 18869,
               "usertype": "Customer",
               "birth year": 1999,
               "gender": "male"
            },

            {
               "tripduration": 723,
               "starttime": "2019-12-01 00:00:11.8180",
               "stoptime": "2019-12-01 00:12:14.8310",
               "start station id": 146,
               "start station name": "Hudson St & Reade St",
               "start station latitude": 40.71625008,
               "start station longitude": -74.0091059,
               "end station id": 238,
               "end station name": "Bank St & Washington St",
               "end station latitude": 40.7361967,
               "end station longitude": -74.00859207,
               "bikeid": 15334,
               "usertype": "Subscriber",
               "birth year": 1997,
               "gender": "male"
            }
        ]' > rides.json

        echo '602,"2019-12-01 00:00:05.5640","2019-12-01 00:10:07.8180",3382,"Carroll St & Smith St",40.680611,-73.99475825,3304,"6 Ave & 9 St",40.668127,-73.98377641,41932,"Subscriber",1970,1
            1206,"2019-12-01 00:00:10.9630","2019-12-01 00:20:17.8820",362,"Broadway & W 37 St",40.75172632,-73.98753523,500,"Broadway & W 51 St",40.76228826,-73.98336183,18869,"Customer",1999,1
            723,"2019-12-01 00:00:11.8180","2019-12-01 00:12:14.8310",146,"Hudson St & Reade St",40.71625008,-74.0091059,238,"Bank St & Washington St",40.7361967,-74.00859207,15334,"Subscriber",1997,1 
        ' > rides_no_header.json
        ```

    - id: windows
      content: |

        **Step 1: Create and Move to the `test-datasets` Directory**

        ```sh
        mkdir test-datasets

        cd test-datasets
        ```

        **Step 2: Create `.json` Example Files**

        ```sh
        @'
         {
            "tripduration": 602,
            "starttime": "2019-12-01 00:00:05.5640",
            "stoptime": "2019-12-01 00:10:07.8180",
            "start station id": 3382,
            "start station name": "Carroll St & Smith St",
            "start station latitude": 40.680611,
            "start station longitude": -73.99475825,
            "end station id": 3304,
            "end station name": "6 Ave & 9 St",
            "end station latitude": 40.668127,
            "end station longitude": -73.98377641,
            "bikeid": 41932,
            "usertype": "Subscriber",
            "birth year": 1970,
            "gender": "male"
         }
        '@ | Set-Content -Path ride_01.json

        @'
         {
            "tripduration": 1206,
            "starttime": "2019-12-01 00:00:10.9630",
            "stoptime": "2019-12-01 00:20:17.8820",
            "start station id": 362,
            "start station name": "Broadway & W 37 St",
            "start station latitude": 40.75172632,
            "start station longitude": -73.98753523,
            "end station id": 500,
            "end station name": "Broadway & W 51 St",
            "end station latitude": 40.76228826,
            "end station longitude": -73.98336183,
            "bikeid": 18869,
            "usertype": "Customer",
            "birth year": 1999,
            "gender": "male"
         }
        '@ | Set-Content -Path ride_02.json

        @'
         {
            "tripduration": 723,
            "starttime": "2019-12-01 00:00:11.8180",
            "stoptime": "2019-12-01 00:12:14.8310",
            "start station id": 146,
            "start station name": "Hudson St & Reade St",
            "start station latitude": 40.71625008,
            "start station longitude": -74.0091059,
            "end station id": 238,
            "end station name": "Bank St & Washington St",
            "end station latitude": 40.7361967,
            "end station longitude": -74.00859207,
            "bikeid": 15334,
            "usertype": "Subscriber",
            "birth year": 1997,
            "gender": "male"
         }
        '@ | Set-Content -Path ride_03.json

        @'
         [
            {
               "tripduration": 602,
               "starttime": "2019-12-01 00:00:05.5640",
               "stoptime": "2019-12-01 00:10:07.8180",
               "start station id": 3382,
               "start station name": "Carroll St & Smith St",
               "start station latitude": 40.680611,
               "start station longitude": -73.99475825,
               "end station id": 3304,
               "end station name": "6 Ave & 9 St",
               "end station latitude": 40.668127,
               "end station longitude": -73.98377641,
               "bikeid": 41932,
               "usertype": "Subscriber",
               "birth year": 1970,
               "gender": "male"
            },

            {
               "tripduration": 1206,
               "starttime": "2019-12-01 00:00:10.9630",
               "stoptime": "2019-12-01 00:20:17.8820",
               "start station id": 362,
               "start station name": "Broadway & W 37 St",
               "start station latitude": 40.75172632,
               "start station longitude": -73.98753523,
               "end station id": 500,
               "end station name": "Broadway & W 51 St",
               "end station latitude": 40.76228826,
               "end station longitude": -73.98336183,
               "bikeid": 18869,
               "usertype": "Customer",
               "birth year": 1999,
               "gender": "male"
            },

            {
               "tripduration": 723,
               "starttime": "2019-12-01 00:00:11.8180",
               "stoptime": "2019-12-01 00:12:14.8310",
               "start station id": 146,
               "start station name": "Hudson St & Reade St",
               "start station latitude": 40.71625008,
               "start station longitude": -74.0091059,
               "end station id": 238,
               "end station name": "Bank St & Washington St",
               "end station latitude": 40.7361967,
               "end station longitude": -74.00859207,
               "bikeid": 15334,
               "usertype": "Subscriber",
               "birth year": 1997,
               "gender": "male"
            }
         ]
        '@ | Set-Content -Path rides.json

        @'
         602,"2019-12-01 00:00:05.5640","2019-12-01 00:10:07.8180",3382,"Carroll St & Smith St",40.680611,-73.99475825,3304,"6 Ave & 9 St",40.668127,-73.98377641,41932,"Subscriber",1970,1
         1206,"2019-12-01 00:00:10.9630","2019-12-01 00:20:17.8820",362,"Broadway & W 37 St",40.75172632,-73.98753523,500,"Broadway & W 51 St",40.76228826,-73.98336183,18869,"Customer",1999,1
         723,"2019-12-01 00:00:11.8180","2019-12-01 00:12:14.8310",146,"Hudson St & Reade St",40.71625008,-74.0091059,238,"Bank St & Washington St",40.7361967,-74.00859207,15334,"Subscriber",1997,1
        '@ | Set-Content -Path rides_no_header.json
        ```

    - id: linux
      content: |

        **Step 1: Create and Move to the `test-datasets` Directory**

        ```sh
        mkdir test-datasets

        cd test-datasets
        ```

        **Step 2: Create `.json` Example Files**

        ```sh
        cat << 'EOF' > ride_01.json
         {
            "tripduration": 602,
            "starttime": "2019-12-01 00:00:05.5640",
            "stoptime": "2019-12-01 00:10:07.8180",
            "start station id": 3382,
            "start station name": "Carroll St & Smith St",
            "start station latitude": 40.680611,
            "start station longitude": -73.99475825,
            "end station id": 3304,
            "end station name": "6 Ave & 9 St",
            "end station latitude": 40.668127,
            "end station longitude": -73.98377641,
            "bikeid": 41932,
            "usertype": "Subscriber",
            "birth year": 1970,
            "gender": "male"
         }
        EOF

        cat << 'EOF' > ride_02.json
         {
            "tripduration": 1206,
            "starttime": "2019-12-01 00:00:10.9630",
            "stoptime": "2019-12-01 00:20:17.8820",
            "start station id": 362,
            "start station name": "Broadway & W 37 St",
            "start station latitude": 40.75172632,
            "start station longitude": -73.98753523,
            "end station id": 500,
            "end station name": "Broadway & W 51 St",
            "end station latitude": 40.76228826,
            "end station longitude": -73.98336183,
            "bikeid": 18869,
            "usertype": "Customer",
            "birth year": 1999,
            "gender": "male"
         }
        EOF

        cat << 'EOF' > ride_03.json
         {
            "tripduration": 723,
            "starttime": "2019-12-01 00:00:11.8180",
            "stoptime": "2019-12-01 00:12:14.8310",
            "start station id": 146,
            "start station name": "Hudson St & Reade St",
            "start station latitude": 40.71625008,
            "start station longitude": -74.0091059,
            "end station id": 238,
            "end station name": "Bank St & Washington St",
            "end station latitude": 40.7361967,
            "end station longitude": -74.00859207,
            "bikeid": 15334,
            "usertype": "Subscriber",
            "birth year": 1997,
            "gender": "male"
         }
        EOF

        cat << 'EOF' > rides.json
         [
            {
               "tripduration": 602,
               "starttime": "2019-12-01 00:00:05.5640",
               "stoptime": "2019-12-01 00:10:07.8180",
               "start station id": 3382,
               "start station name": "Carroll St & Smith St",
               "start station latitude": 40.680611,
               "start station longitude": -73.99475825,
               "end station id": 3304,
               "end station name": "6 Ave & 9 St",
               "end station latitude": 40.668127,
               "end station longitude": -73.98377641,
               "bikeid": 41932,
               "usertype": "Subscriber",
               "birth year": 1970,
               "gender": "male"
            },

            {
               "tripduration": 1206,
               "starttime": "2019-12-01 00:00:10.9630",
               "stoptime": "2019-12-01 00:20:17.8820",
               "start station id": 362,
               "start station name": "Broadway & W 37 St",
               "start station latitude": 40.75172632,
               "start station longitude": -73.98753523,
               "end station id": 500,
               "end station name": "Broadway & W 51 St",
               "end station latitude": 40.76228826,
               "end station longitude": -73.98336183,
               "bikeid": 18869,
               "usertype": "Customer",
               "birth year": 1999,
               "gender": "male"
            },

            {
               "tripduration": 723,
               "starttime": "2019-12-01 00:00:11.8180",
               "stoptime": "2019-12-01 00:12:14.8310",
               "start station id": 146,
               "start station name": "Hudson St & Reade St",
               "start station latitude": 40.71625008,
               "start station longitude": -74.0091059,
               "end station id": 238,
               "end station name": "Bank St & Washington St",
               "end station latitude": 40.7361967,
               "end station longitude": -74.00859207,
               "bikeid": 15334,
               "usertype": "Subscriber",
               "birth year": 1997,
               "gender": "male"
            }
         ]
        EOF

        cat << 'EOF' > rides_no_header.json
         602,"2019-12-01 00:00:05.5640","2019-12-01 00:10:07.8180",3382,"Carroll St & Smith St",40.680611,-73.99475825,3304,"6 Ave & 9 St",40.668127,-73.98377641,41932,"Subscriber",1970,1
         1206,"2019-12-01 00:00:10.9630","2019-12-01 00:20:17.8820",362,"Broadway & W 37 St",40.75172632,-73.98753523,500,"Broadway & W 51 St",40.76228826,-73.98336183,18869,"Customer",1999,1
         723,"2019-12-01 00:00:11.8180","2019-12-01 00:12:14.8310",146,"Hudson St & Reade St",40.71625008,-74.0091059,238,"Bank St & Washington St",40.7361967,-74.00859207,15334,"Subscriber",1997,1
        EOF
        ```

- Find Your MongoDB Connection String.

  **Important:**

  Your MongoDB Atlas connection string resembles the following example:

  ```sh
  mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
  ```

## Get Started with mongoimport

`mongoimport` is a command-line tool for importing data from JSON,
CSV, and TSV files into MongoDB collections. `mongoimport` can be
combined with other command-line tools such as JQ for
JSON manipulation, CSVKit for CSV manipulation, or
`curl` for dynamically downloading data files from servers on the Internet.

### Choose a Source Data Format

JSON is both a hierarchical data format, like MongoDB documents, and is also
explicit about the types of data it encodes.

CSV (and TSV) data is tabular, and each row will be imported into MongoDB as a
separate document. This means that these formats cannot support hierarchical
data in the same way as a MongoDB document can. When importing CSV data into
MongoDB, `mongoimport` attempts to make sensible choices when
identifying the type of specific field. This behavior can be overridden with
flags or type specification.

### Connect mongoimport to Your Database

Use your MongoDB Atlas connection string to connect `mongoimport` to the
`test` database and `test-collection` collection.
  

```sh
mongoimport --uri 'mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority' \
   --db=test \
   --collection=test-collection 
```

   
Successful connection to your database collection resembles the following:
   

```sh
2025-07-14T10:22:58.317-0400	connected to: mongodb+srv://cluster0.zoikgns.mongodb.net/
2025-07-14T10:23:01.318-0400	test.test-collection	0B
2025-07-14T10:23:04.318-0400	test.test-collection	0B
...
```

After you successfully connect to your database collection, follow the examples
to learn how to use `mongoimport` to import data into MongoDB.

## Steps

The following examples show you how to:

- mongoimport-guide-import-one

- mongoimport-guide-import-many

- mongoimport-guide-import-json-array

- mongoimport-guide-import-mongodb-specific-types

- mongoimport-guide-import-csv-with-fields

- mongoimport-guide-import-csv-with-fields-and-types

### Import Documents with --file

Use the `--file` option to specify the location and name of the file
containing the data to import into a MongoDB collection.

The following example imports the `ride_01.json` file into the new collection,
`test-collection`, in the `test` database by providing the file's path
`--file=ride_01.json`.

```sh
mongoimport --uri 'mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority' \
  --db=test \
  --collection=test-collection \
  --file=ride_01.json
```

Successful import resembles the following:
   

```sh
2025-07-14T11:47:01.303-0400	connected to: mongodb+srv://[**REDACTED**]@cluster0.zoikgns.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
2025-07-14T11:47:01.391-0400	1 document(s) imported successfully. 0 document(s) failed to import.
```

To view the successful data import, you can use the 
Atlas UI.

(Figure: /images/import-one-json-doc-mongoimport.png)

**Note:**

For each imported document, MongoDB generates a required unique 
_id value.

If you do not specify a file, `mongoimport` reads data from
standard input (e.g. `stdin`). The following example demonstrates how to
import multiple documents by piping them to `mongoimport`, which
then reads the data from `stdin`.

```sh
echo "{\"bikeid\":\"1234\"}\n{\"bikeid\":\"5678\"}" | mongoimport --uri 'mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority' \
  --db=test \
  --collection=test-collection-stdin
```

Successful import resembles the following:
   

```sh
2025-07-14T11:08:08.884-0600	connected to: mongodb+srv://[**REDACTED**]@cluster0.zoikgns.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
2025-07-14T11:08:09.095-0600	2 document(s) imported successfully. 0 document(s) failed to import.
```

### Import Documents with Piping

You can pipe multiple JSON documents from another tool, such as `cat`, to
import multiple files with `mongoimport`. From the directory that
contains the JSON files for import, you can run the following command to import
the documents.

```sh
cat *_*.json | mongoimport --uri 'mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority' \
  --db=test \
  --collection=test-collection-many
```

Successful import resembles the following:
   

```sh
2025-07-21T16:48:23.519-0400	connected to: mongodb+srv://[**REDACTED**]@cluster0.zoikgns.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
2025-07-21T16:48:23.627-0400	3 document(s) imported successfully. 0 document(s) failed to import.
```

### Import a JSON Array

To import a JSON array of documents, you can use the `--jsonArray` option to specify the format of the data. You specify
the data source, which can be a file or standard input, separately. The
following example imports the `rides.json` file containing a single JSON
array.

```sh
mongoimport --uri 'mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority' \
  --db=test \
  --collection=test-collection-array \
  --file=rides.json \
  --jsonArray
```

Successful import resembles the following:
   

```sh
2025-07-14T11:48:10.829-0400	connected to: mongodb+srv://[**REDACTED**]@cluster0.zoikgns.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
2025-07-14T11:48:10.899-0400	3 document(s) imported successfully. 0 document(s) failed to import.
```

If you do not add the `--jsonArray` option, `mongoimport`
will fail with the error `cannot decode array into a Document` because MongoDB
documents are comparable to JSON objects, not arrays.

**Note:**

You can store an array as a value in a document, but a document cannot be
an array.

### Import MongoDB-Specific Types with JSON

Since MongoDB stores data as BSON, you must use
Extended JSON to recognize fields imported as
JSON as specific BSON types. This means you can provide a field MongoDB
originally recognizes as a `string` in the following nested structure to have
MongoDB recognize it as a `date` type.

```sh
"starttime": {
   "$date": "2019-12-01T00:00:05.5640Z"
}
```

To transform your existing data, see the section on mongoimport-jq.

### Import CSV or TSV Into a Collection with Specified Field Types

If you have CSV or TSV files to import, use the `--type=csv` or `--type=tsv`, respectively, to tell
`mongoimport` the format to expect.

If your CSV or TSV file has a header row, use the `--headerline` option to tell `mongoimport` the first
line should not be imported as a document.

Since CSV and TSV data does not include type information, you can solve this by
specifying field types when you call `mongoimport`. The first way
to provide `mongoimport` with type information is if you list the
field names on the command line with the `--fields` option.

```sh
mongoimport --uri 'mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority' \
   --db=test \
   --collection=test-field-file \
   --file=rides_no_header.csv \
   --type=csv \
   --fields="tripduration","starttime","stoptime","start station id","start station name","start station latitude","start station longitude","end station id","end station name","end station latitude","end station longitude","bikeid","usertype","birth year","gender"
```

Another way to provide `mongoimport` with type information is if
you put the field names in a file, such as `field_file.txt`, and point to it with the `--fieldFile` option.

tabs:
  - id: macos
    content: |

     ```sh
     echo 'tripduration
     starttime
     stoptime
     start station id
     start station name
     start station latitude
     start station longitude
     end station id
     end station name
     end station latitude
     end station longitude
     bikeid
     usertype
     birth year
     gender' > field_file.txt
     ```

  - id: linux
    content: |

     ```sh
     cat << 'EOF' > field_file.txt
     tripduration
     starttime
     stoptime
     start station id
     start station name
     start station latitude
     start station longitude
     end station id
     end station name
     end station latitude
     end station longitude
     bikeid
     usertype
     birth year
     gender
     EOF
     ```

  - id: windows
    content: |

     ```sh
     @"
     tripduration
     starttime
     stoptime
     start station id
     start station name
     start station latitude
     start station longitude
     end station id
     end station name
     end station latitude
     end station longitude
     bikeid
     usertype
     birth year
     gender
     "@ | Set-Content -Path field_file.txt
     ```

```sh
mongoimport --uri 'mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority' \
   --db=test \
   --collection=test-field-file \
   --file=rides_no_header.csv \
   --type=csv \
   --fieldFile=field_file.txt
```

Successful import for the `--fields` and
`--fieldFile` options resemble the following:
   

```sh
2025-07-14T11:48:10.829-0400	connected to: mongodb+srv://[**REDACTED**]@cluster0.zoikgns.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
2025-07-14T11:48:10.899-0400	3 document(s) imported successfully. 0 document(s) failed to import.
```

To view the successful data import, you can use the 
Atlas UI.

(Figure: /images/import-test-field-file-mongoimport.png)

### Import CSV or TSV Into a Collection with Specified Field and Data Types

Above, you can see that `mongoimport` automatically makes decisions
on data types. To instead specify the type of some or all of your fields, you
can use the `--columnsHaveTypes`
option, or add types to the file you use with the `--fieldFile` option.

tabs:
  - id: macos
    content: |

     ```sh
     echo 'tripduration.auto()
     starttime.date(2006-01-02 15:04:05)
     stoptime.date(2006-01-02 15:04:05)
     start station id.auto()
     start station name.auto()
     start station latitude.auto()
     start station longitude.auto()
     end station id.auto()
     end station name.auto()
     end station latitude.auto()
     end station longitude.auto()
     bikeid.auto()
     usertype.auto()
     birth year.auto()
     gender.auto()' > field_file_with_types.txt
     ```

  - id: linux
    content: |

     ```sh
     cat << 'EOF' > field_file_with_types.txt
     tripduration.auto()
     starttime.date(2006-01-02 15:04:05)
     stoptime.date(2006-01-02 15:04:05)
     start station id.auto()
     start station name.auto()
     start station latitude.auto()
     start station longitude.auto()
     end station id.auto()
     end station name.auto()
     end station latitude.auto()
     end station longitude.auto()
     bikeid.auto()
     usertype.auto()
     birth year.auto()
     gender.auto()
     EOF
     ```

  - id: windows
    content: |

     ```sh
     @"
     tripduration.auto()
     starttime.date(2006-01-02 15:04:05)
     stoptime.date(2006-01-02 15:04:05)
     start station id.auto()
     start station name.auto()
     start station latitude.auto()
     start station longitude.auto()
     end station id.auto()
     end station name.auto()
     end station latitude.auto()
     end station longitude.auto()
     bikeid.auto()
     usertype.auto()
     birth year.auto()
     gender.auto()
     "@ | Set-Content -Path field_file_with_types.txt
     ```

```sh
mongoimport --uri 'mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority' \
   --db=test \
   --collection=test-field-file \
   --file=test-datasets/rides_no_header.csv \
   --type=csv \
   --fieldFile=field_file_with_types.txt
```

Successful import resembles the following:
   

```sh
2025-07-14T11:48:10.829-0400	connected to: mongodb+srv://[**REDACTED**]@cluster0.zoikgns.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
2025-07-14T11:48:10.899-0400	3 document(s) imported successfully. 0 document(s) failed to import.
```

To view the successful data import, you can use the 
Atlas UI.

(Figure: /images/import-field-file-with-types-mongoimport.png)

Now, you can see that `mongoimport` uses the data types you provide
to store the imported file.

## Useful Command-line Tools

You can use other command-line programs alongside `mongoimport` to
further streamline your data import.

JQ
~~

JQ is a processor for JSON data. It incorporates a powerful filtering and
scripting language for filtering, manipulating, and generating JSON data. You
can use a multi-stage pipe to pipe data into `mongoimport` via JQ.
To learn more about how to use JQ, see the [JQ Manual](https://jqlang.org/manual/). 

### CSVKit

CSVKit is a collection of tools for filtering and manipulating CSV data. CSVKit
tools such as `csvgrep`, which filters rows based on expressions, and
`csvcut`, which removes whole columns from CSV input, are useful tools for
slicing data before providing it to `mongoimport`. To learn
more about how to use CSVKit, see the 
[CSVKit Documentation](https://csvkit.readthedocs.io/en/latest/index.html).

## Learn More

- See our mongoimport documentation for more details on possible options.
