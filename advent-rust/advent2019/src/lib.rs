#[derive(PartialEq, Debug)]
pub enum Status {
    RUNNING,
    BLOCKED,
    HALTED
}

pub struct Intcode {
    pub program: Vec<isize>,
    pub status: Status,
    pub pc: isize,
    pub output: Vec<isize>,
    pub input: Vec<isize>
}

impl Intcode {

    //Create an Intcode object with the specified program
    pub fn create(program: Vec<isize>) -> Intcode {
        return Intcode{
            program: program,
            status: Status::RUNNING,
            pc: 0,
            output: Vec::new(),
            input: Vec::new()
        };
    }

    fn get_ops(&self, num: usize, modes: isize) -> Vec<usize> {
        let mut ops: Vec<usize> = Vec::new();
        let mut next_mode = modes;

        for offset in 1..=num {
            if next_mode % 10 == 0 {
                ops.push(self.program[self.pc as usize + offset as usize] as usize);
            } else {
                ops.push(self.pc as usize + offset);
            }
            next_mode /= 10;
        }
        return ops;
    }

    pub fn step(&mut self) {
        if self.pc < 0 || self.pc >= self.program.len() as isize || self.program[self.pc as usize] == 99 {
            self.status = Status::HALTED;
        }
        if self.status == Status::HALTED {
            return;
        }

        let opcode = self.program[self.pc as usize] % 100;
        let modes = self.program[self.pc as usize] / 100;
        match opcode {
            1 => {
                //Add
                let ops = self.get_ops(3, modes);
                self.program[ops[2]] = self.program[ops[0]] + self.program[ops[1]];
                self.pc += 4;
            }
            2 => {
                //Multiply
                let ops = self.get_ops(3, modes);
                self.program[ops[2]] = self.program[ops[0]] * self.program[ops[1]];
                self.pc += 4;
            }
            3 => {
                //Input
                if self.input.len() == 0 {
                    self.status = Status::BLOCKED;
                    return;
                }
                let ops = self.get_ops(1, modes);
                self.program[ops[0]] = self.input.remove(0);
                self.pc += 2;
            }
            4 => {
                //Output
                let ops = self.get_ops(1, modes);
                self.output.push(self.program[ops[0]]);
                self.pc += 2;
            }
            5 => {
                //jump-if-true
                let ops = self.get_ops(2, modes);
                if self.program[ops[0]] != 0 {
                    self.pc = self.program[ops[1]];
                } else {
                    self.pc += 3;
                }
            }
            6 => {
                //jump-if-false
                let ops = self.get_ops(2, modes);
                if self.program[ops[0]] == 0 {
                    self.pc = self.program[ops[1]];
                } else {
                    self.pc += 3;
                }
            }
            7 => {
                //less than
                let ops = self.get_ops(3, modes);
                self.program[ops[2]] = {
                    if self.program[ops[0]] < self.program[ops[1]] {
                        1
                    } else {
                        0
                    }
                };
                self.pc += 4;
            }
            8 => {
                //equals
                let ops = self.get_ops(3, modes);
                self.program[ops[2] as usize] = {
                    if self.program[ops[0]] == self.program[ops[1]] {
                        1
                    } else {
                        0
                    }
                };
                self.pc += 4;
            }
            _ => {
                panic!("Invalid opcode");
            }
        }
    }

    pub fn run(&mut self) {
        if self.status == Status::BLOCKED {
            self.status = Status::RUNNING;
        }
        while self.status == Status::RUNNING {
            self.step();
        }
    }
}