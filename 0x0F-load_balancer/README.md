# README

This readme provides a brief description of the concepts covered in this directory.

## Introduction to Load-Balancing and HAProxy

Load balancing is a technique used to distribute workloads uniformly across servers or other compute resources to optimize network efficiency, reliability and capacity. HAProxy, which stands for High Availability Proxy, is a popular open-source software that provides load balancer and proxy server for TCP and HTTP-based applications that spreads requests across multiple servers.

## HTTP Header

HTTP headers let the client and the server pass additional information with an HTTP request or response. An HTTP header consists of its case-insensitive name followed by a colon (`:`), then by its value. They are used for various purposes like authentication, caching, content-type information, etc.

## Debian/Ubuntu HAProxy Packages

HAProxy is available in the default repositories of Debian and Ubuntu operating systems and can be installed using the package manager `apt`. To install HAProxy on Debian/Ubuntu, you can use the following command:

```bash
sudo apt-get update
sudo apt-get install haproxy
```

This will install HAProxy and its dependencies on your machine.
