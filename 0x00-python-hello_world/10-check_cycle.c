#include "lists.h"

/**
* check_cycle - checks to if a singly linked list
* contains a cycle
* @list: The list to inspect
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *current, *previous;

	if (!list || !list->next)
		return (0);

	current = list->next;
	previous = list->next->next;

	while (current && previous && previous->next)
	{
		if (current == previous)
			return (1);

		current = current->next;
		previous = previous->next->next;
	}
	return (0);
}
