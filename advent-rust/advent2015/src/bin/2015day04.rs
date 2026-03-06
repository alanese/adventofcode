use std::fs;

fn main() {
    let data = fs::read_to_string("input-04.txt").expect("Unable to read file");

    let mut next_num: u32 = 1;

    let mut key = format!("{data}{next_num}");
    let mut digest = md5::compute(key);

    while !(format!("{digest:x}").starts_with("00000")) {
        next_num += 1;
        key = format!("{data}{next_num}");
        digest = md5::compute(key);
    } 
    println!("{next_num}");

    while !format!("{digest:x}").starts_with("000000") {
        next_num += 1;
        key = format!("{data}{next_num}");
        digest = md5::compute(key);
    }
    println!("{next_num}");
}