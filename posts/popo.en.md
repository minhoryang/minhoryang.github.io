<!-- 
.. title: POPO
.. slug: popo
.. date: 2015-11-08 23:38:00 UTC+09:00
.. tags:  
.. category: DesignDoc
.. link: 
.. description: 
.. type: text
-->

# [POPO](https://github.com/minhoryang/popo)

Define everything using POPOs (Plain Old Python Object), then you can easily use it from SQLAlchemy ORM, Protobuf3, and so on.

## Wanted Types
- Numeric thingy
- String
- List
	- Huh? How to define the contents of list?
		- Let's Use [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
			- Isn't it Plain-New-Python-Object? ...
- [DateTime](https://docs.python.org/3.5/library/datetime.html#datetime.datetime.now)
- Bytes

## Wanted Exports
- [SQLAlchemy ORM](http://www.sqlalchemy.org/)
- [Protobuf](https://developers.google.com/protocol-buffers/docs/proto3#scalar)

## Wanted Features
- Versioning
	- SQLAlchemy will cover this by alembic
	- Protobuf need to consider this
		- read olders and managing the 
- Exports Factory and Configurable Exports?
	- want to export with
		- [sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
		- [protobuf3](https://github.com/Pr0Ger/protobuf3)
