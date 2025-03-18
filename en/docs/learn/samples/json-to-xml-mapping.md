# JSON to XML Mapping Sample

This sample demonstrates the JSON to XML data mapping capability of the Datamapper engine in WSO2 MI runtime.

This sample contains a REST API called ‘SalesforceLeads’. The Registry contains data mapper configuration files. 

The REST API transforms the JSON message into a XML message using the Data Mapper mediator and responds back the client with the transformed payload.

## Deploying the sample

1.  Open the sample by clicking on the **JSON to XML Mapping** card.
2.  Give a folder location to save the sample.
3.  [Build and run]({{base_path}}/develop/deploy-artifacts#build-and-run) the sample in your Micro Integrator.

## Running the sample

1. Open a terminal and run the following commands to invoke the API.

```bash
curl --location --request POST 'http://localhost:8290/SalesforceLeads' \
--header 'Content-Type: application/json' \
--data '{
  "lead": [
    {
      "ID": "12345",
      "name": "John Doe",
      "city": "New York",
      "code": "NY",
      "country": "USA"
    },
    {
      "ID": "67890",
      "name": "Jane Smith",
      "city": "Los Angeles",
      "code": "LA",
      "country": "USA"
    }
  ],
  "sendNotificationEmail": "true",
  "convertedStatus": "converted",
  "doNotCreateOpportunity": "false",
  "opportunityName": "New Opportunity",
  "overwriteLeadSource": "true",
  "sessionId": "fghij67890"
}'
```

2. You will get the transformed response like below. 

```xml
<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope/" xmlns:urn="urn:enterprise.soap.sforce.com">
    <soapenv:Body>
        <urn:convertLead>
            <urn:leadConverts>
                <urn:convertedStatus>true</urn:convertedStatus>
                <urn:leadId>12345</urn:leadId>
                <urn:opportunityName>John Doe</urn:opportunityName>
            </urn:leadConverts>
            <urn:leadConverts>
                <urn:convertedStatus>true</urn:convertedStatus>
                <urn:leadId>67890</urn:leadId>
                <urn:opportunityName>Jane Smith</urn:opportunityName>
            </urn:leadConverts>
            <urn:overwriteLeadSource>true</urn:overwriteLeadSource>
            <urn:sendNotificationEmail>true</urn:sendNotificationEmail>
        </urn:convertLead>
    </soapenv:Body>
    <soapenv:Header>
        <urn:SessionHeader>
            <urn:sessionId>fghij67890</urn:sessionId>
        </urn:SessionHeader>
    </soapenv:Header>
</soapenv:Envelope>
```
