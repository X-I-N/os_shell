class Process:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        if name == 'init':
            self.parent = None
        else:
            self.parent = processes[count]


instructions = []
processes = []
count = 0


def init():
    print("Process init is running ......")
    pro = Process('init', 0)
    processes.append(pro)
    print("> init", end=' ')


def get_instructions(file_path):
    f = open(file_path, mode='r', encoding='gb2312')
    context = f.read()
    instructions.extend(context.split('\n'))
    f.close()


def execute(instruction):
    type_ins = instruction.split()[0]
    print(type_ins)
    pass


if __name__ == '__main__':
    init()
    get_instructions('D://test.txt')
    num_instructions = len(instructions)
    for i in range(num_instructions):
        execute(instructions[i])
