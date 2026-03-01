use std::collections::HashMap;

#[derive(PartialEq, Debug)]
pub enum Status {
    RUNNING,
    BLOCKED,
    HALTED
}

pub struct Intcode {
    pub program: HashMap<i64, i64>,
    pub status: Status,
    pub pc: i64,
    pub output: Vec<i64>,
    pub input: Vec<i64>,
    pub relative_base: i64
}

impl Intcode {

    //Create an Intcode object with the specified program
    pub fn create(program: HashMap<i64, i64>) -> Intcode {
        return Intcode{
            program: program,
            status: Status::RUNNING,
            pc: 0,
            output: Vec::new(),
            input: Vec::new(),
            relative_base: 0
        };
    }

    fn get_ops(&self, num: u8, modes: i64) -> Vec<i64> {
        let mut ops: Vec<i64> = Vec::new();
        let mut next_mode = modes;

        for offset in 1..=num {
            match next_mode % 10 {
                0 => ops.push(*self.program.get(&(self.pc + offset as i64)).unwrap()),
                1 => ops.push(self.pc + offset as i64),
                2 => ops.push(*self.program.get(&(self.pc + offset as i64)).unwrap() + self.relative_base),
                _ => panic!("Invalid opcode")
            }
            next_mode /= 10;
        }
        return ops;
    }

    fn get_mem(&mut self, addr: i64) -> i64 {
        if !self.program.contains_key(&addr) {
            self.program.insert(addr, 0);
        }
        self.program[&addr]
    }

    pub fn step(&mut self) {
        if self.status == Status::HALTED {
            return;
        }

        let opcode = self.program[&self.pc] % 100;
        let modes = self.program[&self.pc] / 100;
        match opcode {
            1 => {
                //Add
                let ops = self.get_ops(3, modes);
                let op0 = self.get_mem(ops[0]);
                let op1 = self.get_mem(ops[1]);
                self.program.insert(ops[2], op0 + op1);
                self.pc += 4;
            }
            2 => {
                //Multiply
                let ops = self.get_ops(3, modes);
                let op0 = self.get_mem(ops[0]);
                let op1 = self.get_mem(ops[1]);
                self.program.insert(ops[2], op0 * op1);
                self.pc += 4;
            }
            3 => {
                //Input
                if self.input.len() == 0 {
                    self.status = Status::BLOCKED;
                    return;
                }
                let ops = self.get_ops(1, modes);
                self.program.insert(ops[0], self.input.remove(0));
                self.pc += 2;
            }
            4 => {
                //Output
                let ops = self.get_ops(1, modes);
                let op0 = self.get_mem(ops[0]);
                self.output.push(op0);
                self.pc += 2;
            }
            5 => {
                //jump-if-true
                let ops = self.get_ops(2, modes);
                let op0 = self.get_mem(ops[0]);
                let op1 = self.get_mem(ops[1]);
                if op0 != 0 {
                    self.pc = op1;
                } else {
                    self.pc += 3;
                }
            }
            6 => {
                //jump-if-false
                let ops = self.get_ops(2, modes);
                let op0 = self.get_mem(ops[0]);
                let op1 = self.get_mem(ops[1]);
                if op0 == 0 {
                    self.pc = op1;
                } else {
                    self.pc += 3;
                }
            }
            7 => {
                //less than
                let ops = self.get_ops(3, modes);
                let op0 = self.get_mem(ops[0]);
                let op1 = self.get_mem(ops[1]);
                self.program.insert(ops[2], if op0 < op1 {1} else {0});
                self.pc += 4;
            }
            8 => {
                //equals
                let ops = self.get_ops(3, modes);
                let op0 = self.get_mem(ops[0]);
                let op1 = self.get_mem(ops[1]);
                self.program.insert(ops[2], if op0 == op1 {1} else {0});
                self.pc += 4;
            }
            9 => {
                //Relative base offset
                let ops = self.get_ops(1, modes);
                let op0 = self.get_mem(ops[0]);
                self.relative_base += op0;
                self.pc += 2;
            }
            99 => {
                self.status = Status::HALTED;
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