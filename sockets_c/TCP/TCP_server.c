#include "common.h"

int main(int argc, char *argv[ ]){

    //local variables 
    int                 listenfd, connfd, n;
    struct sockaddr_in  servaddr;
    uint8_t             buff[MAXLINE+1];
    uint8_t             recvline[MAXLINE+1];
    char rec_mod[MAXLINE];

    //allocating resources 
    if ((listenfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
        err_n_die("Error while creating the socket");

    bzero(&servaddr, sizeof(servaddr));
        servaddr.sin_family      = AF_INET;
        servaddr.sin_addr.s_addr = htonl(INADDR_ANY); //responding to anything
        servaddr.sin_port        = htons(SERVER_PORT);

    //bind the listening socket to the address
        if ((bind(listenfd, (SA *) &servaddr, sizeof(servaddr))) < 0)
            err_n_die("bind error!");
        
        if((listen(listenfd, 10)) < 0)
            err_n_die("listen error!");

    for ( ; ; ){
        struct sockaddr_in addr;
        socklen_t addr_len;
        char client_address[MAXLINE+1]; 

        //accept blocks until an incoming connection arrives
        //it returns a "file descriptor" to the connection
        printf("waiting for a connection on port %d\n", SERVER_PORT);
        fflush(stdout);
        connfd = accept(listenfd, (SA *) &addr, &addr_len); //start accepting connections

        //convert the internet address in network format
        inet_ntop(AF_INET, &addr, client_address, MAXLINE);
        printf("Client connection : %s\n", client_address);

        //zero out the receive buffer to make sure it ends up null
        memset(recvline, 0, MAXLINE);

        //now read the client's message
        while ( (n = read(connfd, recvline, MAXLINE-1) ) > 0){
            fprintf(stdout, "\n%s\n\n%s", bin2hex(recvline, n), recvline);

            //detect the end of the message
            if(recvline[n-1] == '\n'){
                break;
            }
            memset(recvline, 0, MAXLINE);
        }
        

        if(n < 0)
            err_n_die("read error!");

        //programming application*
        for (int i = 0; i < (MAXLINE-1); i++){
            rec_mod[i] = (unsigned char)recvline[i];
        }
        char string1[MAXLINE] = "A mensagem recebida pelo servidor foi: ";
        strcat (string1, rec_mod);

        snprintf((char*)buff, sizeof(buff), "HTTP/1.0 200 OK %s\r\n\r\n", string1);

        write(connfd, (char*)buff, strlen((char *)buff));
        close (connfd);
    }
    exit(0);
}