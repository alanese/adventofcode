use std::fs;

fn fuel_req(mass: i32) -> i32 {
    (mass/3) - 2
}

fn fuel_req_p2(mass: i32) -> i32 {
    let mut curr_mass = mass;
    let mut fuel = 0;

    curr_mass = fuel_req(curr_mass);
    while curr_mass > 0 {
        fuel += curr_mass;
        curr_mass = fuel_req(curr_mass);
    }

    fuel
}
fn main() {
    let data = fs::read_to_string("input-01.txt")
        .expect("Unable to open file");

    let mut total_fuel: i32 = 0;
    let mut total_fuel_p2: i32 = 0;
    for line in data.lines() {
        let mass: i32 = line.parse().expect("Bad line");
        total_fuel += fuel_req(mass);
        total_fuel_p2 += fuel_req_p2(mass);
    }

    println!("{total_fuel}");
    println!("{total_fuel_p2}");

}