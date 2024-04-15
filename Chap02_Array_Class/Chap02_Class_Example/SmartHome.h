#pragma once
#include <iostream> // input output 쉽게 사용
#include <string>  // 문자열
using namespace std; // std 라이브러리 namespace 설정

// SmartHome
class SmartHome {
private:
        // 클래스 변수들 (member variable, attribute, field)
    string owner;
    int temperature;
    int humidity;
    bool security;
public:
    // 클래스 변수들 (class function, method)
    // 생성자
    SmartHome(string owner, int temperature, int humidity, bool security) {
        this->owner = owner;
        this->temperature = temperature;
        this->humidity = humidity;
        this->security = security;
    }
    //parameter, argument
    /*
    SmartHome(string o, int t, int h, bool s)
        : temperature(t), humidity(h), security(sec) {
        strcpy(owner, o):
    }*/
    // 소멸자 
    //~SmartHome() {}

    void setTemperature(int temperature) {
        this->temperature = temperature;
    }
    void setHumidity(int humidity) {
        this->humidity = humidity;
    }
    void setSecurity(bool security) {
        this->security = security;
    }
    string getOwner() {
        return this->owner;
    }
    int getTemperature() {
        return this->temperature;
    }
    int getHumidity() {
        return this->humidity;
    }
    bool getSecurity() {
        return this->security;
    }
    void printStatus() {
        cout << ": " << this->owner << endl;
        cout << "온도: " << this->temperature << "도" << endl;
        cout << "습도: " << this->humidity << "%" << endl;
        if (this->security) {
            cout << " security on" << endl;
        }
        else {
            cout << "security off" << endl;
        }
    }
};