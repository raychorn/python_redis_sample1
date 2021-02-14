# Python Redis Sample 1

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [RQ](#RQ)
- [GO](#GO)
- [GO-RMQ](#GO-RMQ)
- [go-redis-queue](#go-redis-queue)
- [go-bee-queue](#go-bee-queue)
- [Prerequisites](#Prerequisites)

## About <a name = "about"></a>

Redis Queuing Prototype

## Getting Started <a name = "getting_started"></a>

Simulate a Queue using Redis as the database.

### Prerequisites <a name = "Prerequisites"></a>

Dockerfile.

```
apt update -y
apt upgrade -y
apt install redis-server -y
```
#### /etc/redis/redis.conf

```
maxmemory 256mb
maxmemory-policy allkeys-lru
```

```
redis-cli info
redis-cli info stats
redis-cli info server
```

### RQ [Redis Queue](https://python-rq.org/) is a simple Python library for queueing jobs and processing them in the background with workers. It is backed by Redis and it is designed to have a low barrier to entry. It can be integrated in your web stack easily. <a name = "RQ"></a>

```
https://python-rq.org/
```

### GO <a name = "GO"></a> 

[Lightweight queue based on golang and redis](https://developpaper.com/lightweight-queue-based-on-golang-and-redis/)

```
https://developpaper.com/lightweight-queue-based-on-golang-and-redis/
```

#### GO <a name = "GO-RMQ"></a>

[RMQ](https://github.com/adjust/rmq)

#### GO <a name = "go-redis-queue"></a>

[go-redis-queue](https://github.com/AgileBits/go-redis-queue)

##### GO non-redis <a name = "go-bee-queue"></a>

[bee-queue](https://github.com/bee-queue/bee-queue)

## Redis Pub/Sub

### Python Samples

#### Python Pub/Sub [redis-pub-sub-with-python](https://beyondexperiment.com/vijayravichandran06/redis-pub-sub-with-python/)

[redis-pubsub-and-message-queueing](https://stackoverflow.com/questions/27745842/redis-pubsub-and-message-queueing)


(c). Copyright 2021, Ray C Horn, All Rights Reserved.