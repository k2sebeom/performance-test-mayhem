use actix_web::{web, App, HttpResponse, HttpServer, Responder};
use serde_json::json;

async fn greet() -> impl Responder {
    let response_data = json!({"hello": "world"});
    HttpResponse::Ok().content_type("application/json").body(response_data.to_string())
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().route("/", web::get().to(greet)))
        .bind("127.0.0.1:8000")?
        .run()
        .await
}
