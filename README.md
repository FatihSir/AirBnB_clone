# 0x00. AirBnB clone - The console
![AirBnB](1.jpeg)

Welcome to the AirBnB clone project! This initiative marks the beginning of your journey towards building a comprehensive web application inspired by AirBnB. Start by reading the AirBnB concept page to understand the broader context of the project.

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

#### 4. Create BaseModel from dictionary

Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation.
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```
Update `models/base_model.py:`

- `__init__(self, *args, **kwargs):`
    - you will use `*args, **kwargs` arguments for the constructor of a `BaseModel`. (more - information inside the **AirBnB clone**` concept page)
    - `*args` won’t be used
    - if `kwargs` is not empty:
        - each key of this dictionary is an attribute name (Note `__class__` from `kwargs` is the only one that should not be added as an attribute. See the example output, below)
        - each value of this dictionary is the value of this attribute name
        - **Warning**: `created_at` and `updated_at` are strings in this dictionary, but inside your `BaseModel` instance is working with `datetime` object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
    - otherwise:
        - create `id` and `created_at` as you did previously (new instance)
```console
guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
JSON of my_model:
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    __class__: (<class 'str'>) - BaseModel
    my_number: (<class 'int'>) - 89
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    name: (<class 'str'>) - My_First_Model
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
False
guillaume@ubuntu:~/AirBnB$
```
**Repo:**

- GitHub repository: `AirBnB_clone`
- File: `models/base_model.py, tests/`

#### 5. Store first object

Now we can recreate a `BaseModel` from another one by using a dictionary representation:

```console 
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```
It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.

Writing the dictionary representation to a file won’t be relevant:

- Python doesn’t know how to convert a string to a dictionary (easily)
- It’s not human readable
- Using this file with another program in Python or other language will be hard.

So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:

```console
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```

Magic right?

Terms:

- **simple Python data structure**: Dictionaries, arrays, number and string. ex: `{ '12': { 'numbers': [1, 2, 3], 'name': "John" } }`
- **JSON string representation**: String representing a simple data structure in JSON format. ex: `'{ "12": { "numbers": [1, 2, 3], "name": "John" } }'`

Write a class `FileStorage` that serializes instances to a JSON file and deserializes JSON file to instances:

- `models/engine/file_storage.py`
- Private class attributes:
    - `__file_path`: string - path to the JSON file (ex: `file.json`)
    - `__objects`: dictionary - empty but will store all objects by `<class name>.id` (ex: to store a `BaseModel` object with `id=12121212`, the key will be `BaseModel.12121212`)
- Public instance methods:
    - `all(self)`: returns the dictionary `__objects`
    - `new(self, obj)`: sets in `__objects` the `obj` with key `<obj class name>.id`
    - `save(self)`: serializes `__objects` to the JSON file (path: `__file_path`)
    - `reload(self)`: deserializes the JSON file to `__objects` (only if the JSON file (`__file_path`) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

Update `models/__init__.py`: to create a unique `FileStorage` instance for your application

- import `file_storage.py`
- create the variable `storage`, an instance of `FileStorage`
- call` reload()` method on this variable

Update `models/base_model.py`: to link your `BaseModel` to `FileStorage` by using the variable `storage`

- import the variable `storage`
- in the method `save(self)`:
    - call `save(self)` method of `storage`
- `__init__(self, *args, **kwargs)`:
    - if it’s a new instance (not from a dictionary representation), add a call to the method `new(self)` on `storage`
```console
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
guillaume@ubuntu:~/AirBnB$ 
```
**Repo:**

- GitHub repository: `AirBnB_clone`
- File: `models/engine/file_storage.py, models/engine/__init__.py, models/__init__.py, models/base_model.py, tests/`
