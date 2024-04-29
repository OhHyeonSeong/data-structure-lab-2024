#include "Location2D.h"
#include <queue>
using namespace std;

#define MAZE_SIZE  6

char map[MAZE SIZE][MAZE_SIZE] = {
	{'1', '1', '1', '1', '1', '1'},
	{'e', '0', '1', '0', '0', '1'},
	{'1', '0', '0', '0', '1', '1'},
	{'1', '0', '1', '0', '1', '1'},
	{'1', '0', '1', '0', '0', 'x'},
	{'1', '1', '1', '1', '1', '1'},
};

bool inValidLoc(int r, int c)
{
	if (r < 0 || c < 0 || r >= MAZE_SIZE || c >= MAZE_SIZE)
		return false;
	else 
		return map[r][c] == '0' || map[r][c] == 'x'
}

int main()
{
	deque<Location2D> locDeque;
	Location2D emtry(1, 0);
	locDeque.push_front(entry);

	while (locDeque.empty() == false) {
		Location2D here = locDeque.front();
		locDeque.pop_front();

		int r = here.row;
		int c = here.col;

		printf("현재 위치 = (%d, %d)", r, c);
		if (map[r][c] == 'x') {
			printf("출구 도착 \n");
			return;
		}
	}
}