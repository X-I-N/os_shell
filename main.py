class Process:
    def __init__(self, name, priority, status='ready'):
        self.name = name
        self.priority = priority
        if name == 'init':
            self.parent = None
        else:
            self.parent = running
        self.status = status
        self.child = []


instructions = []
process_0 = None
processes_1 = []
processes_2 = []
count_1 = 0
count_2 = 0
blocked_list = []
running = None


def init():
    global process_0
    print("Process init is running ......")
    pro = Process('init', 0)
    process_0 = pro
    pro.status = 'running'
    global running
    running = pro
    print("> init", end=' ')


def get_instructions(file_path):
    f = open(file_path, mode='r', encoding='gb2312')
    context = f.read()
    instructions.extend(context.split('\n'))
    f.close()


def execute(instruction):
    type_ins = instruction.split()[0]
    if type_ins == 'cr':
        name = instruction.split()[1]
        priority = instruction.split()[2]
        create_process(name, int(priority))
    elif type_ins == 'to':
        time_out()
    elif type_ins == 'de':
        name = instruction.split()[1]
        pro = get_process(name)
        destroy_process(pro)


def create_process(name, priority):
    pro = Process(name, priority)
    running.child.append(pro)

    if priority == 1:
        processes_1.append(pro)
    elif priority == 2:
        processes_2.append(pro)

    run_next_process()
    print(running.name, end=' ')


def run_next_process():
    global count_1, count_2, running

    if len(processes_1) == 0 and len(processes_2) == 0:
        running = process_0
    elif len(processes_2) > 0:
        running.status = 'ready'
        processes_2[count_2].status = 'running'
        running = processes_2[count_2]
    else:
        running.status = 'ready'
        processes_1[count_1].status = 'running'
        running = processes_1[count_1]


def time_out():
    global count_1, count_2

    if running.priority == 1:
        count_1 += 1
        count_1 %= len(processes_1)
    elif running.priority == 2:
        count_2 += 1
        count_2 %= len(processes_2)

    run_next_process()
    print(running.name, end=' ')


def get_process(name):
    for i in range(len(processes_1)):
        if name == processes_1[i].name:
            return processes_1[i]
    for j in range(len(processes_2)):
        if name == processes_2[j].name:
            return processes_2[j]


def remove_process(pro):
    global count_1, count_2
    if pro.priority == 1:
        global count_1
        processes_1.remove(pro)
        if len(processes_1) is not 0:
            count_1 %= len(processes_1)
    if pro.priority == 2:
        global count_2
        processes_2.remove(pro)
        if len(processes_2) is not 0:
            count_2 %= len(processes_2)
    if pro == running:
        run_next_process()


def destroy_process(pro, is_print=True):
    if len(pro.child) is not 0:
        for ii in range(len(pro.child)):
            destroy_process(pro.child[ii], is_print=False)
        pro.child.clear()

    remove_process(pro)

    if is_print:
        print(running.name, end=' ')


if __name__ == '__main__':
    init()
    get_instructions('D://test.txt')
    num_instructions = len(instructions)
    for i in range(num_instructions):
        execute(instructions[i])
