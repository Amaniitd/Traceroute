from scapy.all import *
import matplotlib.pyplot as plt
domain = input("Enter the domain name: ")
hops = []
RTT = []
for i in range(1, 30):
    packet = IP(dst=domain, ttl=i) / UDP(dport=33434)
    response = sr1(packet, verbose=0)
    if response is None:
        break
    elif response.type == 3:
        hops.append(response.src)
        RTT.append(response.time - packet.sent_time)
        break
    hops.append(response.src)
    RTT.append(response.time - packet.sent_time)
numbers = [1]
print("IP addresses of all the hops:")
print(hops[0])
for i in range(1, len(RTT)):
    print(hops[i])
    numbers.append(i+1)
# print(hops)
# print(RTT)
plt.plot(numbers, RTT)
plt.xlabel('No of hops')
plt.ylabel('RTT')
plt.title('RTT vs hops')
plt.savefig('output.png')
plt.show()
