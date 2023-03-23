To run:

`cd <folder>` to change working directory to the desired folder

Then `python3 <file name>` to run the file. Output printed to terminal

To go from the current directory to another:
`cd ../` to go up a level to the outermost directory
` cd <folder>` to get into the desired folder


## Object Oriented Programming

All Programs have both Data and Behaviour. Consider a simple To Do program that lists tasks which can be toggles to either complete or incomplete.

Data is what the Program knows. In the To Do program, the Data would be the task description and the task status.

Behaviour is what the Program can do. In the To Do program, we can toggle the task status

OOP is the main Programming paradigm. It competes with Procedural Programming and Functional Programming

### Procedural Programming

In PP, data and behaviours are spread out into the same set of step-by-step instructions. When we need to use a behaviour, we can manipulate the data directly, which changes the overall state of the application

In PP, the order in which code is written is very important, and data is directly mutated as the program runs

### Functional Programming

In FP, the data and the behaviour are separate. Therefore, when we toggle a task, the behaviour is abstracted into a pure function, which takes the old data as an input and returns a copy of the new data as an output. The data is never mutated directly.

### OO Programming

In OOP, the data and the behaviours are grouped together into objects. An object is an entity which holds all of the relevant data plus the behaviours that can operate on the data. In our To Do program, each task would be an object that holds the description and status, as well as the behaviour that can toggle the status.

### 4 Pillars

OOP has 4 pillars:
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

#### Encapsulation

To dive a bit deeper, when we talk about Task objects in our To Do program, we would actually create a Task class with the toggle behaviour, and then instantiate various task objects from that class.

Encapsulation is an object's ability to bundle related data and behaviours together. The data scope is limited to only the relevant bits. Because each object is self-contained, external code cannot see the object or modify it.

#### Abstraction

Abstraction is the concept of hiding complex logic from a user. This makes the code easier to use in other places. In our To Do program, we abstract the complex logic necessary to toggle a task's status away from the user - all they see is a toggle button. All we need to do is call the toggle function or toggle method, and not worry about how it works.

#### Inheritance

Inheritance is the ability of one class to inherit all of the functionality of another class. In our To Do program, we could use inheritance to define another type of task, such as a type of task with a deadline for completion

All we need to do is write the code for the deadline field and a method for checking if the task is overdue. This new task inherits all of the parent class' methods and attributes. This also means that if we update the code for the parent Task class, all classes that inherit from that parent will be updated as well.

#### Polymorphism

Polymorphism means 'having multiple forms'. In coding, this means that objects instantiated from classes can have multiple data-types. Consider the To Do program with the Task class and a DeadlineTask class that inherits from the Task class. If we instantiate two objects - one from the Task class and another from the DeadlineTask class - then the Task obkect will have the Task data type and the DeadlineTask object will have both the DeadlineTask data type and the Task data type. This is because the DeadlineTask object inherits all of the methods and attributes of the Task class.


## Errors
<!-- refactor into list -->
BaseException
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError