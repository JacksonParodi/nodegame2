import json


class Node:

    def __init__(self, id: int, text: str, answers=[]) -> None:
        self.id = id
        self.text = text
        self.answers = answers


all_nodes = []

all_nodes.append(Node(id=10, text='what is your name?'))
all_nodes.append(Node(id=11, text='you walk into a coffee shop. what do you order?', answers=[
                 'coffee', 'tea', 'latte', 'water']))
all_nodes.append(Node(id=12, text='as you enjoy your beverage, a quiet person walks up to you. how do you response?', answers=[
                 'say hello', 'say howdy', 'say nothing', 'violence']))
all_nodes.append(Node(id=13, text='the stranger smiles and walks away. you feel warm, what do next?', answers=[
    'leave the coffee shop', 'contemplate']))
all_nodes.append(Node(id=14, text='the stranger dissolves into a strange mist. you feel cold, what do next?', answers=[
    'leave the coffee shop', 'contemplate']))
all_nodes.append(Node(
    id=15, text='you did what you did and you cannot undo it. dont sweat it, everyone makes mistakes'))
all_nodes.append(Node(id=16, text='you step onto the street. to your left is a graveyard, to your right is a bus stop. where to?', answers=[
                 'graveyard', 'bus stop']))
all_nodes.append(Node(id=17, text='the graveyard air is still and silent. would you like to speak with a skeleton?', answers=[
    'yes', 'no']))
all_nodes.append(Node(
    id=18, text='the skeleton just stares at you. it isnt mad, it is simply disappointed'))
all_nodes.append(Node(
    id=19, text='you are at the bus stop and unsure of what happens next. want to cry?', answers=['sure', 'not sure']))
all_nodes.append(Node(
    id=20, text='you shed a small tear just as the bus arrives. would you like to board the bus?', answers=['yes', 'no']))
all_nodes.append(
    Node(id=21, text='you just sit there, and sit there, and sit there'))
all_nodes.append(Node(id=22, text='the bus drives off, possibly forever'))
all_nodes.append(Node(id=23, text='\nthat is it, there is now more. say r for new game+, or x to close\n'))

with open("nodes.json", "r") as file:
    json_nodes = json.load(file)
    for raw_node in json_nodes:
        all_nodes.append(Node(raw_node["text"], raw_node["answers"]))


def clear_nodes_json() -> None:
    with open("nodes.json", "w") as file:
        json.dump([], file)
        return


def add_node() -> None:
    new_node = {"text": "",
                "answers": []}
    new_node["text"] = input("Enter the text: ")
    for new_answer in range(0, int(input("Enter the number of answers: "))):
        new_node["answers"].append(input("Enter the answer: "))

    with open("nodes.json", "r") as file:
        data = json.load(file)
        data.append(new_node)
        with open("nodes.json", "w") as file:
            json.dump(data, file, indent=4, sort_keys=True,)
            return


def node_tools() -> None:
    while True:
        print('hello jackson, please select\n')
        print("1. Add node")
        print("2. Clear nodes.json")
        print("3. Exit")

        answer = input("> > > ")
        if answer == "1":
            add_node()
        elif answer == "2":
            clear_nodes_json()
        elif answer == "3":
            return
        else:
            print("Invalid input")


if __name__ == "__main__":
    node_tools()
