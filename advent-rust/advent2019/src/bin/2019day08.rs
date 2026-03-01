use std::fs;

//This probably already exists somewhere in std
fn count<T:PartialEq>(seq: &[T], target: T) -> u32 {
    let mut count: u32 = 0;
    for elt in seq {
        if *elt == target {
            count += 1;
        }
    }
    count
}

fn main() {
    // Set up a few useful constants
    const ZERO: u8 = '0' as u8;
    const ONE: u8 = '1' as u8;
    const TWO: u8 = '2' as u8;
    const LAYER_WIDTH: usize = 25;
    const LAYER_HEIGHT: usize = 6;
    const LAYER_AREA: usize = LAYER_WIDTH * LAYER_HEIGHT;

    //Read data from file
    let data = fs::read_to_string("input-08.txt").expect("Unable to read file");
    let bytes = data.as_bytes();

    //Part 1
    let mut fewest_zeroes: u32 = u32::MAX;
    let mut fewest_zero_layer = &[1][..];

    let mut layer_index = 0;
    while layer_index * LAYER_AREA < bytes.len() {
        let next_row = &bytes[LAYER_AREA*layer_index..LAYER_AREA*(layer_index+1)];
        let zero_count = count(next_row, ZERO);
        if zero_count < fewest_zeroes {
            fewest_zeroes = zero_count;
            fewest_zero_layer = next_row;
        }
        layer_index +=1 ;
    }

    let one_count = count(fewest_zero_layer, ONE);
    let two_count = count(fewest_zero_layer, TWO);
    println!("{}", one_count*two_count);

    //Part 2
    let mut index = 0;
    while index < LAYER_AREA {
        let mut color = -1;
        let mut layer = 0;
        while layer * LAYER_AREA < bytes.len() {
            match bytes[index + layer * LAYER_AREA] {
                ZERO => {
                    color = 0;
                    break;
                }
                ONE => {
                    color = 1;
                    break;
                }
                _ => layer += 1
            }
        }
        match color {
            1 => print!("#"),
            _ => print!(" ")
        }
        index += 1;
        if index % LAYER_WIDTH == 0 {
            println!("");
        }
    }

}