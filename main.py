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
processes_1 = []
processes_2 = []
count_1 = 0
count_2 = 0
blocked_list = []
running = None


def init():
    print("Process init is running ......")
    pro = Process('init', 0)
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
        schedule()
    elif type_ins == 'to':
        time_out()


def create_process(name, priority):
    pro = Process(name, priority)
    running.child.append(pro)
    if priority == 1:
        processes_1.append(pro)
    elif priority == 2:
        processes_2.append(pro)


def schedule():
    global running
    run_priority = running.priority
    if len(processes_2) != 0 and run_priority < 2:
        running.status = 'ready'
        processes_2[count_2].status = 'running'
        running = processes_2[count_2]
    elif len(processes_1) != 0 and run_priority < 1:
        running.status = 'ready'
        processes_1[count_1].status = 'running'
        running = processes_1[count_1]
    print(running.name, end=' ')


def time_out():
    global count_1, count_2, running

    if running.priority == 1:
        count_1 += 1
        count_1 %= len(processes_1)
        if len(processes_2) > 0:
            running.status = 'ready'
            processes_2[count_2].status = 'running'
            running = processes_2[count_2]
        else:
            running.status = 'ready'
            processes_2[count_2].status = 'running'
            running = processes_2[count_2]
    elif running.priority == 2:
        count_2 += 1
        count_2 %= len(processes_2)
        running.status = 'ready'
        processes_2[count_2].status = 'running'
        running = processes_2[count_2]

    print(running.name, end=' ')


if __name__ == '__main__':
    init()
    get_instructions('D://test.txt')
    num_instructions = len(instructions)
    for i in range(num_instructions):
        execute(instructions[i])
