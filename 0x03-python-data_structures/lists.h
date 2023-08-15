#ifndef LISTS_H
#define LSITS_H

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listinit_t **head, const int n);
void free_listint(listint_t *head);

void reverse_listint(listiint_t **head);
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
