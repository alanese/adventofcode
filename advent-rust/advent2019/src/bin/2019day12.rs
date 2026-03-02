use std::fs;
use std::cmp::Ordering;
use std::collections::HashSet;
use regex::Regex;

#[derive(Debug, Copy, Clone)]
struct Moon {
    x: i32,
    y: i32,
    z: i32,
    dx: i32,
    dy: i32,
    dz: i32
}

impl Moon {
    fn get_energy(&self) -> i32 {
        (self.x.abs() + self.y.abs() + self.z.abs()) * (self.dx.abs() + self.dy.abs() + self.dz.abs())
    }

    fn accel_towards(&mut self, other: Moon) {
        match self.x.cmp(&other.x) {
            Ordering::Less => self.dx += 1,
            Ordering::Greater => self.dx -= 1,
            Ordering::Equal => ()
        }
        match self.y.cmp(&other.y) {
            Ordering::Less => self.dy += 1,
            Ordering::Greater => self.dy -= 1,
            Ordering::Equal => ()
        }
        match self.z.cmp(&other.z) {
            Ordering::Less => self.dz += 1,
            Ordering::Greater => self.dz -= 1,
            Ordering::Equal => ()
        }
    }

    fn move_step(&mut self) {
        self.x += self.dx;
        self.y += self.dy;
        self.z += self.dz;
    }
}

const MOON_REGEX: &str = r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>";
fn parse_moon (moon: &str) -> Moon {
    let re = Regex::new(MOON_REGEX).unwrap();

    let captures = re.captures(moon).expect("malformed moon");

    let x: i32 = captures.get(1).unwrap().as_str().parse().unwrap();
    let y: i32 = captures.get(2).unwrap().as_str().parse().unwrap();
    let z: i32 = captures.get(3).unwrap().as_str().parse().unwrap();

    Moon {
        x,
        y,
        z,
        dx: 0,
        dy: 0,
        dz: 0
    }
}

fn split_coords(moons: &Vec<Moon>) -> (Vec<i32>, Vec<i32>, Vec<i32>) {
    let mut x_coords: Vec<i32> = Vec::new();
    let mut y_coords: Vec<i32> = Vec::new();
    let mut z_coords: Vec<i32> = Vec::new();

    for moon in moons {
        x_coords.push(moon.x);
        x_coords.push(moon.dx);
        y_coords.push(moon.y);
        y_coords.push(moon.dy);
        z_coords.push(moon.z);
        z_coords.push(moon.dz);
    }

    (x_coords, y_coords, z_coords)
}

fn update_moons(moons: &mut Vec<Moon>) {
    let moon_count = moons.len();

    for i in 0..moon_count {
        let moon_2: Moon = moons.get(i).unwrap().clone();
        for j in 0..moon_count {
            let moon_1: &mut Moon = moons.get_mut(j).unwrap();
            moon_1.accel_towards(moon_2);
        }
    }

    for i in 0..moon_count {
        moons[i].move_step();
    }
}

fn gcd(mut x: i64, mut y: i64) -> i64 {
    while y != 0 {
        (x,y) = (y, x%y);
    }

    x
}

fn lcm(x: i64, y: i64) -> i64 {
    (x*y) / gcd(x,y)
}

fn main() {
    let data = fs::read_to_string("input-12.txt").expect("Unable to read file");
    
    let mut moons: Vec<Moon> = Vec::new();
    for line in data.lines() {
        moons.push(parse_moon(line));
    }
    
    let mut moons_copy = moons.clone();

    for step in 0..1000 {
        update_moons(&mut moons_copy);
        if step%100 == 0 {
            println!("Step {} : {moons_copy:?}", step+1);
        }
    }
    //println!("{moons_copy:?}");
    let mut total = 0;
    for moon in moons_copy {
        total += moon.get_energy();
    }
    println!("{total}");

    let mut x_recur = -1;
    let mut y_recur = -1;
    let mut z_recur = -1;

    let mut x_set: HashSet<Vec<i32>> = HashSet::new();
    let mut y_set: HashSet<Vec<i32>> = HashSet::new();
    let mut z_set: HashSet<Vec<i32>> = HashSet::new();

    let (x_coords, y_coords, z_coords) = split_coords(&moons);
    x_set.insert(x_coords);
    y_set.insert(y_coords);
    z_set.insert(z_coords);

    let mut step: i64 = 0;
    while x_recur == -1 || y_recur == -1 || z_recur == -1 {
        step += 1;
        update_moons(&mut moons);

        let (x_coords, y_coords, z_coords) = split_coords(&moons);
        if x_recur == -1 {
            if x_set.contains(&x_coords) {
                x_recur = step;
            } else {
                x_set.insert(x_coords);
            }
        }
        
        if y_recur == -1 {
            if y_set.contains(&y_coords) {
                y_recur = step;
            } else {
                y_set.insert(y_coords);
            }
        }

        if z_recur == -1 {
            if z_set.contains(&z_coords) {
                z_recur = step;
            } else {
                z_set.insert(z_coords);
            }
        }
    }
    println!("{x_recur} {y_recur} {z_recur}");
    println!("{}", lcm(lcm(x_recur, y_recur), z_recur) );
}