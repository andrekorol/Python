#include "timed_input.hpp"
#include <iostream>

int main() {
    std::string prompt;
    std::cout << "Enter the prompt: ";
    std::getline(std::cin, prompt, '\n');
    long int time_limit;
    std::cout << "\nEnter the time limit for the input(in seconds): ";
    std::cin >> time_limit;
    std::cout << "\n";
    TimedInput timedout (prompt, time_limit);

    std::string answer = timedout.return_input();

    if (answer.empty()) {
	std::cout << time_limit << " seconds time limit exceeded!\n";
    }
    else {
	std::cout << "Your answer was: " << answer << "\n";
    }

    return 0;
}
