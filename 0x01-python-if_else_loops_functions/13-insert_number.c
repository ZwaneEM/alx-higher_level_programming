#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked
 * list.
 * @head: The start of the list.
 * @number: Is the number to add to the list.
 * Return: the address of the new node, or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
		listint_t *slow_node, *fast_node, *new_node;

		if (!head)
		{
			return (NULL);
		}

		slow_node = *head;
		fast_node = (*head)->next;

		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);

		new_node->n = number;
		new_node->next = NULL;

		while (fast_node != NULL)
		{
			if (fast_node->n >= number)
			{
				new_node->next = slow_node->next;
				slow_node->next = new_node;
				return (*head);
			}
			slow_node = slow_node->next;
			fast_node = fast_node->next;
		}

		if (fast_node == NULL)
			slow_node->next = new_node;

		return (*head);
}
