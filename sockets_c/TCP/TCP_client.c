#include "common.h"

int main(int argc, char *argv[ ]){

    //local variables 
    int     sockfd, n, sendbytes;
    struct  sockaddr_in servaddr;
    char    sendline[MAXLINE], recvline[MAXLINE];

    //usage check
    if(argc != 2)   
        err_n_die("usage : %s <server address>", argv[0]);

    /*
    AF_INET     -> Address Family - Internet
    SOCK_STREAM -> Stream Socket (send stream of data, instead of a chunck)
    0           -> standart for TCP 
    */

    if( (sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0 )
        err_n_die("Error while creating the socket");

    //to zero out
    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(SERVER_PORT); //host to network, short

    //string IP binary representation "1.2.3..." => [1,2,3...]
    if (inet_pton(AF_INET, argv[1], &servaddr.sin_addr) <= 0)
        err_n_die("inet_pton error for %s ", argv[1]);

    //trying connection with server
    if( connect(sockfd, (SA *) &servaddr, sizeof(servaddr)) < 0 )
        err_n_die("connect failed!");

    /*
    connected! Preparing message.
    requesting webpage and finishing.
    */
    
    sprintf(sendline, "Batata doce quente \r\n\r\n");
    sendbytes = strlen(sendline);

    //write request into the socket
    if (write(sockfd, sendline, sendbytes) != sendbytes)
        err_n_die("write error!");

    //receive and print the response
    memset(recvline, 0, MAXLINE);
    //now read the server's response
    while ((n = read(sockfd, recvline, MAXLINE-1)) > 0){
        printf("%s", recvline);
    }
    if (n < 0)
        err_n_die("read error!");

    exit(0);
}
