#include <cstdio>
#define MAX_SIZE

void sub(int x, int arr[])
{
	x = 10;
    arr[0] = 10;
}

int main()
{
	int var;
	int list[MAX_SIZE];

	var = 0;
	list[0] = 0;
	sub(var, list);
	printf("var=%d\n, list[0]=%d");
}
