#include "timed_input.hpp"
#include <iostream>
#include <thread>
#include <chrono>
#include <mutex>
#include <condition_variable>

TimedInput::TimedInput(std::string prompt_str, long int time) : prompt{prompt_str}, li_time_limit{time} { }


void TimedInput::read_string() {
    std::cin >> input_string;
    cv.notify_one();
}

std::string TimedInput::return_input() {
    std::cout << "Time limit for input = " << li_time_limit << " seconds!\n" << prompt << "\n";
    std::thread th(&TimedInput::read_string, this);
    
    std::mutex mtx;
    std::unique_lock<std::mutex> lck(mtx);
    time_limit = (std::chrono::seconds) li_time_limit;
    
    while ((cv.wait_for(lck, time_limit) != std::cv_status::timeout) && (input_string.empty())) { }
    
    th.detach();
    
    return input_string;
}


extern "C" {
    TimedInput* TimedInput_new(std::string prompt, long int time_limit) { return new TimedInput(prompt, time_limit); }
    void TimedInput_read_string(TimedInput* timed_input) { timed_input->read_string(); }
    std::string TimedInput_return_input(TimedInput* timed_input) { return timed_input->return_input(); }
}
