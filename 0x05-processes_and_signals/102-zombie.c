# include "stdio.h"
# include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - a function that runs infinitely and returns nothing
 * Return: 0 in the end
 */
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
 * main - the entry program that creates 5 zombie processes
 * Return: 0 on success
 */
int main(void)
{
int children_processes = 0;
pid_t pid;

while (children_processes < 5)
{
pid = fork();
if (!pid)
break;
printf("Zombie process created, PID: %i\n", (int)pid);
children_processes++;
}
if (pid != 0)
infinite_while();
return (0);
}
