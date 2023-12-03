#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: The start of the list
 * Return: 0 if it is not, 1 if is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int leng = length_list(head);
	int is_pal = 0;

	is_pal += arr_counter(head, leng);

	return (is_pal);
}

/**
 * length_list - it gets the length of the list
 * @head: start of the list
 * Return: The length of a list
 */
int length_list(listint_t **head)
{
	int count = 0;
	listint_t *itr = (*head);

	while (itr != NULL)
	{
		count++;
		itr = itr->next;
	}

	return (count);
}

/**
 * arr_counter - creates an array of integer and checks
 * if they are palindrome
 * @head: The start of the list
 * @leng: Length of the list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int arr_counter(listint_t **head, int leng)
{
	int *arr_list;
	listint_t *itr = (*head);
	int i = 0, v;
	int leng_cpy = 0;


	arr_list = malloc(sizeof(int) * leng);
	if (arr_list == NULL)
		return (-1);

	while (itr != NULL)
	{
		arr_list[i] = itr->n;
		itr = itr->next;
		i += 1;
	}

	leng_cpy += leng;

	if (leng % 2 != 0)
	{
		leng -= 1;
		leng = (leng / 2) + 1;
	}

	else
		leng /= 2;

	for (i = 0, v = (leng_cpy - 1); i < leng; i++, v--)
	{
		if (arr_list[i] != arr_list[v])
			return (0);
	}
	free(arr_list);
	return (1);
}
