CC		=clang
TARGETS	=tcpc tcps
OBJFILES	=TCP_client.o common.o TCP_server.o
all 		=tcpc tcps

all: tcpc tcps

tcpc: TCP_client.o common.o
	$(CC) -g -c common.c
	$(CC) -o tcpc TCP_client.c common.c
     	
tcps: TCP_server.o common.o
	$(CC) -g -c common.c
	$(CC) -o tcps TCP_server.c common.c

clean: 
	rm -rf $(OBJFILES) $(TARGETS)
