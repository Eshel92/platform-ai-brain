<!-- Converted from performance-advisor/drop-indexes.txt (reStructuredText). Includes are inlined. -->

# Review Drop Index Recommendations

The Performance Advisor suggests dropping unused, redundant, and hidden 
indexes to improve write performance and increase storage space. 

**See also:**

To learn more about the impact of unnecessary indexes, see 
indexes-anti-pattern.

## Unused Indexes

An index is unused if it doesn't support any queries.

The Performance Advisor flags an index as unused if it hasn't supported 
a query in 7 or more days after it was created or the server was 
restarted.

## Redundant Indexes

An index is redundant if another index supports any query that it could.

The Performance Advisor flags an index as redundant if it matches the 
prefix of another index in the same collection.

**Example:**

If a collection contains the indexes:

- `{ a: 1 }`
- `{ b: -1 }`
- `{ a: 1, b: -1 }`

`{ a: 1 }` is redundant because it matches the prefix 
`{ a: 1, b: -1 }`.

`{ b: -1 }` is not redundant because it does not match any prefix.

In the Performance Advisor, redundant indexes are marked with a red 
`Redundant` badge. Below each redundant index, the Performance 
Advisor displays the related indexes that cover it.

**Note:**

Related indexes are displayed for you to verify that the redundant 
index can be dropped safely. Related indexes are not recommended 
for removal.

## Hidden Indexes

*New in MongoDB version 4.4*

Hidden indexes aren't used to support queries. They still impact write 
performance and consume storage space.

Hiding an index is useful for evaluating the impact of removing an 
index before doing so. Unhiding an index is much easier than 
rebuilding a deleted index.

**See also:**

To learn more about hidden indexes, see 
Hidden Indexes in the MongoDB manual.

To hide an index with the Performance Advisor, see 
Drop or Hide an Index.

To unhide an index, see 
Unhide an Existing Index 
in the MongoDB manual.

The Performance Advisor always recommends dropping hidden indexes. 
After you are confident a hidden index is unnecessary, drop it.

## Drop or Hide an Index

**Note:**

MongoDB recommends hiding indexes before you 
drop them. Hidden Indexes are available in 
MongoDB version 4.4 and higher.

To drop or hide an index with the Performance Advisor:

**Step 1: Navigate to the Performance Advisor Drop Indexes recommendations.**

In the Performance Advisor tab, click 
View Recommendations on the Drop Indexes card.

**Step 2: On the index you want to drop or hide, click Drop Index.**

The Performance Advisor displays a dialog with a link to 
Data Explorer and a copyable 
`MongoDB Shell` command to drop that index.

In MongoDB 4.4 and higher, the dialog also provides a copyable 
MongoDB Shell command to hide that index.

**Step 3: Drop or hide the index through Data Explorer or MongoDB Shell.**

To drop an index with Data Explorer, click the 
Indexes tab, then click Drop next to the 
index you want to drop. You will be asked for confirmation.

To drop or hide an index with MongoDB Shell, paste and run the 
command provided by the Performance Advisor.
