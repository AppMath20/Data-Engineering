# -*- coding: cp1251 -*-

"""
Класс для игры "угадай животное".
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
        Конструктор. Принимет первое животное, которое знает система.
        """
        self.treeHead = self.treeCur = self.Node(initialAnimal, "animal")
        pass

    def Request(self):
        """
        Метод получения текущего вопроса системы. Может быть вызван несколько раз подряд до получения ответа.
        Кортежи могут быть двух видов:
            1. ("question", <строка с вопросом, как он был введён в систему>);
            2. ("animal", <строка с животным, как оно было введено в систему>).
        """
        return (self.treeCur.type, self.treeCur.data)

    def Yes(self):
        """
        На текущий вопрос системы ответ "Да".
        Если Request() возвращает кортеж с "animal", то обновляет сессию.
        """
        if self.treeCur.type == "animal":
            self.treeCur = self.treeHead
        else:
            self.treeCur = self.treeCur.left
        pass

    def No(self):
        """
        На текущий вопрос системы ответ "Нет".
        """
        if self.treeCur.type == "question":
            self.treeCur = self.treeCur.right
        pass

    def AddDef(self, question, animal):
        """
        Ввести определение, если система не угадала животное.
        Принимает вопрос и животное. Животное является ответом "Да" на вопрос, а ответом "Нет" является животное, получаемое Request().
        Обновляет сессию.
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
