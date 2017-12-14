#include <iostream>
#include <thread>
#include <chrono>
#include <mutex>
#include <condition_variable>
#include <string>
#include <ctime>

std::condition_variable cv;

std::string str;

void read_string() {
    std::cin >> str;
    cv.notify_one();
}

int main() {
    std::cout << "Please enter your name: ";
    std::thread th(read_string);

    std::mutex mtx;
    std::unique_lock<std::mutex> lck(mtx);
    while ((cv.wait_for(lck, std::chrono::seconds(5)) != std::cv_status::timeout) and (str.empty())) {
	
    }
    while (str.empty()) {
	
    	std::time_t current = time(0);
    	std::string tempo = std::ctime(&current);
        tempo.resize( tempo.length() - 1 );
    	std::cout << "\r" << tempo << "\nPlease enter your name: " << std::flush;
    }

    std::cout << str << "\n";
    
    th.detach();
    
    return 0;
}
