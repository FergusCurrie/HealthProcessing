# HealthProcessing
Apple health metrics processing. 

Note: export.xml is a subset of export_cda.xml so we only process export.xml. 
To use:
1. Export from apple data, will get a a zip export.zip
2. Unzip and remove the top export.xmlof the file so that it begins with :
```
    <?xml version="1.0" encoding="UTF-8"?>
<HealthData locale="en_NZ">
 <ExportDate value="2023-02-06 13:25:18 +1300"/>
```
3. Use xml parser functoin parsing the path of export.xml
4. Boom. The saved csv is the cleaned data. Delete zips and folder s