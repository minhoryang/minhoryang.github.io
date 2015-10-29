<!-- 
.. title: API
.. slug: api
.. date: 2015-10-30 08:00:00 UTC+09:00
.. tags:  
.. category: DesignDoc
.. link: 
.. description: 
.. type: text
-->

- Kubernetes (Docker Container, Label(Version Tagging))
- Load Balancing
- DNS-Based Connecting
- Git-Branch-Based Versioning
- (External Configuration Injecting)
- (Single-Source Based?)
	- Divide the roles by launch commands?
- (Multiple DC Supported?)
	- Latest Checker Needed
		- First, check latest
		- Second, if latest, use it and notify. If not, delegate or sync that info. 
	- Data Exchanger Needed
- (Local Testing?)



## API Routers (Endpoints)
- HTTPS
- Isolated Repository
- Versioning (which api specs included)

## API Service Specs
- HTTP
- Versioning
- Multiple Features encapsuled

## API Workers (Logics)
- GRPC
- Versioning (which algorithms used)

## Datastores
- GRPC
- Services:
	- DB: SQLAlchemy
	- MQ(Message Queue): RabbitMQ
	- File / Object Storage: S3
- Versioning
- Syncable Data Exchanger

## NAT
- Git Repository
- Kubernetes
- Consul DNS (?)
- Bastion Hosts
- VPN

# WORK IN PROGRESS...
