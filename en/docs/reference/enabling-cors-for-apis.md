# Enabling CORS for APIs

Cross-Origin Resource Sharing (CORS) is a mechanism that allows accessing restricted resources (i.e., fonts, images, scripts, videos, and iframes) from domains outside the domain from which the requesting resource originated. Browsers define the origin as a combination of Scheme (`http://`, `https://`), Host, and Port. By default, web browsers apply the same-origin policy to avoid interactions between different origins. CORS defines a way in which a browser and a server can interact to determine whether or not it is safe to allow the cross-origin requests.

In MI, you can enable Cross-Origin Resource Sharing per API or as a global configuration that is applied across all APIs.

-   [Enabling CORS Globally](#EnablingCORSGlobally)
-   [Enabling CORS Per API](#EnablingCORSPerAPI)

<a name="EnablingCORSGlobally"></a>

## Enabling CORS Globally

You can enable CORS globally for MI by configuring the `deployment.toml` file, which is located in the `<MI_HOME>/repository/conf/` directory.

Follow the instructions below to enable CORS response headers globally. Once this configuration is enabled, it will be applied across all the APIs in the runtime.

1.  Open the `<MI_HOME>/conf/deployment.toml` file.
2.  Locate the following configuration and set the `enable` attribute to `true` with the required CORS headers in the response. 
     After this configuration is applied in the API Gateway, it will affect all the API calls served by the Gateway.

    ``` toml
    [apim.cors]
    enable = true
    allow_origins = "*"
    allow_methods = ["GET","PUT","POST","DELETE","PATCH","OPTIONS"]
    allow_headers = ["authorization","Access-Control-Allow-Origin","Content-Type","SOAPAction","apikey","Internal-Key"]
    allow_credentials = false
    ```

!!! info
    CORS configuration is enabled by default. Access control can be done by changing the parameters mentioned above in the `deployment.toml` file.



