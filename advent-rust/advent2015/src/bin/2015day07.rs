use std::fs;
use std::collections::HashMap;

enum GateInput {
    Gate(String),
    Numeric(u16)
}

enum Gate {
    PassThrough(GateInput),
    And(GateInput, GateInput),
    Or(GateInput, GateInput),
    Lshift(GateInput, GateInput),
    Rshift(GateInput, GateInput),
    Not(GateInput)
}

fn evaluate_input(g: &GateInput, gates: &HashMap<String, Gate>, values: &mut HashMap<String, u16>) -> u16 {
    match g {
        GateInput::Gate(x) => evaluate_gate(&x, gates, values),
        GateInput::Numeric(x) => *x
    }
}

fn evaluate_gate(g: &String, gates: &HashMap<String, Gate>, values: &mut HashMap<String, u16>) -> u16 {
    if values.contains_key(g) {
        return *values.get(g).unwrap();
    }

    let result = match gates.get(g).unwrap() {
        Gate::PassThrough(x) => evaluate_input(x, gates, values),
        Gate::And(x, y) => {
            let op1 = evaluate_input(x, gates, values);
            let op2 = evaluate_input(y, gates, values);
            op1 & op2
        }
        Gate::Or(x, y) => {
            let op1 = evaluate_input(x, gates, values);
            let op2 = evaluate_input(y, gates, values);
            op1 | op2
        }
        Gate::Lshift(x, y) => {
            let op1 = evaluate_input(x, gates, values);
            let op2 = evaluate_input(y, gates, values);
            op1.unbounded_shl(op2 as u32)
        }
        Gate::Rshift(x, y) => {
            let op1 = evaluate_input(x, gates, values);
            let op2 = evaluate_input(y, gates, values);
            op1.unbounded_shr(op2 as u32)
        }
        Gate::Not(x) => {
            let op1 = evaluate_input(x, gates, values);
            !op1
        }
    };

    values.insert(g.clone(), result);
    
    result

}

fn parse_input(word: &str) -> GateInput {
    let maybe_num: Result<u16, _> = word.parse();
    match maybe_num {
        Ok(x) => GateInput::Numeric(x),
        Err(_) => GateInput::Gate(String::from(word))
    }
}

fn parse_gate(line: &str) -> (Gate, String) {
    let words: Vec<&str> = line.split_whitespace().collect();
    let gate_id = String::from(*words.last().unwrap());
    if words.len() == 3 {
        let input = parse_input(words[0]);
        
        (Gate::PassThrough(input), gate_id)
    } else if words.len() == 4 {
        let input = parse_input(words[1]);
        
        (Gate::Not(input), gate_id)
    } else {
        let input1 = parse_input(words[0]);
        let input2 = parse_input(words[2]);
        match words[1] {
            "AND" => (Gate::And(input1, input2), gate_id),
            "OR" => (Gate::Or(input1, input2), gate_id),
            "LSHIFT" => (Gate::Lshift(input1, input2), gate_id),
            "RSHIFT" => (Gate::Rshift(input1, input2), gate_id),
            _ => panic!()
        }
    }

}

fn main() {
    let data = fs::read_to_string("input-07.txt").expect("Unable to read file");

    let mut gates: HashMap<String, Gate> = HashMap::new();

    for line in data.lines() {
        let (gate, id ) = parse_gate(line);
        gates.insert(id, gate);
    }

    let mut values: HashMap<String, u16> = HashMap::new();

    let target = String::from("a");
    let mut result = evaluate_gate(&target, &gates, &mut values);
    println!("{result}");

    values.clear();
    values.insert(String::from("b"), result);
    result = evaluate_gate(&target, &gates, &mut values);
    println!("{result}");

}