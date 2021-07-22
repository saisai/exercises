#include <chrono>
#include <iostream>
#include <thread>
#include <vector>

int main(int argc, char* argv[]) {
  std::vector<std::thread> threads;

  for (int i = 1; i < argc; ++i) {
    threads.emplace_back([i, &argv]() {
      int arg = std::stoi(argv[i]);
      std::this_thread::sleep_for(std::chrono::seconds(arg));
      std::cout << argv[i] << std::endl;
    });
  }

  for (auto& thread : threads) {
    thread.join();
  }
}

// g++ -lpthread
// ./a.out 8 15 14 9 17 20 16 24 6 24 21 23 19 23 19
