use dotenv::dotenv;
use std::env;
use std::fs;
use std::path::Path;

fn get_filepaths_in_dir(dir_path: String) -> std::io::Result<Vec<String>> {
    let mut filepaths = Vec::new();
    let path = Path::new(&dir_path);

    if path.is_dir() {
        for entry in fs::read_dir(path)? {
            let entry = entry?;
            let path = entry.path();

            if path.is_file() {
                if let Some(path_str) = path.to_str() {
                    filepaths.push(path_str.to_string());
                }
            }
        }
    }

    Ok(filepaths)
}

fn main() {
    dotenv().ok();
    let dir_path = env::var("DATA_DIR").expect("No DATA_DIR is set!");
    println!("Using data directory {}", dir_path);
    let files = get_filepaths_in_dir(dir_path).unwrap();
    for file in files {
        println!("Found {file:?}");
    }
}
