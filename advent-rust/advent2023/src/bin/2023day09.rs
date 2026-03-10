use std::fs;

fn get_differences(seq: &Vec<i64>) -> Vec<i64> {
    let mut differences: Vec<i64> = Vec::new();
    for i in 1..seq.len() {
        differences.push(seq[i] - seq[i-1]);
    }

    differences
}

fn extrapolate_next(seq: &Vec<i64>) -> i64 {
    if seq.iter().all(|x| *x==0) {
        0
    } else {
        seq.last().unwrap() + extrapolate_next(&get_differences(seq))
    }
}

fn extrapolate_previous(seq: &Vec<i64>) -> i64 {
    if seq.iter().all(|x| *x == 0) {
        0
    } else {
        seq.first().unwrap() - extrapolate_previous(&get_differences(seq))
    }

}

fn parse_sequence(line: &str) -> Vec<i64> {
    let mut result: Vec<i64> = Vec::new();

    for num in line.split_whitespace() {
        result.push(num.parse().expect("Unable to parse"));
    }

    result
}

fn main() {

    //Read and parse input
    let data = fs::read_to_string("input-09.txt").expect("Unable to read file");
    let mut sequences: Vec<Vec<i64>> = Vec::new();
    for line in data.lines() {
        sequences.push(parse_sequence(line));
    }

    let mut total = 0;
    for sequence in sequences.iter() {
        total += extrapolate_next(&sequence);

    }

    println!("{total}");

    total = 0;
    for sequence in sequences {
        total += extrapolate_previous(&sequence);
    }

    println!("{total}");
}