# ccsu-opendata
Frequency analysis database for CCSU Exams
This repo contains frequency analysis data on topics that appeared in CCSU Exams. This data is freely accessible/editable/exploitable under the Open Data initiative.

## Directory Structure
Relative to the root of the repo, the data is store at following path:
```
/{CourseName}/{SubjectCode}.json
```
Where `CourseName` is name of the course (for e.g. `BCA`), and SubjectCode is the three digit code for each subject (for e.g. `503`)

## Schema
The schema is available in the `schema.json` file.

## Contributions
As of yet, data is only available for the `BCA` course. Contributions for other courses will appreciated.

## Testing
The json files must follow the schema defined in `schema.json`. To test the compliance of your changes locally, use the `go` testing tools.
Follow the following steps:
1. Download and install `go` from https://go.dev/dl/
2. Run `go test` in the repo's root
