#include "common.h"

int main(int argc, char *argv[ ]){

    //local variables 
    int                 sockfd, n;
    struct sockaddr_in  servaddr, client_addr;
    uint8_t             buff[MAXLINE+1];
    socklen_t           addr_size;
    char rec_mod[MAXLINE];

    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0)
        err_n_die("Error while creating the socket");
    
    memset(&servaddr, '\0', sizeof(servaddr));

    bzero(buff, MAXLINE);
    servaddr.sin_family      = AF_INET;
    servaddr.sin_port        = htons(SERVER_PORT);
    servaddr.sin_addr.s_addr = INADDR_ANY;

    if ((bind(sockfd, (SA *) &servaddr, sizeof(servaddr))) < 0)
        err_n_die("bind error!");

    for ( ; ; ){

        printf("waiting for a connection on port %d\n", SERVER_PORT);
        fflush(stdout);

        addr_size = sizeof(client_addr);
        bzero(buff, sizeof(buff));

        //get message from client
        n = recvfrom(sockfd, (char *)buff, sizeof(buff), 0,
        (struct sockaddr*)&client_addr, &addr_size);


        //programming application*
        for (int i = 0; i < n; i++){
            rec_mod[i] = (unsigned char)buff[i];

            if(rec_mod[i-1] == '\n'){
                break;
            }
        }
        char string1[MAXLINE] = "Tudo fica melhor com ";
        strcat (string1, rec_mod);

        bzero(buff, MAXLINE);
        printf("Message recieved from client: %s", buff);
        printf("Message sent to client: %s \n", string1);

        sendto(sockfd, string1, MAXLINE, MSG_CONFIRM, (struct sockaddr*)&client_addr, sizeof(client_addr));

    }
    exit(0); 
}