#ifndef _COMMON_H_
#define _COMMON_H_

#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h> // basic socket definition
#include <sys/types.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <stdarg.h>
#include <errno.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <netdb.h>
#include <strings.h>

// default HTTP port 80 (12000)
#define SERVER_PORT 12000

//buffer size to read the data
#define MAXLINE 1024 

//Structure describing an Internet socket address
#define SA struct sockaddr

//handle errors
void err_n_die(const char *fmt, ...);
//converts bytes in hexa
char *bin2hex(const unsigned char *input, size_t len);

#endif