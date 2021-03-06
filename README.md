dynash
======

A simple "shell" to access DynamoDB via "boto".

You can create/delete/list/describe tables, add/modify/delete/list records and more.

- ls: list tables

- create {tablename}: create table

- delete {tablename}: delete table

- describe {tablename}: describe table

- capacity {tablename} {read_capacity} {write_capacity}: update table capacity

- use {tablename}: select table

- scan/l: list table content

- get {id}: get item(s) from table

- put {id} {properties}: add item to table

- update {id} {properties}: update item

- rm {id}: remove item from table

- query/q: query table 

and many more (use 'help' to find the available commands)

### Config:
- Credentials should be in your boto config file (see http://docs.pythonboto.org/en/latest/boto_config_tut.html)
- You can specify the AWS Region to connect to in your /etc/boto.cfg file. If it is not specified, it will use the default (us-east-1).

For example:
<pre>
[Credentials]
aws_access_key_id=YOUR_ACCESS_KEY_ID
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY

[dynamodb]
region=eu-west-1
</pre>

### Note:

- Item related commands use the currently selected table (see 'use' command) but you can pass a table name as first parameter prefixed by ':'
 
- Command completion is enabled (and it will complete table names)

- You can set various flags (like debug, verbose, pretty-print, etc.) using the 'set' command (try 'set -l')k

- You can redirect the output of commands using standard shell redirection ( > outfile )

- You can execute shell commands using '!shell command'

