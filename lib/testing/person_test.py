#!/usr/bin/env python3

#!/usr/bin/env python3

from person import Person
import io
import sys
import types

class TestPerson:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person"'''
        guido = Person("Guido")  # Provide a name here
        assert(type(guido) == Person)

class TestTalk:
    '''Person.talk() in person.py'''

    def test_is_method(self):
        '''is an instance method'''
        guido = Person("Guido")  # Provide a name here
        assert(type(guido.talk) == types.MethodType)

    def test_prints_hello_world(self):
        '''prints "Hello World!"'''
        guido = Person("Guido")  # Provide a name here
        captured_out = io.StringIO()
        sys.stdout = captured_out
        guido.talk()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello World!\n")

class TestWalk:
    '''Person.walk() in person.py'''

    def test_is_method(self):
        '''is an instance method'''
        guido = Person("Guido")  # Provide a name here
        assert(type(guido.walk) == types.MethodType)

    def test_prints_the_person_is_walking(self):
        '''prints "The person is walking."'''
        guido = Person("Guido")  # Provide a name here
        captured_out = io.StringIO()
        sys.stdout = captured_out
        guido.walk()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "The person is walking.\n")