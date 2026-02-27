pub struct Intcode {
    pub program: Vec<isize>,
    pub running: bool,
    pub pc: isize,
    pub output: Vec<isize>,
    pub input: Vec<isize>
}

impl Intcode {
    fn get_ops(&self, num: isize, modes: isize) -> Vec<isize> {
        let mut ops: Vec<isize> = Vec::new();
        let mut next_mode = modes;

        for offset in 1..=num {
            if next_mode % 10 == 0 {
                ops.push(self.program[self.pc as usize + offset as usize]);
            } else {
                ops.push(self.pc + offset);
            }
            next_mode /= 10;
        }
        return ops;
    }

    pub fn step(&mut self) {
        //println!("PC: {}, state: {:?}", self.pc, self.program);
        if self.pc < 0 || self.pc >= self.program.len() as isize || self.program[self.pc as usize] == 99 {
            self.running = false;
        }
        if !self.running {
            return
        }

        let opcode = self.program[self.pc as usize] % 100;
        let modes = self.program[self.pc as usize] / 100;
        match opcode {
            1 => {
                //Add
                let ops = self.get_ops(3, modes);
                self.program[ops[2] as usize] = self.program[ops[0] as usize] + self.program[ops[1] as usize];
                self.pc += 4;
            }
            2 => {
                //Multiply
                let ops = self.get_ops(3, modes);
                self.program[ops[2] as usize] = self.program[ops[0] as usize] * self.program[ops[1] as usize];
                self.pc += 4;
            }
            3 => {
                //Input
                let ops = self.get_ops(1, modes);
                self.program[ops[0] as usize] = self.input.remove(0);
                self.pc += 2;
            }
            4 => {
                //Output
                let ops = self.get_ops(1, modes);
                self.output.push(self.program[ops[0] as usize]);
                self.pc += 2;
            }
            5 => {
                //jump-if-true
                let ops = self.get_ops(2, modes);
                if self.program[ops[0] as usize] != 0 {
                    self.pc = self.program[ops[1] as usize];
                } else {
                    self.pc += 3;
                }
            }
            6 => {
                //jump-if-false
                let ops = self.get_ops(2, modes);
                if self.program[ops[0] as usize] == 0 {
                    self.pc = self.program[ops[1] as usize];
                } else {
                    self.pc += 3;
                }
            }
            7 => {
                //less than
                let ops = self.get_ops(3, modes);
                self.program[ops[2] as usize] = {
                    if self.program[ops[0] as usize] < self.program[ops[1] as usize] {
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
                    if self.program[ops[0] as usize] == self.program[ops[1] as usize] {
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
        while self.running {
            self.step();
        }
    }
}