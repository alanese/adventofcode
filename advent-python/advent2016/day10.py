from typing import NamedTuple

class Bot(NamedTuple):
    id: int
    high_dest: int
    low_dest: int
    storage: list[int]

#Value (index 0) goes to bot (index 1)
value_lines: list[tuple[int, int]] = []
#Bot (index 0) gives low to (index 1) and high to (index 2)
# negative low/high refers to output -(x+1)
bot_lines: list[tuple[int, int, int]] = []
with open("input-10.txt") as f:
    max_bot: int = -1
    max_output: int = -1
    for line in f:
        line_split:list[str] = line.strip().split()
        if line_split[0] == "value":
            value_lines.append((int(line_split[1]), int(line_split[5])))
        else:
            bot_num: int = int(line_split[1])
            if bot_num > max_bot:
                max_bot = bot_num
            low: int = int(line_split[6])
            high: int = int(line_split[11])
            if line_split[5] == "output":
                if low > max_output:
                    max_output = low
                low = -(low+1)
            if line_split[10] == "output":
                if high > max_output:
                    max_output = high
                high = -(high+1)
            bot_lines.append((bot_num, low, high))

DUMMY_BOT = Bot(-1, 0, 0, [])
bots: list[Bot] = [DUMMY_BOT] * (max_bot+1)
output: list[int] = [-1] * (max_output+1)

active_bots: list[Bot] = []
new_bot: Bot
for bot_id, low_dest, high_dest in bot_lines:
    new_bot = Bot(bot_id, high_dest, low_dest, [])
    bots[bot_id] = new_bot
    active_bots.append(new_bot)

for value, bot_target in value_lines:
    bots[bot_target].storage.append(value)

finished_bots: list[Bot] = []
seen_states: set[tuple[int, int]] = set()
while len(active_bots) > 0:
    current_bot: Bot = active_bots.pop(0)
    current_state = (current_bot.id, len(active_bots))
    if current_state in seen_states:
        print("Stasis reached")
        break
    seen_states.add(current_state)
    if len(current_bot.storage) == 2:
        cur_bot_high: int = current_bot.storage[1]
        cur_bot_low: int = current_bot.storage[0]
        if cur_bot_high < cur_bot_low:
            cur_bot_high, cur_bot_low = cur_bot_low, cur_bot_high
        if current_bot.low_dest >= 0:
            bots[current_bot.low_dest].storage.append(cur_bot_low)
        else:
            output[-1 * (current_bot.low_dest + 1)] = cur_bot_low
        
        if current_bot.high_dest >= 0:
            bots[current_bot.high_dest].storage.append(cur_bot_high)
        else:
            output[-1 * (current_bot.high_dest + 1)] = cur_bot_high
        finished_bots.append(current_bot)

        if (cur_bot_low, cur_bot_high) == (17,61):
            print(current_bot)
    else:
        active_bots.append(current_bot)

print(output[0] * output[1] * output[2])