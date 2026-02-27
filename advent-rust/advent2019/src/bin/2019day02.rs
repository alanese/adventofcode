use std::fs;
use advent2019::Intcode;

fn create_program(ops: &Vec<usize>, v1: usize, v2: usize) -> Intcode {
    let mut new_ops = ops.clone();
    new_ops[1] = v1;
    new_ops[2] = v2;
    return Intcode{
        program: new_ops,
        running: true,
        pc: 0
    };

}

fn main() {
    let data = fs::read_to_string("input-02.txt").expect("Unable to read file");

    let mut program: Vec<usize> = Vec::new();

    for word in data.trim().split(",") {
        program.push(word.parse().expect("Parse error"));
    }

    //Part 1
    let mut intcode = create_program(&program, 12, 2);

    intcode.run();

    println!("{}", intcode.program[0]);

    'outer: for noun in 0usize..100 {
        for verb in 0usize..100 {
            intcode = create_program(&program, noun, verb);
            intcode.run();
            if intcode.program[0] == 19690720 {
                println!("{}", 100*noun + verb);
                break 'outer;
            }

        }
    }
}