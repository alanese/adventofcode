use std::fs;
use std::collections::HashMap;


fn get_depth(orbits: &HashMap<String, String>, body: &String) -> u32 {
    let center = orbits.get(body);
    match center {
        Some(a) => 1 + get_depth(orbits, a),
        None => 0
    }
}

fn get_orbital_chain(body: &String, orbits: &HashMap<String, String>) -> Vec<String> {
    let mut chain: Vec<String> = Vec::new();
    let mut curr: &String = body;
    chain.push(curr.clone());
    while orbits.contains_key(curr) {
        curr = &orbits[curr];
        chain.push(curr.clone());
    }

    return chain;
}

fn main() {
    //Read and parse input data
    let data = fs::read_to_string("input-06.txt").expect("Unable to read file");

    let mut orbits: HashMap<String, String> = HashMap::new();

    for line in data.lines() {
        let (center, orbiter) = line.split_once(")").expect("Bad format");
        orbits.insert(String::from(orbiter), String::from(center));
    }

    //Part 1
    let mut total_orbits: u32 = 0;

    for body in orbits.keys() {
        total_orbits += get_depth(&orbits, body);
    }
    println!("{total_orbits}");

    //Part 2
    let you_depth = get_depth(&orbits, &String::from("YOU"));
    let san_depth = get_depth(&orbits, &String::from("SAN"));
    let you_chain = get_orbital_chain(&String::from("YOU"), &orbits);
    let san_chain = get_orbital_chain(&String::from("SAN"), &orbits);

    for body in san_chain {
        if you_chain.contains(&body) {
            let body_depth = get_depth(&orbits, &body);
            println!("{}", you_depth + san_depth - 2*(body_depth) - 2);
            break;
        }
    }

}