use std::fs;


fn calibration_value(line: &str) -> u32 {
    let chars: Vec<char> = line.chars().collect();
    let digits: Vec<&char> = chars.iter().filter(|x| x.is_digit(10)).collect();
    let first = *digits[0];
    let last: char;
    if digits.len() > 1 {
        last = *digits[digits.len() - 1];
    } else {
        last = *digits[0];
    }

    let mut s = String::new();
    s.push(first);
    s.push(last);
    
    return s.parse().expect("Invalid string");
}

fn calibration_value_p2(line: &str) -> u32 {
    let first: u32 = first_digit(line);
    let second: u32 = last_digit(line);
    return 10*first + second;
}

//this is so bad
fn first_digit(line: &str) -> u32 {
    if line.len() == 0 {
        return 0
    } else if line.starts_with("one") {
        return 1;
    } else if line.starts_with("two") {
        return 2;
    } else if line.starts_with("three") {
        return 3;
    } else if line.starts_with("four"){
        return 4;
    } else if line.starts_with("five"){
        return 5;
    } else if line.starts_with("six"){
        return 6;
    } else if line.starts_with("seven"){
        return 7;
    } else if line.starts_with("eight"){
        return 8;
    } else if line.starts_with("nine"){
        return 9;
    } else {
        let chars: Vec<char> = line.chars().collect();
        if chars[0].is_digit(10) {
            return chars[0].to_digit(10).expect("Error - invalid parse somehow");
        } else {
            return first_digit(&line[1..]);
        }
    }
}

fn last_digit(line: &str) -> u32 {
    if line.len() == 0 {
        return 0;
    } else if line.ends_with("one") {
        return 1;
    } else if line.ends_with("two") {
        return 2;
    } else if line.ends_with("three") {
        return 3;
    } else if line.ends_with("four") {
        return 4;
    } else if line.ends_with("five") {
        return 5;
    } else if line.ends_with("six") {
        return 6;
    } else if line.ends_with("seven") {
        return 7;
    } else if line.ends_with("eight") {
        return 8;
    } else if line.ends_with("nine") {
        return 9;
    } else {
        let chars: Vec<char> = line.chars().collect();
        if chars[chars.len()-1].is_digit(10){
            return chars[chars.len()-1].to_digit(10).expect("Error - invalid parse somehow");
        } else {
            return last_digit(&line[..line.len()-1]);
        }
    }
}

fn main() {
    let words = fs::read_to_string("input-01.txt")
        .expect("Unable to read file");

    let mut total_value: u32 = 0;
    let mut total_value_p2: u32 = 0;
    for word in words.lines() {
        total_value += calibration_value(word);
        total_value_p2 += calibration_value_p2(word);
        
    }

    println!("{}", total_value);
    println!("{}", total_value_p2);


}