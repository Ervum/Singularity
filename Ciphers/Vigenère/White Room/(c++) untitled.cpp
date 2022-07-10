#include <chrono>
#include <string>
#include <cstdlib>
#include <iostream>

int main()
{
    union
    {
        double d;
        char c[8];
    };
    d = std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
    const char displacement = std::abs(c[0] ^ c[1] ^ c[2] ^ c[3] ^ c[4] ^ c[5] ^ c[6] ^ c[7]);
    std::string i, o;
    std::cout << "Your input message:\n";
    std::cin >> i;
    o.reserve(i.size());
    for(const char ch : i)
        o.append(1ull, (ch + ((ch + displacement) % 128)) % 128);
    std::cout << "Your output: " << o;
}
