use std::fs;
use regex::Regex;

fn count(s: &String, target: char) -> usize {
    let mut count: usize = 0;

    for c in s.chars() {
        if c == target {
            count += 1;
        }
    }

    count
}

fn parse_line(line: &str) -> (usize, usize, char, String) {
    let re = Regex::new(r"(\d+)-(\d+) ([a-zA-Z]): ([a-zA-Z]+)").unwrap();
    let caps = re.captures(line).unwrap();

    let num1: usize = caps[1].parse().unwrap();
    let num2: usize = caps[2].parse().unwrap();
    let c = caps[3].chars().collect::<Vec<_>>()[0]; 
    let pw = String::from(&caps[4]);

    (num1, num2, c, pw)
}

fn main() {
    let data = fs::read_to_string("input-02.txt").expect("Unable to open file");

    let parsed: Vec<(usize, usize, char, String)> = data.lines().map(|x| parse_line(x)).collect();

    let mut valid_count: u32 = 0;

    for (low, high, target, pw) in parsed.iter() {
        let char_count = count(pw, *target);
        if *low <= char_count && char_count <= *high {
            valid_count += 1;
        }
    }

    println!("{valid_count}");

    valid_count = 0;

    for (low, high, target, pw) in parsed.iter() {
        let chars: Vec<char> = pw.chars().collect();
        if (chars[*low-1] == *target) ^ (chars[*high-1] == *target) {
            valid_count += 1;
        }
    }

    println!("{valid_count}");
}