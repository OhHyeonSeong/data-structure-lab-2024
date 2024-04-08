#include <cstdio>
#include "Car.h"
#include "sportsCar.h"
#include "Rectangle.h"

int main() {
    // Car Ŭ���� ���
    /* Car myCar(50, "K3", 4);
    Car yourCar(100, "K5", 3);
    myCar.display();
    yourCar.display();
    myCar.whereAmI();
    yourCar.whereAmI();
    //sportsCar Ŭ���� ���
    SportsCar scar;
    scar.speedUp();
    */
    Rectangle r(10, 20);
    double perimeter = r.getPerimeter();
    std::cout << "Rectangle 1:" << std::endl;
    std::cout << "Area: " << r.getArea() << std::endl;
    std::cout << "Perimeter" << perimeter << std::endl;
    std::cout << "Is square?" << std::boolalpha << r.isSquare() << std::endl;
}
       