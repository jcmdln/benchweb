use dropshot::endpoint;
use dropshot::ApiDescription;
use dropshot::ConfigDropshot;
use dropshot::ConfigLogging;
use dropshot::ConfigLoggingLevel;
use dropshot::HttpError;
use dropshot::HttpResponseOk;
use dropshot::HttpServerStarter;
use dropshot::RequestContext;

#[tokio::main]
async fn main() -> Result<(), String> {
    let config_logging = ConfigLogging::StderrTerminal {
        level: ConfigLoggingLevel::Warn,
    };
    let log = config_logging
        .to_logger("rust-dropshot")
        .map_err(|error| format!("failed to create logger: {}", error))?;

    let mut api = ApiDescription::new();
    api.register(hello_world).unwrap();

    let server = HttpServerStarter::new(
        &ConfigDropshot {
            bind_address: "0.0.0.0:5150".parse().unwrap(),
            request_body_max_bytes: 1024,
            tls: None,
        },
        api,
        (),
        &log,
    )
    .map_err(|error| format!("failed to create server: {}", error))?
    .start();

    server.await
}

#[allow(unused_variables)]
#[endpoint {
    method = GET,
    path = "/",
}]
async fn hello_world(rqctx: RequestContext<()>) -> Result<HttpResponseOk<String>, HttpError> {
    Ok(HttpResponseOk("Hello, world!".to_string()))
}
