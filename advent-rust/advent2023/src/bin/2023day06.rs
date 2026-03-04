use std::fs;

fn ways_to_beat(length: i64, record: i64) -> u64 {
    let mut count: u64 = 0;

    for i in 0..=length {
        if i * (length-i) > record {
            count += 1;
        }
    }

    count
}
fn main() {
    let data = fs::read_to_string("input-06.txt").expect("Unable to read file");
    let lines: Vec<&str> = data.split("\n").collect();
    let times: Vec<&str> = lines[0].split_whitespace().collect();
    let records: Vec<&str> = lines[1].split_whitespace().collect();

    let mut product = 1;
    for i in 1..times.len() {
        product *= ways_to_beat(times[i].parse().unwrap(), records[i].parse().unwrap());
    }
    println!("{product}");

    let mut time = String::from("");
    let mut rec = String::from("");
    for i in 1..times.len() {
        time.push_str(times[i]);
        rec.push_str(records[i]);
    }
    //There's definitly a better way to do this
    //Using the quadratic formula, probably
    //Don't want to fiddle with making sure float precision isn't a problem, though
    //it would probably be fine
    println!("{}", ways_to_beat(time.parse().unwrap(), rec.parse().unwrap()));
}