use std::fs;
use std::collections::HashMap;
use advent2019::{Intcode, Status};

fn create_program(ops: &HashMap<i64, i64>, v1: i64, v2: i64) -> Intcode {
    let mut new_ops = ops.clone();
    new_ops.insert(1, v1);
    new_ops.insert(2, v2);
    return Intcode{
        program: new_ops,
        status: Status::RUNNING,
        pc: 0,
        output: Vec::new(),
        input: Vec::new(),
        relative_base: 0
    };

}

fn main() {
    let data = fs::read_to_string("input-02.txt").expect("Unable to read file");

    let mut program: HashMap<i64, i64> = HashMap::new();

    for (i, word) in data.trim().split(",").enumerate() {
        program.insert(i as i64, word.parse().expect("Parse error"));
    }

    //Part 1
    let mut intcode = create_program(&program, 12, 2);

    intcode.run();

    println!("{}", intcode.program[&0]);

    'outer: for noun in 0..100 {
        for verb in 0..100 {
            intcode = create_program(&program, noun, verb);
            intcode.run();
            if intcode.program[&0] == 19690720 {
                println!("{}", 100*noun + verb);
                break 'outer;
            }

        }
    }
}