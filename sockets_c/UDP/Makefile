CC		=clang
TARGETS	=udpc udps
OBJFILES	=UDP_client.o common.o UDP_server.o
all 		=udpc udps

all: udpc udps

udpc: UDP_client.o common.o
	$(CC) -g -c common.c
	$(CC) -o udpc UDP_client.c common.c
     	
udps: UDP_server.o common.o
	$(CC) -g -c common.c
	$(CC) -o udps UDP_server.c common.c

clean: 
	rm -rf $(OBJFILES) $(TARGETS)
