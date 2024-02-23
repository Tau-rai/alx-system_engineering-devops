# README

This readme provides brief descriptions of the concepts covered in this repository through doing project tasks. 

## What is a Server

A server is a computer or system that provides resources, data, services, or programs to other computers, known as clients, over a network. In theory, whenever computers share resources with client machines they are considered servers.

## Where Servers Usually Live

Servers usually live in data centers. A data center is a facility used to house computer systems and related components, such as telecommunications and storage systems. It generally includes redundant or backup power supplies, redundant data communications connections, environmental controls (e.g., air conditioning, fire suppression), and various security devices.

## What is SSH

SSH, or Secure Shell, is a cryptographic network protocol for operating network services securely over an unsecured network. Typical applications include remote command-line, login, and remote command execution, but any network service can be secured with SSH.

## How to Create an SSH RSA Key Pair

You can create an SSH RSA key pair using the following command in your terminal:

```bash
ssh-keygen -t rsa
```

This command will prompt you to enter a file in which to save the key. You can press enter to accept the default location. You'll then be asked to optionally enter a passphrase for the key.

## How to Connect to a Remote Host Using an SSH RSA Key Pair

To connect to a remote host using an SSH RSA key pair, you can use the following command:

```bash
ssh -i /path/to/your/private/key username@hostname
```

Replace `/path/to/your/private/key` with the path to your private key file, `username` with your username on the remote host, and `hostname` with the hostname or IP address of the remote host.

## The Advantage of Using #!/usr/bin/env bash Instead of /bin/bash

The `#!/usr/bin/env bash` shebang has the advantage of looking for wherever the `bash` interpreter is installed, and running it. This makes scripts more portable across different systems where Bash might not be installed in the same location.
