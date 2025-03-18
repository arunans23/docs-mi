# XML to JSON Mapping

This sample demonstrates the XML to JSON data mapping capability of the Datamapper engine in WSO2 MI runtime.

This sample contains a REST API called ‘EngineerEmployeeServiceAPI’. The Registry contains data mapper configuration files. 

The REST API transforms the JSON message into a XML message using the Data Mapper mediator and responds back the client with the transformed payload.

## Deploying the sample

1.  Open the sample by clicking on the **XML to JSON Mapping** card.
2.  Give a folder location to save the sample.
3.  [Build and run]({{base_path}}/develop/deploy-artifacts#build-and-run) the sample in your Micro Integrator.

## Running the sample

1. Open a terminal and run the following commands to invoke the API.

```bash
curl --location --request POST 'http://localhost:8290/employeeservice' \
--header 'Content-Type: application/xml' \
--data '<ns1:employees xmlns:ns1="http://wso2.employee.info" xmlns:ns2="http://wso2.employee.address">
    <ns1:employee>
        <ns1:firstname>Mike</ns1:firstname>
        <ns1:lastname>Jhonson</ns1:lastname>
        <ns2:addresses>
            <ns2:address location="home">
                <ns2:city postalcode="30000">KS</ns2:city>
                <ns2:road>main rd</ns2:road>
            </ns2:address>
            <ns2:address location="office">
                <ns2:city postalcode="10003">NY</ns2:city>
                <ns2:road>cross street</ns2:road>
            </ns2:address>
        </ns2:addresses>
    </ns1:employee>
    <ns1:employee>
        <ns1:firstname>Patric</ns1:firstname>
        <ns1:lastname>Jane</ns1:lastname>
        <ns2:addresses>
            <ns2:address location="home">
                <ns2:city postalcode="60000">Melborne</ns2:city>
                <ns2:road>park street</ns2:road>
            </ns2:address>
            <ns2:address location="office">
                <ns2:city postalcode="10003">NY</ns2:city>
                <ns2:road>cross street</ns2:road>
            </ns2:address>
        </ns2:addresses>
    </ns1:employee>
    <ns1:employee>
        <ns1:firstname>Thelesa</ns1:firstname>
        <ns1:lastname>Lisbon</ns1:lastname>
        <ns2:addresses>
            <ns2:address location="home">
                <ns2:city postalcode="60000">Madrid</ns2:city>
                <ns2:road>Palace street</ns2:road>
            </ns2:address>
            <ns2:address location="office">
                <ns2:city postalcode="10003">NY</ns2:city>
                <ns2:road>cross street</ns2:road>
            </ns2:address>
        </ns2:addresses>
    </ns1:employee>
</ns1:employees>'
```

2. 2. You will get the transformed response like below. 

```bash
{
    "engineers": {
        "engineerList": [
            {
                "addresses": {
                    "address": [
                        {
                            "road": "main rd",
                            "city": {
                                "postalcode": 30000
                            },
                            "location": "HOME"
                        },
                        {
                            "road": "cross street",
                            "city": {
                                "postalcode": 10003
                            },
                            "location": "OFFICE"
                        }
                    ]
                },
                "fullname": "Mike Jhonson"
            },
            {
                "addresses": {
                    "address": [
                        {
                            "road": "park street",
                            "city": {
                                "postalcode": 60000
                            },
                            "location": "HOME"
                        },
                        {
                            "road": "cross street",
                            "city": {
                                "postalcode": 10003
                            },
                            "location": "OFFICE"
                        }
                    ]
                },
                "fullname": "Patric Jane"
            },
            {
                "addresses": {
                    "address": [
                        {
                            "road": "Palace street",
                            "city": {
                                "postalcode": 60000
                            },
                            "location": "HOME"
                        },
                        {
                            "road": "cross street",
                            "city": {
                                "postalcode": 10003
                            },
                            "location": "OFFICE"
                        }
                    ]
                },
                "fullname": "Thelesa Lisbon"
            }
        ]
    }
}
```

