# POPO
Define everything using POPOs (Plain Old Python Object), then you can easily use it from SQLAlchemy ORM, Protobuf3, and so on.

## Wanted Goals
- Python 3
- $ popo input.py
	- -> input.sqla.py
	- -> input.proto
- POPO input files just work as normal python file
- Pipeline:
	- Read Input
	- Convert to Own DataTypes
	- Target Factories
	- Outputs

## Wanted Types
- [Python Default Types](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)
	- Numeric thingy: Integer, Float, Double, ...
	- String
	- List
	- Bytes
- [DateTime](https://docs.python.org/3.5/library/datetime.html#datetime.datetime.now)
- Enum
- ...

## Wanted Targets
- [SQLAlchemy ORM](http://www.sqlalchemy.org/)
- [Protobuf](https://developers.google.com/protocol-buffers/docs/proto3#scalar)
- ...

## Wanted Features
- Versioning
	- SQLAlchemy will cover this by alembic
	- Protobuf need to consider this
		- read olders and managing the 
- Targets Factory and Configurable Targets? (custom type converter?)
	- want to export with
		- [sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
		- [protobuf3](https://github.com/Pr0Ger/protobuf3)
- Prefix/Postfix naming
- ...

## Resolved Question
- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)?
	- Nope, it's not for class defining.
- [How to get parse tree of python?](http://python3porting.com/fixers.html)
	- ast: "designed to generate an abstract syntax tree and ignores all comments and formatting"
	- parser: "internal code parser, which is optimized to generate byte code and too low level"
	- lib2to3: "high level and contains all formatting, but that doesn’t mean it’s easy to use"
		- Why don't you just make 2to3 fixer for converting those?
			- I don't think 2to3 is not for it.
		- how to get the parse tree form lib2to3?
			- lib2to3.pgen2, but it's for python2 (maybe)
				- oops, our target is python3
	- yo yo yo yo yo!!! We don't need to parse! We just used class.
		- So Class.__dict__() and instanceof() will cover all.
			- really? dive it now!
				- import `popo-input`
					- I want cli, but how to import `/path/popo-input.py`?
						- just use `popo-input` and see you next time.
						- I found `modulefinder`, is it related?
				- dir(`popo-input`)
					- ignore `__.*__`
				- .\_\_dict\_\_
					- ignore `__.*__`
				- .

## Unresolved Questions
- Is really needed? helpful?
- How to ...
	- save datetime @ protobuf?
		- maybe timestamp and timezone.
	- manage the build?
	- name exported output?
	- limit the type of contents?
	- limit the size of string with this?
		- using comment? (noooooooooo..)
		- using 
	- manage the metadata of input/output source code?
		- why need it?
			- ...
- Where is the gap for adding versioning process.
- No Private / Forgien Key?!
- Nested Class!
- Alphabetical Order Class Contents?!!!
- How to save the order of input, and keep it as output?!!!!!!!!!! <- currently biggest mission blocker (lib2to3 needed?)

## TODO
- .gitignore

## Milestone
1. Set the clear blueprint for v0.0.0 (due: 151115)
	- minimum wanted-types: 
		- integer
		- string
		- ?
	- 2 targets
		- sqlalchemy
		- protobuf
	- 1 feature
		- target factory
	- Goal: directory design
	- Goal: pipeline design
2. ...