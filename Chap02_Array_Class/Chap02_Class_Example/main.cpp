#include <cstdio>
#include "Car.h"
#include "sportsCar.h"
#include "Rectangle.h"
#include SmartHome.h
#include "Music.h"


int main() {
    // Car 클래스 사용
    /* Car myCar(50, "K3", 4);
    Car yourCar(100, "K5", 3);
    myCar.display();
    yourCar.display();
    myCar.whereAmI();
    yourCar.whereAmI();
    //sportsCar 클래스 사용
    SportsCar scar;
    scar.speedUp();
    
    Rectangle r(10, 20);
    double perimeter = r.getPerimeter();
    std::cout << "Rectangle 1:" << std::endl;
    std::cout << "Area: " << r.getArea() << std::endl;
    std::cout << "Perimeter" << perimeter << std::endl;
    std::cout << "Is square?" << std::boolalpha << r.isSquare() << std::endl;
}*/

// Smarthome Class
/*SmartHome myHome("오현성", 23, 40, true);
myHome.printStatus():
*/


		//Music Streaming Service 
		MusicStreamingService myService("Spotify");
	myService.addMusic("VIBE", "Taeyang", "Album", 2023);
	myService.addMusic("Ditto", "NewJeans", "Album", 2023);
	myService.addMusic("Attention", "NewJeans", "Album", 2023);

	string music_title;
	cout << "Enter the Music Title : ";
	cin >> music_title;

	Music* result = myService.searchByTitle(music_title);
	if (result != NULL) {
		cout << "found: " << result->getTitle() << " by " << result->getArtist() << endl;

	}
	else {
		cout << "Not found" << endl;
	}

	string artist_name;
	cout << "Enter the Artist Name : ";
	cin >> artist_name;

	vector<Music>* > artistResult = myService.searchByArtist(artist_name);
	if (artistResult.size() > 0) {
		cout << "Found " << artistResult.size() << " songs by " << artist_name << " : " << endl;
		for (int i = 0; i < artistResult.size(); i++) {
			cout << artistResult[i]->getTitle() << endl;
		}
	}
	else {
		cout << "not found" << endl;
	}