#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - create an infinite loop
 * Return: Always 0
**/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Generates 5 zombie processes
 * Return: Always 0
**/

int main(void)
{
	int m;
	pid_t zombie;

	for (m = 0; m < 5; m++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}

	infinite_while();
	return (0);
}
