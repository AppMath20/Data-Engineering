# -*- coding: cp1251 -*-

"""
����� ��� ���� "������ ��������".
"""


class Guesser:

    class Node:

        def __init__(self, data: str, type: str):
            self.left = None
            self.right = None
            self.data = data
            self.type = type

    def __init__(self, initialAnimal):
        """
        �����������. �������� ������ ��������, ������� ����� �������.
        """
        self.treeHead = self.treeCur = self.Node(initialAnimal, "animal")
        pass

    def Request(self):
        """
        ����� ��������� �������� ������� �������. ����� ���� ������ ��������� ��� ������ �� ��������� ������.
        ������� ����� ���� ���� �����:
            1. ("question", <������ � ��������, ��� �� ��� ����� � �������>);
            2. ("animal", <������ � ��������, ��� ��� ���� ������� � �������>).
        """
        return (self.treeCur.type, self.treeCur.data)

    def Yes(self):
        """
        �� ������� ������ ������� ����� "��".
        ���� Request() ���������� ������ � "animal", �� ��������� ������.
        """
        if self.treeCur.type == "animal":
            self.treeCur = self.treeHead
        else:
            self.treeCur = self.treeCur.left
        pass

    def No(self):
        """
        �� ������� ������ ������� ����� "���".
        """
        if self.treeCur.type == "question":
            self.treeCur = self.treeCur.right
        pass

    def AddDef(self, question, animal):
        """
        ������ �����������, ���� ������� �� ������� ��������.
        ��������� ������ � ��������. �������� �������� ������� "��" �� ������, � ������� "���" �������� ��������, ���������� Request().
        ��������� ������.
        """
        wrongAns = self.treeCur.data
        self.treeCur.type = "question"
        self.treeCur.data = question
        self.treeCur.left = self.Node(animal, "animal")
        self.treeCur.right = self.Node(wrongAns, "animal")

        if self.treeHead.type == "animal":
            self.treeHead = self.treeCur

        self.treeCur = self.treeHead
        pass


if __name__ == "__main__":
    guesser = Guesser(input("Input initial animal: "))
    while True:
        (type, question) = guesser.Request()
        print(question + "?")
        answer = input("[Y/N]")
        answer = answer.lower()
        if answer == "y" or answer == "yes":
            guesser.Yes()
            if (type == "animal"):
                print("Guessed")
        elif answer == "n" or answer == "no":
            guesser.No()
            if (type == "animal"):
                animal = input("Input new animal: ")
                question = input("Input new definition: ")
                guesser.AddDef(question, animal)
        elif answer == "":
            break
        else:
            print("Incorrect input")
