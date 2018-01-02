#pragma once

#ifdef TIMEDINPUT_EXPORTS  
#define TIMEDINPUT_API __declspec(dllexport)   
#else  
#define TIMEDINPUT_API __declspec(dllimport)   
#endif  

#include <condition_variable>
#include <string>
#include <chrono>

class TimedInput {
    std::condition_variable cv;
    std::string prompt, input_string;
    long int li_time_limit;
    std::chrono::seconds time_limit;
public:
    TimedInput(std::string, long int);
    void read_string();
	const char * return_input();
};
