use std::fs;
use std::collections::HashMap;
use regex::Regex;

#[derive(Debug)]
struct Node {
    id: String,
    left: String,
    right: String
}

impl Node {
    fn from_string(s: String) -> Node {
        let re = Regex::new("([A-Za-z0-9]+) = \\(([A-Za-z0-9]+), ([A-Za-z0-9]+)\\)").unwrap();

        let caps = re.captures(&s).expect("Error - regex not matched");

        Node {
            id: String::from(caps.get(1).unwrap().as_str()),
            left: String::from(caps.get(2).unwrap().as_str()),
            right: String::from(caps.get(3).unwrap().as_str())
        }
    }
}

fn next_position(position: &String,  direction: char, nodes: &HashMap<String, Node>) -> String {
    match direction {
        'L' => nodes.get(position).unwrap().left.clone(),
        'R' => nodes.get(position).unwrap().right.clone(),
        _ => panic!("Invalid direction")
    }
}



fn end_node(pos: &String) -> bool {
    return pos.ends_with('Z');
}

fn main() {
    let data: Vec<String> = fs::read_to_string("input-08.txt").expect("Unable to open file").lines().map(|x| String::from(x)).collect();

    let route = String::from(data.get(0).unwrap());
    let chars: Vec<char> = route.chars().collect();

    let mut nodes: HashMap<String, Node> = HashMap::new();

    let mut p2_nodes: Vec<String> = Vec::new();

    for i in 2..data.len() {
        let node = Node::from_string(data[i].clone());
        let id = node.id.clone();
        nodes.insert(id.clone(), node);
        if id.ends_with('A') {
            p2_nodes.push(id.clone());
        }
    }

    let mut position = String::from("AAA");
    let target = String::from("ZZZ");
    let mut steps: usize = 0;

    while position != target {
        let direction = chars[steps % chars.len()];
        position = next_position(&position, direction, &nodes);
        steps += 1;
    }

    println!("{steps}");

    //Part 2
    steps = 0;

    println!("{p2_nodes:?}");
    while !p2_nodes.iter().all(|p| end_node(p)) {
        p2_nodes = p2_nodes.iter().map(|p| next_position(&p, chars[steps % chars.len()], &nodes)).collect();
        if steps % 100000 == 0 {
            println!("{steps} steps - {p2_nodes:?}");
        }

        steps += 1;
    }

    println!("{steps}");




}