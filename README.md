# Python Redis Sample 1

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Redis Queuing Prototype

## Getting Started <a name = "getting_started"></a>

Simulate a Queue using Redis as the database.

### Prerequisites

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

### RQ [Redis Queue](https://python-rq.org/) is a simple Python library for queueing jobs and processing them in the background with workers. It is backed by Redis and it is designed to have a low barrier to entry. It can be integrated in your web stack easily.

```
https://python-rq.org/
```

### GO  [Lightweight queue based on golang and redis](https://developpaper.com/lightweight-queue-based-on-golang-and-redis/)

```
https://developpaper.com/lightweight-queue-based-on-golang-and-redis/
```

(c). Copyright 2021, Ray C Horn, All Rights Reserved.