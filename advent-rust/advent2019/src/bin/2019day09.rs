use std::fs;
use std::collections::HashMap;
use advent2019::{Intcode, Status};

fn main() {
    //Read and parse data
    let data = fs::read_to_string("input-09.txt").expect("Unable to read file");

    let mut program: HashMap<i64, i64> = HashMap::new();

    for (i, num) in data.split(",").enumerate() {
        program.insert(i as i64, num.parse().expect("Bad parse"));
    }

    //Part 1
    let mut machine = Intcode{
        program: program.clone(),
        status: Status::RUNNING,
        pc: 0,
        output: Vec::new(),
        input: vec![1],
        relative_base: 0
    };

    machine.run();

    println!("{:?}", machine.output);

    machine = Intcode {
        program: program.clone(),
        status: Status::RUNNING,
        pc: 0,
        output: Vec::new(),
        input: vec![2],
        relative_base: 0
    };

    machine.run();

    println!("{:?}", machine.output);
}