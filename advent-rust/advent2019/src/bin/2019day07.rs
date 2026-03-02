use std::fs;
use advent2019::{Intcode, Status};
use std::collections::HashMap;
use itertools::Itertools;

fn get_signal(program: &HashMap<i64, i64>, phase: i64, input: i64) -> i64 {
    let mut machine = Intcode::create(program.clone());
    machine.push_input(phase);
    machine.push_input(input);
    /*
    let mut machine = Intcode {
        program: program.clone(),
        status: Status::Running,
        pc: 0,
        output: Vec::new(),
        input: vec![phase, input],
        relative_base: 0
    };
    */

    machine.run();
    return machine.pop_output().unwrap();
}

fn run_p2(program: &HashMap<i64,i64>, phases: &Vec<i64>, input: i64) -> i64 {
    let mut amp_a = Intcode::create(program.clone());
    amp_a.push_input(phases[0]);
    amp_a.push_input(input);
    let mut amp_b = Intcode::create(program.clone());
    amp_b.push_input(phases[1]);
    let mut amp_c = Intcode::create(program.clone());
    amp_c.push_input(phases[2]);
    let mut amp_d = Intcode::create(program.clone());
    amp_d.push_input(phases[3]);
    let mut amp_e = Intcode::create(program.clone());
    amp_e.push_input(phases[4]);

    let mut final_output: i64 = 0;

    while amp_a.get_status() != Status::Halted && amp_b.get_status() != Status::Halted && amp_c.get_status() != Status::Halted
        && amp_d.get_status() != Status::Halted && amp_e.get_status() != Status::Halted {
        amp_a.run();
        while amp_a.has_output() {
            amp_b.push_input(amp_a.pop_output().unwrap());
        }
        amp_b.run();
        while amp_b.has_output() {
            amp_c.push_input(amp_b.pop_output().unwrap());
        }
        amp_c.run();
        while amp_c.has_output() {
            amp_d.push_input(amp_c.pop_output().unwrap());
        }
        amp_d.run();
        while amp_d.has_output() {
            amp_e.push_input(amp_d.pop_output().unwrap());
        }
        amp_e.run();
        if amp_e.has_output() {
            final_output = amp_e.last_output().unwrap();
        }
        while amp_e.has_output() {
            amp_a.push_input(amp_e.pop_output().unwrap());
        }
    }

    return final_output;
}

fn main() {
    //Read and parse input data
    let data = fs::read_to_string("input-07.txt").expect("Unable to read file");

    let mut program: HashMap<i64, i64> = HashMap::new();

    for (i, num) in data.split(",").enumerate() {
        program.insert(i as i64, num.parse().expect("Malformed input"));
    }

    //Part 1
    let mut max_out: i64 = 0;

    for phases in (0..=4).permutations(5) {
        let a_out = get_signal(&program, phases[0], 0);
        let b_out = get_signal(&program, phases[1], a_out);
        let c_out = get_signal(&program, phases[2], b_out);
        let d_out = get_signal(&program, phases[3], c_out);
        let e_out = get_signal(&program, phases[4], d_out);
        if e_out > max_out {
            max_out = e_out;
        }        
    }

    println!("{max_out}");

    max_out = 0;
    for phases in (5..=9).permutations(5) {
        let result = run_p2(&program, &phases, 0);
        if result > max_out {
            max_out = result;
        }
    }
    println!("{max_out}");
    
}