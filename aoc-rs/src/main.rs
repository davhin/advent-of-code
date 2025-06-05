use dotenv::dotenv;
use std::env;

fn get_filepaths_in_dir(dir_path: String) -> std::io::Result<Vec<String>> {
    let mut filepaths = Vec::new();
    Ok(filepaths)
}

fn main() {
    dotenv().ok();
    let dir_path = env::var("DATA_DIR").expect("No DATA_DIR is set!");
    println!("Using data directory {}", dir_path);
}
