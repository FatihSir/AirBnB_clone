pplication inspired by AirBnB. Start by reading the AirBnB concept page to understand the broader context of the project.

## Project Overview

The initial phase involves developing a command interpreter to manage your AirBnB objects. This foundational step is crucial as it sets the stage for subsequent tasks involving HTML/CSS templating, database storage, API development, and front-end integration.

## Key Objectives

In this project, you will accomplish the following:

1. **Establish a Parent Class**: Create a `BaseModel` class to handle the initialization, serialization, and deserialization of future instances.
2. **Serialization/Deserialization Flow**: Develop a straightforward flow to convert instances to dictionaries, JSON strings, and files, and vice versa.
3. **Class Creation**: Define all classes required for AirBnB (e.g., User, State, City, Place), inheriting from `BaseModel`.
4. **Storage Engine**: Implement the first abstracted storage engine of the project, which will be based on file storage.
5. **Unit Testing**: Create comprehensive unittests to validate all classes and the storage engine.

## Command Interpreter

The command interpreter is akin to a shell but tailored for specific use-cases pertinent to our project. It will enable you to:

- Create new objects (e.g., a new User or Place)
- Retrieve objects from files or databases
- Perform operations on objects (e.g., counting, computing statistics)
- Update object attributes
- Destroy objects

## Resources

To aid your development, refer to the following resources:

- [cmd module](https://docs.python.org/3/library/cmd.html)
- [cmd module in depth](https://docs.python.org/3/library/cmd.html#cmd.Cmd)
- [Packages concept page](https://docs.python.org/3/tutorial/modules.html#packages)
- [uuid module](https://docs.python.org/3/library/uuid.html)
- [datetime module](https://docs.python.org/3/library/datetime.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [args/kwargs](https://realpython.com/python-kwargs-and-args/)
- [Python test cheatsheet](https://www.cheatography.com/ashlyn-black/cheat-sheets/python-unit-testing/)
- [cmd module wiki page](https://en.wikipedia.org/wiki/Cmd_(Python_module))
- [Python unittest](https://realpython.com/python-testing/)

## Learning Objectives

By the end of this project, you should be able to explain:

- How to create a Python package
- How to develop a command interpreter in Python using the cmd module
- The principles of Unit testing and its implementation in large projects
- The processes of serializing and deserializing a class
- How to read and write JSON files
- Managing datetime in Python
- Understanding and using UUIDs
- Utilizing *args and **kwargs
- Handling named arguments in functions

## Project Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- Interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- Files must end with a new line and start with `#!/usr/bin/python3`
- Include a `README.md` file at the root of the project folder
- Code must adhere to `pycodestyle` (version 2.8.*)
- Files must be executable
- Provide documentation for modules, classes, and functions

### Python Unit Tests

- Test files should end with a new line and be stored in a `tests` folder
- Use the `unittest` module
- Test files must be Python files (extension: `.py`)
- Follow the project folder structure for tests
- Run tests with `python3 -m unittest discover tests` or `python3 -m unittest tests/test_models/test_base_model.py`
- Ensure all modules, classes, and functions have documentation

## Tasks 
#### 1. Be pycodestyle compliant!
Write beautiful code that passes the pycodestyle checks.

**Repo** 
- GitHub repository: `AirBnB_clone`

#### 2. Unittests
All your files, classes, functions must be tested with unit tests

```console
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```
*Note that this is just an example, the number of tests you create can be different from the above example.*

**Warning:**

Unit tests must also pass in non-interactive mode:

``` console
guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```

**Repo:**

- GitHub repository: `AirBnB_clone`
- File: `tests/`

### 3. BaseModel

Write a class `BaseModel` that defines all common attributes/methods for other classes:

- `models/base_model.py`
- Public instance attributes:
    - `id`: string - assign with an `uuid` when an instance is created:
        - you can use `uuid.uuid4()` to generate unique `id` but don’t forget to convert to a string
        - the goal is to have unique `id` for each `BaseModel`
    - `created_at`: datetime - assign with the current datetime when an instance is created
    - `updated_at`: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
- `__str__`: should print: `[<class name>]` `(<self.id>)` `<self.__dict__>`
- Public instance methods:
    - `save(self)`: updates the public instance attribute `updated_at` with the current datetime
    - `to_dict(self)`: returns a dictionary containing all keys/values of `__dict__` of the instance:
        - by using `self.__dict__`, only instance attributes set will be returned
        - a key `__class__` must be added to this dictionary with the class name of the object
        - `created_at` and `updated_at` must be converted to string object in ISO format:
            - format: `%Y-%m-%dT%H:%M:%S.%f` (ex: `2017-06-14T22:31:03.285259`)
            - you can use `isoformat()` of `datetime` object
        - This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our `BaseModel`

```console
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - My First Model
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$ 
```
**Repo:**

- GitHub repository: `AirBnB_clone`
- File: `models/base_model.py, models/__init__.py, tests/`
