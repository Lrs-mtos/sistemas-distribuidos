#include "common.h"

int main(){

    //local variables 
    unsigned int     sockfd, len, n;
    char*   string = "Batata frita\r\n\r\n";
    struct  sockaddr_in servaddr;
    uint8_t             buff[MAXLINE+1];

    if( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 )
        err_n_die("Error while creating the socket");
    
    bzero(buff, MAXLINE);
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(SERVER_PORT); //host to network, short
    servaddr.sin_addr.s_addr = INADDR_ANY;

    if ((len = sendto(sockfd, (const char *)string, strlen(string),
    0, (const struct sockaddr*)&servaddr, sizeof(servaddr))) < 0)
        err_n_die("Error while sending message");

    bzero(buff, MAXLINE);

    n = recvfrom(sockfd, (char *)buff, MAXLINE,  
                MSG_WAITALL, (struct sockaddr *) &servaddr, 
                &len); 
    buff[n] = '\0'; 

    printf("Message sent to server: %s\n", string);
    printf("The message recieved from server was: %s\n", buff); 

    
    close(sockfd);

    exit(0);
}
