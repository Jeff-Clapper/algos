#O(n) result with an option for-loop to make the code ledgible. If the second for loop is run, results are then O(2n)

DNs=[
"CN=Server001,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server002,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server003,OU=INDIA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server004,OU=CHINA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server005,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server006,OU=EMEA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server007,OU=CHINA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server008,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server009,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server010,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server011,OU=CHINA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server012,OU=CHINA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server013,OU=INDIA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server014,OU=EMEA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server015,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server016,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server017,OU=INDIA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server018,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server019,OU=CHINA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server020,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server021,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server022,OU=EMEA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server023,OU=EMEA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server024,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server025,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server026,OU=INDIA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server027,OU=CHINA,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server028,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server029,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com",
"CN=Server030,OU=AMER,OU=Servers,OU=Corp,DC=Dogfood,DC=com"
]

def server_count2(arr):
    sorted_servers = {}
    for server in arr:
        server_info=(server.split(','))

        if server_info[1][3:] not in sorted_servers:
            sorted_servers[server_info[1][3:]] = [server_info[0][3:]]
        else:
            sorted_servers[server_info[1][3:]].append(server_info[0][3:])

    return sorted_servers

def ledgible_results(dictionary):
    for location,servers in dictionary.items():
        print(f'{location} has {len(servers)}:')
        for server in servers:
            print('\t',server)



all_servers = server_count2(DNs)
print("the results from the return statement:")
print(all_servers, "\n")

print("results after makeing results readable: ")
ledgible_results(all_servers)


