#ifndef TIMED_INPUT_H
#define TIMED_INPUT_H
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
    std::string return_input();
};
#endif
