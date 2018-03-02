
# ScxmlGenerator
Few stack describing the parsing of scxml file into source code.

This project is made in order to be insert in every software.
Python allows people to insert other programming language inside the code.
So it's good way to insert functionality from other projects inside 
the fsm generate. Plus, we generate object in order to provide 
multi threaded application of the fsm thanks to python object structure, with Pyro for example.

## Requirements

PyScxml should be install with :

`pip2 PyScxml`

Cheetah must be install with :

`pip2 cheetah`

Note that pip2 is mandatory to install dependencies. Indeed, the project run with python 2.7.

## How to use ?

So, in the main.py, you will be able to :
    * Specify the path where the generator can reach a scxml file.
    * Specify the output directory where the files will be generate by the project (ended by "/").

#### Set the input's scxml file
Directly in the constructor of the generator.

#### The output path
Directly in the .generateSource(pathOutput) method.

So to throw the building of fsm's source.

`python2 main.py`

warning : you must execute the project with python 2.7

Will create files.

## Test

To execute test, there is a file named launch_test at the root
of the project. To launch tests,

`python2 launch_test.py`

note that :
    There is integration Test
    There is unitaryTest

## How the project works

You can execute the fsm with the following command :

`python2 PATH_OUT_OUTPUT/fsm.py`

## How to setup your actions

There is a setter inside every fsm's object.
Every fsm object are inside a dictionary name statesItems.

For example if you want to change the OnentryAction for  state "test", you must do :

`statesItem["test"].setOnentryAction(fct)`

Where fct is a function pointer.

Now enjoy the Finite State Machine Generate


##############################################################


## Work achieved

We implement :

    Compouned state ( whitout active ancestor )
    Raise / Send action
    Onexit / Onentry : send / raise
    