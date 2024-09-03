#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)

    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")


class ChattyStudent(Student):
    def hello(self):
        # Use super() to inherit the parent class's hello() method
        super().hello()
        # Add additional "chatty" behavior
        print("How are you doing today? I'm okay, but I'm kind of tired.")
        print("Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy!")
        print("What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        # Call super() multiple times to print "Pick me!" ten times
        for _ in range(10):
            super().raise_hand()
