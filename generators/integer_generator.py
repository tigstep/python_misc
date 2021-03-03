def odds(start, stop):
    for odd in range(start, stop, 2):
        yield odd


g_odd = odds(3, 11)

while True:
    try:
        input("Press Enter to generate the next value...")
        print(next(g_odd))
    except StopIteration as e:
        print("Generator is exhasted : " + str(e))
        break


def read_large_file(file_handler, block_size=100):
    block = []
    for line in file_handler:
        block.append(line)
        if len(block) == block_size:
            yield block
            block = []
    if block:
        yield block


with open("/Users/tigran/IdeaProjects/python_misc/resources/generator_input.txt") as file_handler:
    for block in read_large_file(file_handler):
        input("Press Enter to generate the next block...")
        print(block)
